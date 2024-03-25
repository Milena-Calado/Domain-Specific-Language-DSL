from abc import ABC
from time import sleep
import subprocess
import mysql.connector
import tkinter as tk
from tkinter import messagebox

from abstract_robot import AbstractRobot


class TestRobot(AbstractRobot, ABC):
    """
    This class is used to test the robot_api without the need of a real robot. It is used to test the robot_api
    functionality and to develop the robot_api without the need of a real robot. This class is used in the state machine
    class to test the state machine functionality without the need of a real robot.

    This class implements basic methods of the AbstractRobot class.
    """

    def __init__(self):
        super().__init__()
        self.count = 0

    def execute_python_script(self, file_path):
        try:
            subprocess.run(["python", file_path], check=True)
            print(f"Python file '{file_path}' executed successfully.")
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while executing the script: {str(e)}")

    def connect(self, connection_ip: str = "192.168.2.10"):
        print("using Test Robot")
        print(f"Connecting to robot with IP: {connection_ip}")
        sleep(0.001)

    def disconnect(self):
        print("Disconnecting from robot...")
        sleep(0.001)

    def check_error(self):
        print("Checking error...")
        sleep(0.001)
        if self.count >= 5:
            return False
        else:
            self.count += 1
            return True

    def clear_faults(self):
        print("Clearing faults...")
        sleep(0.001)

    def move_to_home(self):
        print("Moving to home...")
        sleep(0.001)

    def move_joints(self, joints_list):
        print(
            f"Moving joints from position: {joints_list[0]}, {joints_list[1]}, {joints_list[2]}, "
            f"{joints_list[3]}, {joints_list[4]}, {joints_list[5]}"
        )
        sleep(0.001)
        return True

    def move_cartesiann(self, pose_list):
        print(
            f"Moving cartesian pose from position: {pose_list[0]}, {pose_list[1]}, {pose_list[2]}, {pose_list[3]}, "
            f"{pose_list[4]}, {pose_list[5]}"
        )
        sleep(0.001)
        return True

    def move_cartesian(self, pose_list):
        print(
            f"Moving cartesian pose from position: {pose_list[0]}, {pose_list[1]}, {pose_list[2]}, {pose_list[3]}, "
            f"{pose_list[4]}, {pose_list[5]}"
        )
        sleep(0.001)
        return True

    def close_tool(self):
        print(f"Closing tool")
        sleep(0.001)
        return True

    def open_tool(self, value):
        print(f"Opening tool with value: {value}")
        sleep(0.001)

    def get_joint_angles(self):
        print("Getting joint angles...")
        sleep(0.001)
        return [0, 0, 0, 0, 0, 0]

    def get_joint_angles_vision(self):
        print("Getting joint angles from vision...")
        joint_angles = {}
        for joint_angle in range(1, 7):
            joint_angles[f"theta_{joint_angle}"] = 0
        return joint_angles

    def get_cartesian(self):
        print("Getting cartesian pose...")
        sleep(0.001)
        return [0, 0, 0, 0, 0, 0]

    def apply_emergency_stop(self):
        print("Applying emergency stop...")
        sleep(0.001)

    def inverse_kinematics(self, pose_list):
        print(
            f"Calculating inverse kinematics from position: {pose_list[0]}, {pose_list[1]}, {pose_list[2]}, "
            f"{pose_list[3]}, {pose_list[4]}, {pose_list[5]}"
        )
        sleep(0.001)
        return [0, 0, 0, 0, 0, 0]

    def alerta_operacao_terminou(self):
        root = tk.Tk()
        root.withdraw()

        messagebox.showinfo("Attention", "The operation is over.")

    def read_tickets(path_file, save_var_name):
        """
        Reads tickets from a file and stores them in a list.

        Args:
        - path_file (str): The path to the file containing the tickets.
        - save_var_name (list): The variable name to store the tickets.

        Returns:
        - None
        """
        save_var_name = []  # Inicializa a lista vazia para armazenar os tickets
        with open(path_file, "r") as f:
            for line in f:
                save_var_name.append(line.strip())

    def read_medicines(self, medicamentos_tickets):
        medicines = []
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Softex2023",
                database="farmacia",
            )

            cursor = conexao.cursor()

            for medicine in medicines:
                cursor.execute(
                    "SELECT id_medicamento, quantidade FROM itens_ticket WHERE id_ticket = %s",
                    (medicamentos_tickets["id_ticket"],),
                )
                itens = cursor.fetchall()
                for item in itens:
                    medicines.append({"id_medicamento": item[0], "quantidade": item[1]})
            print("Medicamenteos", medicines)

            return medicines

        except mysql.connector.Error as err:
            print("Erro ao acessar o banco de dados:", err)

        finally:
            if "conexao" in locals() and conexao.is_connected():
                cursor.close()
                conexao.close()

    def create_ticket(self, paciente, setor_nome):
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Softex2023",
                database="farmacia",
            )

            cursor = conexao.cursor()

            # Inserir os dados do ticket na tabela 'tickets'
            cursor.execute(
                """
                INSERT INTO tickets (paciente, setor_nome)
                VALUES (%s, %s)
            """,
                (paciente, setor_nome),
            )

            # Capturar o ID do último ticket inserido
            ticket_id = cursor.lastrowid

            # Commit para salvar as alterações
            conexao.commit()

            print("Ticket criado com sucesso.")

            # Retornar o ID do ticket
            return ticket_id

        except Exception as e:
            print(f"Erro ao criar ticket: {e}")
            return None

        finally:
            # Fechar o cursor e a conexão
            cursor.close()
            conexao.close()

    def create_medicamento(self, nome, quantidade, pose):
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Softex2023",
                database="farmacia",
            )

            cursor = conexao.cursor()

            cursor.execute(
                """
                INSERT INTO medicamentos (nome, quantidade, pose)
                VALUES (%s, %s, %s)
            """,
                (nome, quantidade, pose),
            )

            # Commit para salvar as alterações
            conexao.commit()

            print("Medicamento criado com sucesso.")

        except Exception as e:
            print(f"Erro ao criar medicamento: {e}")
        finally:
            # Fechar cursor e conexão
            cursor.close()
            conexao.close()

    def addMedicines(self, id_ticket, nome, quantidade):
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Softex2023",
                database="farmacia",
            )

            cursor = conexao.cursor()

            # Buscar informações do medicamento
            cursor.execute(
                """
                SELECT id, pose, quantidade FROM medicamentos WHERE nome = %s
            """,
                (nome,),
            )
            medicamento_info = (
                cursor.fetchone()
            )  # Recupera a primeira linha do resultado

            # Verificar se o medicamento foi encontrado
            if medicamento_info:
                id_medicamento = medicamento_info[0]
                pose = medicamento_info[1]
                estoque_atual = medicamento_info[2]

                if estoque_atual < quantidade:
                    raise ValueError("Quantidade insuficiente em estoque.")

                # Subtrair a quantidade do estoque
                novo_estoque = estoque_atual - quantidade
                cursor.execute(
                    """
                    UPDATE medicamentos SET quantidade = %s WHERE id = %s
                """,
                    (novo_estoque, id_medicamento),
                )

                # Buscar informações do ticket com base no ID fornecido
                cursor.execute(
                    """
                    SELECT paciente, setor_nome, status_processo FROM tickets WHERE id = %s
                """,
                    (id_ticket,),
                )
                ticket_info = cursor.fetchone()

                # Verificar se o ticket foi encontrado
                if ticket_info:
                    paciente = ticket_info[0]
                    setor_nome = ticket_info[1]
                    status_processo = ticket_info[2]

                    # Inserir a associação entre o ticket e o medicamento na tabela 'medicamentos_tickets'
                    cursor.execute(
                        """
                        INSERT INTO medicamentos_tickets (id_ticket, paciente, setor_nome, id_medicamento, nome, quantidade, pose, status_processo)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                        (
                            id_ticket,
                            paciente,
                            setor_nome,
                            id_medicamento,
                            nome,
                            quantidade,
                            pose,
                            status_processo,
                        ),
                    )

                    # Commit para salvar as alterações
                    conexao.commit()

                    print("Medicamento adicionado ao ticket com sucesso.")
                else:
                    print("Ticket não encontrado.")
            else:
                print("Medicamento não encontrado.")

        except Exception as e:
            print(f"Erro ao adicionar medicamento ao ticket: {e}")
        finally:
            # Fechar cursor e conexão
            cursor.close()
            conexao.close()


if __name__ == "__main__":
    robot = TestRobot()
