import threading
from time import sleep


from kortex_api.Exceptions.KException import KException
from kortex_api.Exceptions.KServerException import KServerException
from kortex_api.autogen.client_stubs.BaseClientRpc import BaseClient
from kortex_api.autogen.client_stubs.BaseCyclicClientRpc import BaseCyclicClient
from kortex_api.autogen.client_stubs.DeviceConfigClientRpc import DeviceConfigClient
from kortex_api.autogen.client_stubs.GripperCyclicClientRpc import GripperCyclicClient
from kortex_api.autogen.messages import Base_pb2, BaseCyclic_pb2, DeviceConfig_pb2, Common_pb2

from robot_api.robot.abstract_robot import AbstractRobot
from robot_api.robot.robot_connection import RobotConnection
from robot_api.robot.utils.functions import read_joints_from_json

class Robot(AbstractRobot):

    def run_python_file(file_path):
        try:
            with open(file_path, 'r') as file:
                code = file.read()
                exec(code)
                print(f"Python file '{file_path}' executed successfully.")
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error: {e}")
    
    def connect(self, connection_ip: str = "192.168.2.10"):       
        self.device = RobotConnection.create_tcp_connection(connection_ip)
        self.router = self.device.connect()

        # Create required services
        self.base = BaseClient(self.router)
        self.gripper = GripperCyclicClient(self.router)
        self.base_cyclic = BaseCyclicClient(self.router)
        self.device_config = DeviceConfigClient(self.router)
        self.check_error()
        if self.critical_error:
            self.clear_faults()
        else:
            self.base_feedback = BaseCyclic_pb2.BaseFeedback()
            self.open_tool(0.70)

    def disconnect(self):       
        if not self.device:
            return
        self.device.disconnect()
        self.base = None
        self.base_cyclic = None
        self.device = None
        self.router = None

    def move_to_home(self):       
        positions_dict = read_joints_from_json()
        home = positions_dict['home']
        self.move_joints(home)  # TODO positions from json, home
        self.open_tool(0.70)

    def move_joints(self, joints_list):       
        feedback = self.base_cyclic.RefreshFeedback()

        # TODO: Essa checagem de erro tem que estar em outro canto, não deve estar aqui dentro dessa classe nem desse
        #  método.
        self.feedback_list = [feedback.base.fault_bank_a, feedback.base.fault_bank_b,
                              feedback.base.warning_bank_a, feedback.base.warning_bank_b]

        self.get_arm_state()
        self.get_safety_status()

        self.action = Base_pb2.Action()
        self.action.name = "Example angular action movement"
        self.action.application_data = ""

        # Place arm straight up
        for joint_id in range(len(joints_list)):
            joint_angle = self.action.reach_joint_angles.joint_angles.joint_angles.add()
            joint_angle.joint_identifier = joint_id
            joint_angle.value = joints_list[joint_id]

        finished = self.__detection_move(Base_pb2)

        if self.arm_state_notif_handle is not None:
            self.base.Unsubscribe(self.arm_state_notif_handle)

        return finished

    def move_cartesiann(self, pose_list):
        """
        Set movement for robot with cartesian coordinates
        Args:
            (float) pose[0]: x value
            (float) pose[1]: y value
            (float) pose[2]: z value
            (float) theta_x: theta_x value
            (float) theta_y: theta_y value
            (float) theta_z: theta_z value

        Returns:
            (bool): Move is finished
        """
        self.action = Base_pb2.Action()
        self.action.name = "Example Cartesian action movement"
        self.action.application_data = ""

        cartesian_pose = self.action.reach_pose.target_pose
        cartesian_pose.x = pose_list[0]  # [meters]
        cartesian_pose.y = pose_list[1]  # [meters]
        cartesian_pose.z = pose_list[2]  # [meters]
        cartesian_pose.theta_x = pose_list[3]  # [degrees]
        cartesian_pose.theta_y = pose_list[4]  # [degrees]
        cartesian_pose.theta_z = pose_list[5]  # [degrees]

        finished = self.__detection_move()

        return finished

    def close_tool(self) -> bool:
        """
        This function closes the gripper and tries detected object
        Returns:
            (bool): object_detect: returns whether an object was detected or not detected
        """
        object_detected = False

        while not object_detected and float(self.atribute_from_gripper()["position"]) < 97:
            gripper_command = Base_pb2.GripperCommand()
            finger = gripper_command.gripper.finger.add()
            gripper_command.mode = Base_pb2.GRIPPER_POSITION
            finger.finger_identifier = 1
            finger.value = (float(self.atribute_from_gripper()["position"]) + 1.7) / 100
            self.base.SendGripperCommand(gripper_command)

            current = float(self.atribute_from_gripper()["current_motor"])
            if 4 < current:
                print("atypical current 1")
                print(current)
                current = 0

            if current > 0.65:
                finger.value = (float(self.atribute_from_gripper()["position"]) + 1.3) / 100
                self.base.SendGripperCommand(gripper_command)
                current = float(self.atribute_from_gripper()["current_motor"])
                if current > 0.58:
                    object_detected = True

        return object_detected

    def open_tool(self, value=0.70):
        """
        Open griper with value
        Args
            :(float) value: Value for open grips
        """
        self.gripper_command = Base_pb2.GripperCommand()
        finger = self.gripper_command.gripper.finger.add()

        self.gripper_command.mode = Base_pb2.GRIPPER_POSITION
        finger.finger_identifier = 1
        finger.value = value
        self.base.SendGripperCommand(self.gripper_command)

        sleep(2)

    