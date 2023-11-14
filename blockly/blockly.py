# blockly/blocks.py
# Aqui você pode definir funções ou classes que representam blocos Blockly específicos
# e que serão usados para gerar o código Python correspondente.

from blockly.Python import Blockly

class move_to_home(Blockly.Block):
    def __init__(self):
        super(ExecuteMoveToHomeBlock, self).__init__('execute_move_to_home')
        self.append_dummy_input()
        self.append_field("Execute Move to Home")
        self.set_previous_statement(True, None)
        self.set_next_statement(True, None)
        self.set_colour(230)
        self.set_tooltip("Executes the move_to_home function in Python.")
        self.set_help_url("")

    def to_python_code(self, block):
        code = 'move_to_home()\n'
        return code

# Adicione mais blocos e classes aqui, se necessário
