from abc import ABC
from time import sleep
import subprocess
import mysql.connector

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
        print(f'Connecting to robot with IP: {connection_ip}')
        sleep(0.001)

    def disconnect(self):
        print('Disconnecting from robot...')
        sleep(0.001)

    def check_error(self):
        print('Checking error...')
        sleep(0.001)
        if self.count >= 5:
            return False
        else:
            self.count += 1
            return True

    def clear_faults(self):
        print('Clearing faults...')
        sleep(0.001)

    def move_to_home(self):
        print('Moving to home...')
        sleep(0.001)

    def move_joints(self, joints_list):
        print(f'Moving joints from position: {joints_list[0]}, {joints_list[1]}, {joints_list[2]}, '
              f'{joints_list[3]}, {joints_list[4]}, {joints_list[5]}')
        sleep(0.001)
        return True

    def move_cartesiann(self, pose_list):
        print(f'Moving cartesian pose from position: {pose_list[0]}, {pose_list[1]}, {pose_list[2]}, {pose_list[3]}, '
              f'{pose_list[4]}, {pose_list[5]}')
        sleep(0.001)
        return True

    def move_cartesian(self, pose_list):
        print(f'Moving cartesian pose from position: {pose_list[0]}, {pose_list[1]}, {pose_list[2]}, {pose_list[3]}, '
              f'{pose_list[4]}, {pose_list[5]}')
        sleep(0.001)
        return True

    def close_tool(self):
        print(f'Closing tool')
        sleep(0.001)
        return True

    def open_tool(self, value):
        print(f'Opening tool with value: {value}')
        sleep(0.001)

    def get_joint_angles(self):
        print('Getting joint angles...')
        sleep(0.001)
        return [0, 0, 0, 0, 0, 0]

    def get_joint_angles_vision(self):
        print('Getting joint angles from vision...')
        joint_angles = {}
        for joint_angle in range(1, 7):
            joint_angles[f"theta_{joint_angle}"] = 0
        return joint_angles

    def get_cartesian(self):
        print('Getting cartesian pose...')
        sleep(0.001)
        return [0, 0, 0, 0, 0, 0]

    def apply_emergency_stop(self):
        print('Applying emergency stop...')
        sleep(0.001)

    def inverse_kinematics(self, pose_list):
        print(f'Calculating inverse kinematics from position: {pose_list[0]}, {pose_list[1]}, {pose_list[2]}, '
              f'{pose_list[3]}, {pose_list[4]}, {pose_list[5]}')
        sleep(0.001)
        return [0, 0, 0, 0, 0, 0]

    
    def create_database(self):
        try:
            # Conectar ao MySQL
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Softex2023"
            )

            cursor = conexao.cursor()

            # Remover o banco de dados caso ele exista
            cursor.execute("DROP DATABASE IF EXISTS farmacia")

            # Criar o banco de dados
            cursor.execute("CREATE DATABASE IF NOT EXISTS farmacia")

            # Selecionar o banco de dados
            cursor.execute("USE farmacia")          
            
                    # Criar a tabela 'tickets' se não existir
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tickets (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    paciente VARCHAR(255) NOT NULL,                   
                    setor_nome VARCHAR(255),
                    status_processo BOOLEAN DEFAULT FALSE
                )
            """)

            # Criar a tabela 'medicamentos' se não existir
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS medicamentos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    quantidade INT,
                    pose VARCHAR(50)
                )
            """)

            # Criar a tabela 'medicamentos_tickets' para armazenar os medicamentos associados aos tickets
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS medicamentos_tickets (
                    id_ticket INT,
                    id_medicamento INT,
                    qtd_medicamento INT,
                    pose_medicamento VARCHAR(50),
                    FOREIGN KEY (id_ticket) REFERENCES tickets(id),
                    FOREIGN KEY (id_medicamento) REFERENCES medicamentos(id)
                )
            """)

            # Commit para salvar as alterações
            conexao.commit()

            # Fechar o cursor e a conexão
            cursor.close()
            conexao.close()

            print("Banco de dados e tabelas criados com sucesso.")

        except Exception as e:
            print(f"Erro ao criar banco de dados e tabelas: {e}")

    def create_ticket(self, paciente,setor_nome):
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Softex2023",
                database="farmacia"
            )

            cursor = conexao.cursor()

            # Inserir os dados do ticket na tabela 'tickets'
            cursor.execute("""
                INSERT INTO tickets (paciente, setor_nome)
                VALUES (%s, %s)
            """, (paciente, setor_nome))

            # Commit para salvar as alterações
            conexao.commit()

            print("Ticket criado com sucesso.")

        except Exception as e:
            print(f"Erro ao criar ticket: {e}")

        finally:
            # Fechar o cursor e a conexão
            cursor.close()
            conexao.close()   
  

    def create_medicamento(self, nome, quantidade):
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Softex2023",
                database="farmacia"
            )

            cursor = conexao.cursor()

            # Valor fixo para a pose do medicamento
            pose = "ValorFixo"

            # Inserir os dados do medicamento na tabela 'medicamentos' com a pose fixa
            cursor.execute("""
                INSERT INTO medicamentos (nome, quantidade, pose)
                VALUES (%s, %s, %s)
            """, (nome, quantidade, pose))

            # Commit para salvar as alterações
            conexao.commit()

            print("Medicamento criado com sucesso.")

        except Exception as e:
            print(f"Erro ao criar medicamento: {e}")
        finally:
            # Fechar cursor e conexão
            cursor.close()
            conexao.close()
    
    

if __name__ == "__main__":
    robot = TestRobot()
    