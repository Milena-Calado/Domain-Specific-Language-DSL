#! /usr/bin/env python3
import threading
from time import sleep

from kortex_api.Exceptions.KException import KException
from kortex_api.Exceptions.KServerException import KServerException
from kortex_api.autogen.client_stubs.BaseClientRpc import BaseClient
from kortex_api.autogen.client_stubs.BaseCyclicClientRpc import BaseCyclicClient
from kortex_api.autogen.client_stubs.DeviceConfigClientRpc import DeviceConfigClient
from kortex_api.autogen.client_stubs.GripperCyclicClientRpc import GripperCyclicClient
from kortex_api.autogen.messages import Base_pb2, BaseCyclic_pb2, DeviceConfig_pb2, Common_pb2

from abstract_robot import AbstractRobot
from robot_connection import RobotConnection


TIMEOUT_DURATION = 20

# This dict it contains all error lists and what have to do in each case
error_list = {4: "MAXIMUM_AMBIENT_TEMPERATURE", 8: "MAXIMUM_CORE_TEMPERATURE", 16: "JOINT_FAULT",
              256: "BRAKE_REMOVAL_FAILURE", 1024: "UNABLE_TO_REACH_POSE", 2048: "JOINT_DETECTION_ERROR",
              4096: "NETWORK_INITIALIZATION_ERROR", 8192: "MAXIMUM_CURRENT", 16384: "MAXIMUM_VOLTAGE",
              32768: "MINIMUM_VOLTAGE", 65536: "MAXIMUM_END_EFFECTOR_TRANSLATION_VELOCITY",
              131072: "MAXIMUM_END_EFFECTOR_ORIENTATION_VELOCITY",
              262144: "MAXIMUM_END_EFFECTOR_TRANSLATION_ACCELERATION",
              524288: "MAXIMUM_END_EFFECTOR_ORIENTATION_ACCELERATION",
              1048576: "MAXIMUM_END_EFFECTOR_TRANSLATION_FORCE", 2097152: "MAXIMUM_END_EFFECTOR_ORIENTATION_FORCE",
              4194304: "MAXIMUM_END_EFFECTOR_PAYLOAD",
              16777216: "EMERGENCY_LINE_ACTIVATED", 33554432: "INRUSH_CURRENT_LIMITER_FAULT",
              67108864: "NVRAM_CORRUPTED", 134217728: "INCOMPATIBLE_FIRMWARE_VERSION",
              268435456: "POWERON_SELF_TEST_FAILURE", 536870912: "DISCRETE_INPUT_STUCK_ACTIVE",
              1073741824: "ARM_INTO_ILLEGAL_POSITION"}
INCREMENT = (1.3, 1.5, 1.7)


class Robot(AbstractRobot):
    
    """
    This class is responsible for the robot connection and movement. Now, the robot used is the Kinova Gen3 Lite.
    The methods implemented in this class are the basic movements of the robot, such as cartesian and joints movements.
    This class implements the AbstractRobot class, which has the basic methods for the robot.
    """
    def __init__(self):
        self.base = None
        self.error = None
        self.router = None
        self.action = None
        self.device = None
        self.gripper = None
        self.base_cyclic = None
        self.active_state = None
        self.error_number = None
        self.safety_status = None
        self.robot_stopped = None
        self.base_feedback = None
        self.device_config = None
        self.gripper_command = None
        self.arm_state_notif_handle = None
        self.safety_state_notif_handle = None
        self.critical_error = False
        self.feedback_list = []
        self.action_list = []

    def execute_python_script(self, file_path):
        try:
            print(f"Reading file: {file_path}")
            with open(file_path, 'r') as file:
                code = file.read()               
                exec(code)
                print(f"Python file '{file_path}' executed successfully.")
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error: {e}")
    

    def connect(self, connection_ip: str = "192.168.2.10"):
        # TODO change this class for connect with cabe ethernet or use cabe
        """
        Connect api with the robot, using the ethernet connection ip as default connection
        """
        # Create a connection to the device and get the router
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
        """
        Finish connection with robot
        """
        if not self.device:
            return
        self.device.disconnect()
        self.base = None
        self.base_cyclic = None
        self.device = None
        self.router = None

    def check_for_end_or_abort(self, e):
        # TODO identify right error
        """
        Return a closure checking for END or ABORT notifications

        Args:
            (any) e: event to signal when the action is completed
            (will be set when an END or ABORT occurs)
        """

        def check(notification, event=e):
            if notification.action_event == Base_pb2.ACTION_ABORT:
                event.set()
                print(event)
                if notification.abort_details == Base_pb2.ROBOT_IN_FAULT:
                    event.set()
                    print(event)
            if notification.action_event == Base_pb2.ACTION_END:
                event.set()

        return check

    def check_error(self):
        """
        This function handle, analyzing and identifies robot errors call when robot tries move and change the status
        message robot

        Returns:
        (bool): from state machine
        """
        if (self.base.GetArmState().active_state == Base_pb2.ARMSTATE_IN_FAULT or
                self.base.GetArmState().active_state == Base_pb2.ARMSTATE_SERVOING_LOW_LEVEL):
            if (self.base_cyclic.RefreshFeedback().base.fault_bank_a in error_list or
                    self.base_cyclic.RefreshFeedback().base.fault_bank_b in error_list):
                error_number = int(error_list.get(self.base_cyclic.RefreshFeedback().base.fault_bank_a))
                self.critical_error = True
                self.error_number = error_number
                return False
            else:
                self.critical_error = False
                return False
        elif self.base_cyclic.RefreshFeedback().base.warning_bank_a != 0 or \
                self.base_cyclic.RefreshFeedback().base.warning_bank_b != 0:
            if self.base_cyclic.RefreshFeedback().base.warning_bank_a != 0:
                error_number = self.base_cyclic.RefreshFeedback().base.warning_bank_a
            else:
                error_number = self.base_cyclic.RefreshFeedback().base.warning_bank_b

            self.critical_error = False
            self.error_number = error_number
            return False

        elif self.base.GetArmState().active_state == 3:
            return True

        return True

    def get_arm_state(self):
        def callback_arm_state(data):
            if data.active_state == Base_pb2.ARMSTATE_IN_FAULT:
                self.active_state = data.active_state

            if data.active_state == Common_pb2.ARMSTATE_SERVOING_PLAYING_SEQUENCE:
                self.active_state = data.active_state

        try:
            self.arm_state_notif_handle = \
                self.base.OnNotificationArmStateTopic(callback_arm_state,
                                                      Base_pb2.NotificationOptions())
        except KException as k_ex:
            print("kexception ", k_ex)

    def get_safety_notification(self):
        def callback_safety(data):
            try:
                self.arm_state_notif_handle = \
                    self.device_config.OnNotificationSafetyTopic(callback_safety,
                                                                 DeviceConfig_pb2.NotificationOptions())

            except KException as k_ex:
                print("kexception ", k_ex)

    def get_safety_status(self):
        def callback_arm_state(data):
            self.safety_status = data.safety_handle.identifier

        try:
            self.safety_state_notif_handle = \
                self.device_config.OnNotificationSafetyTopic(callback_arm_state,
                                                             DeviceConfig_pb2.NotificationOptions())
        except Exception as k_ex:
            print("kexception ", k_ex)

    def get_safety_list(self):

        return self.base.SafetyNotificationList

    def __detection_move(self, obj_notification: object = Base_pb2):
        """
        Create a thread and finish robot move
        Args:
            (Any) action: Instructions for movement or joints or cartesian

        Returns:
            (bool): Move is finished
        """

        e = threading.Event()

        if obj_notification == Base_pb2:
            notification_handle = \
                self.base.OnNotificationActionTopic(
                    self.check_for_end_or_abort(e),
                    Base_pb2.NotificationOptions()
                )

        try:
            self.base.ExecuteAction(self.action)
        except (Exception,):
            print(Exception)

        finished = e.wait(TIMEOUT_DURATION)

        self.base.Unsubscribe(notification_handle)

        return finished

    def clear_faults(self):
        if self.action is not None:
            self.base.ClearFaults()

    # TODO: O robô não lida com posição internamente, isso é responsabilidade das máquinas de estado.
    def move_to_home(self):
        """
        Move robot for home position
        """
        positions_dict = read_joints_from_json()
        home = positions_dict['home']
        self.move_joints(home)  # TODO positions from json, home
        self.open_tool(0.70)

    # TODO: O robô não lida com posição internamente, isso é responsabilidade das máquinas de estado.
    def move_to_drop(self):
        """
        Move robot for home position
        """
        safety1 = read_joints_from_json()['safety 1']
        self.move_joints(safety1)  # TODO positions from json, home

    def move_joints(self, joints_list):
        """
        Set movement for robot with joints values
        Args:
            (list) joints_list: lista with values for all joints for movement

        Returns:
            (bool) move is finished
        """
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

    def move_cartesian(self, coordinates):
        action = Base_pb2.Action()
        action.name = "Example Cartesian action movement"
        action.application_data = ""

        cartesian_pose = action.reach_pose.target_pose
        cartesian_pose.x = coordinates[0]  # [meters]
        cartesian_pose.y = coordinates[1]  # [meters]
        cartesian_pose.z = coordinates[2]  # [meters]
        cartesian_pose.theta_x = coordinates[3]  # [degrees]
        cartesian_pose.theta_y = coordinates[4]  # [degrees]
        cartesian_pose.theta_z = coordinates[5]  # [degrees]

        e = threading.Event()
        notification_handle = self.base.OnNotificationActionTopic(
            self.check_for_end_or_abort(e),
            Base_pb2.NotificationOptions()
        )

        self.base.ExecuteAction(action)

        finished = e.wait(TIMEOUT_DURATION)
        self.base.Unsubscribe(notification_handle)

        if finished:
            print("Cartesian movement completed")
        else:
            print("Timeout on action notification wait")
        return finished

    def close_tool(self) -> bool:
        """
        This function closes the gripper and tries detected object
        Returns:
            (bool): object_detect: returns whether an object was detected or not detected
        """
        object_detected = False
        average = 0
        loops = 1
        current = 0
        currents = 0
        max_variation = 0.27
        while not object_detected and float(self.atribute_from_gripper()["position"]) < 95:
            gripper_command = Base_pb2.GripperCommand()
            finger = gripper_command.gripper.finger.add()
            gripper_command.mode = Base_pb2.GRIPPER_POSITION
            finger.finger_identifier = 1
            finger.value = self.__increment()
            self.base.SendGripperCommand(gripper_command)

            current = float(self.atribute_from_gripper()["current_motor"])
            if 4 > current:
                currents += current
                average = currents/loops
                loops += 1
            else:
                print("atipical current")

            if loops > 1:
                if average + max_variation < current:
                    finger.value = self.__increment()
                    self.base.SendGripperCommand(gripper_command)
                    current = float(self.atribute_from_gripper()["current_motor"])
                    if average + max_variation < current:
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

    def get_joint_angles(self):
        """
        Get joint angles from robot.
        Returns:
            (list): joint_angles: list with all joints angles
        """
        joint_angles_obj = self.base.GetMeasuredJointAngles()
        joint_angles_list = joint_angles_obj.joint_angles
        joint_angles = []
        for joint in joint_angles_list:
            joint_angles.append(joint.value)

        return joint_angles

    def get_joint_angles_vision(self):
        try:
            print("Getting Angles for every joint...")
            input_joint_angles = self.base.GetMeasuredJointAngles()
        except KServerException as ex:
            return False

        joint_angles = {}

        for joint_angle in input_joint_angles.joint_angles:
            joint_angles[f"theta_{joint_angle.joint_identifier + 1}"] = joint_angle.value

        return joint_angles

    def get_cartesian(self):
        """
        Get actual cartesian pose from robot.
        Returns:
            (list): final_pose: list with cartersian pose
        """
        pose_obj = self.base.GetMeasuredCartesianPose()
        final_pose = [pose_obj.x, pose_obj.y, pose_obj.z, pose_obj.theta_x, pose_obj.theta_y, pose_obj.theta_z]

        return final_pose

    def apply_emergency_stop(self):
        self.base.ApplyEmergencyStop()

    @staticmethod
    def get_gripper_command():
        return Base_pb2.GripperCommand()

    def atribute_from_gripper(self):
        variable = self.base_cyclic.RefreshFeedback().__str__().split()
        position = variable.index("gripper_feedback")
        information_gripper = {"position": variable[position + 7],
                               "velocity": variable[position + 9],
                               "current_motor": variable[position + 11]}

        return information_gripper

    def __increment(self):
        if float(self.atribute_from_gripper()['position']) < 70:
            return (float(self.atribute_from_gripper()["position"]) + INCREMENT[2]) / 100
        elif float(self.atribute_from_gripper()['position']) < 85:
            return (float(self.atribute_from_gripper()["position"]) + INCREMENT[1]) / 100
        else:
            return (float(self.atribute_from_gripper()["position"]) + INCREMENT[0]) / 100

    def inverse_kinematics(self, pose_list):
        # Object containing cartesian coordinates and Angle Guess
        input_joint_angles = self.base.GetMeasuredJointAngles()
        input_ik_data = Base_pb2.IKData()

        # Fill the IKData Object with the cartesian coordinates that need to be converted
        input_ik_data.cartesian_pose.x = pose_list[0]
        input_ik_data.cartesian_pose.y = pose_list[1]
        input_ik_data.cartesian_pose.z = pose_list[2]
        input_ik_data.cartesian_pose.theta_x = pose_list[3]
        input_ik_data.cartesian_pose.theta_y = pose_list[4]
        input_ik_data.cartesian_pose.theta_z = pose_list[5]

        # Fill the IKData Object with the guessed joint angles
        for joint_angle in input_joint_angles.joint_angles:
            j_angle = input_ik_data.guess.joint_angles.add()
            # '- 1' to generate an actual "guess" for current joint angles
            j_angle.value = joint_angle.value - 1

        try:
            computed_joint_angles = self.base.ComputeInverseKinematics(input_ik_data)
        except KServerException as ex:
            print("Unable to compute inverse kinematics")
            print("Error_code:{} , Sub_error_code:{} ".format(ex.get_error_code(), ex.get_error_sub_code()))
            print("Caught expected error: {}".format(ex))
            return False

        out_joint_angles = []
        for joint_angle in computed_joint_angles.joint_angles:
            out_joint_angles.append(joint_angle.value)

        return out_joint_angles
        
    # Função para mover o robô com base nos medicamentos e quantidades
    def mover_para_medicamentos(medicamento, quantidade):
        if medicamento == 'Colistimetato de sódio':
            code = 'obj.move_joints([295.18951416015625, 309.2252197265625, 116.1842041015625, 295.02618408203125, 80.2393798828125, 85.50155639648438])\nobj.move_cartesiann([0.1557641625404358, -0.44633567333221436, 0.12219314277172089, 87.29951477050781, -0.5001964569091797, 15.019988059997559])\nobj.move_cartesiann([0.20072071254253387, -0.5997055172920227, 0.12531529366970062, 88.035400390625, -0.2923136055469513, 14.742742538452148])\nobj.close_tool()\nobj.move_joints([308.3565368652344, 293.7962341308594, 114.3787841796875, 293.5994873046875, 93.23373413085938, 90.71200561523438])\nobj.move_joints([15.547500610351562, 293.7962341308594, 114.3787841796875, 293.5994873046875, 93.23373413085938, 90.71200561523438])\nobj.move_joints([5.11016845703125, 338.84356689453125, 99.62835693359375, 266.817138671875, 325.823486328125, 12.781982421875])\nobj.move_joints([5.1771087646484375, 315.9814453125, 96.06057739257812, 262.8784484863281, 345.0887756347656, 17.115264892578125])\nobj.open_tool(0.60)\n'
            for i in range(quantidade):
                # Lógica de movimento do robô para o medicamento Colistimetato de sódio
                print(f'Movimento do robô para {medicamento} - Iteração {i+1}')
        elif medicamento == 'Tigeciclina':
            code = 'obj.move_joints([295.18951416015625, 309.2252197265625, 116.1842041015625, 295.02618408203125, 80.2393798828125, 85.50155639648438])\nobj.move_cartesiann([0.1557641625404358, -0.44633567333221436, 0.12219314277172089, 87.29951477050781, -0.5001964569091797, 15.019988059997559])\nobj.move_cartesiann([0.20072071254253387, -0.5997055172920227, 0.12531529366970062, 88.035400390625, -0.2923136055469513, 14.742742538452148])\nobj.close_tool()\nobj.move_joints([308.3565368652344, 293.7962341308594, 114.3787841796875, 293.5994873046875, 93.23373413085938, 90.71200561523438])\nobj.move_joints([15.547500610351562, 293.7962341308594, 114.3787841796875, 293.5994873046875, 93.23373413085938, 90.71200561523438])\nobj.move_joints([5.11016845703125, 338.84356689453125, 99.62835693359375, 266.817138671875, 325.823486328125, 12.781982421875])\nobj.move_joints([5.1771087646484375, 315.9814453125, 96.06057739257812, 262.8784484863281, 345.0887756347656, 17.115264892578125])\nobj.open_tool(0.60)\n'
            for i in range(quantidade):
                # Lógica de movimento do robô para o medicamento Tigeciclina
                print(f'Movimento do robô para {medicamento} - Iteração {i+1}')
        elif medicamento == 'Fentanila':
            code = 'obj.move_joints([295.18951416015625, 309.2252197265625, 116.1842041015625, 295.02618408203125, 80.2393798828125, 85.50155639648438])\nobj.move_cartesiann([-0.011559383943676949, -0.42786967754364014, 0.2772851288318634, 88.28321075439453, -0.8314085602760315, 0.5609025359153748])\nobj.move_cartesiann([-0.01142274122685194, -0.6069214344024658, 0.28211238980293274, 87.37435913085938, -0.9280807971954346, 0.5559726357460022])\nobj.close_tool()\nobj.move_joints([285.50921630859375, 338.14031982421875, 135.8863525390625, 285.9048156738281, 70.42501831054688, 84.9200439453125])\nobj.move_joints([15.547500610351562, 338.14031982421875, 135.8863525390625, 285.9048156738281, 70.42501831054688, 84.9200439453125])\nobj.move_joints([5.11016845703125, 338.84356689453125, 99.62835693359375, 266.817138671875, 325.823486328125, 12.781982421875])\nobj.move_joints([5.1771087646484375, 315.9814453125, 96.06057739257812, 262.8784484863281, 345.0887756347656, 17.115264892578125])\nobj.open_tool(0.60)\n'
            for i in range(quantidade):
                # Lógica de movimento do robô para o medicamento Fentanila
                print(f'Movimento do robô para {medicamento} - Iteração {i+1}')
        else:
            print(f'Medicamento não reconhecido: {medicamento}')
