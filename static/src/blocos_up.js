Blockly.Blocks['create_ticket'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Create Ticket");
    this.appendValueInput("medicamentos")
        .setCheck("Array")
        .appendField("Medicamentos");
    this.appendValueInput("nomePaciente")
        .setCheck("String")
        .appendField("Nome do Paciente");
    this.appendValueInput("doseMedicamento")
        .setCheck("String")
        .appendField("Pose do Medicamento");
    this.appendValueInput("quantidade")
        .setCheck("Number")
        .appendField("Quantidade");
    this.setOutput(true, null);
    this.setColour(230);
    this.setTooltip('');
    this.setHelpUrl('');
  }
};

Blockly.Blocks['execute_python_script'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Create database");
    this.appendValueInput("PATH FILE")
        .setCheck("String")        
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("Run a path Python script specified by the user.");
    this.setHelpUrl("");
  }
};  

Blockly.Blocks.connectToRobot = {
  init: function() {
    this.appendDummyInput()
        .appendField("Connect to robot")
        .appendField("IP:")
        .appendField(new Blockly.FieldTextInput("'192.168.2.10'"), "connection_ip");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);   
    this.setTooltip("Connect to the robot API using the default connection IP address.");
    this.setHelpUrl("");
  }
};

Blockly.Blocks.disconnectFromRobot = {
  init: function() {
    this.appendDummyInput()
        .appendField("Disconnect the robot");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);    
    this.setTooltip("Terminate the connection with the robot.");
    this.setHelpUrl("");
  }
};
 
Blockly.Blocks['move_to_home'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Move to home");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(65);
    this.setTooltip("Move the robot to its home position based on the robot type.");
  }
};


Blockly.Blocks.moveJoints = {
  init: function() {
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.appendDummyInput()
        .appendField("Move joints");
    this.appendValueInput("joints_list")
        .setCheck("Array")
        .appendField("Joints:");      
    this.setTooltip("Configure robot movement with joint values.");
    this.setColour(65);
    this.setHelpUrl("");
  }
};
  
Blockly.Blocks.moveCartesian = {
  init: function () {
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(230);
      this.appendDummyInput()
          .appendField("Move to cartesian");
      this.appendValueInput("pose_list")
          .setCheck("Array")
          .appendField("Poses [x, y, z, roll, pitch, yaw]:");
      this.setTooltip("Configure the robot movement with Cartesian coordinates.");
      this.setColour(65);
      this.setHelpUrl("");
  }
};

// Bloco 'open_tool'
Blockly.Blocks.open_tool = {
  init: function() {
    this.appendDummyInput()
        .appendField("Open tool");                        
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
    this.setTooltip("Open gripper with the specified value.");
    this.setHelpUrl("");
  }
};


Blockly.Blocks.close_tool = {
  init: function() {
    this.appendDummyInput()
        .appendField("Close tool");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("This function closes the gripper and tries to detect an object.");
 this.setHelpUrl("");
  }
};

  
Blockly.Blocks['retrieve_tickets'] = {
  init: function() {
    this.appendValueInput("retrieve_tickets")
        .setCheck(null)
        .appendField("Retrieve tickets ID");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(330);
  this.setTooltip("");
  this.setHelpUrl("");
  }
};

Blockly.Blocks['retrieve_items'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setCheck(null)
        .appendField("Retrieve items");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(330);
  this.setTooltip("");
  this.setHelpUrl("");
  }
};


Blockly.Blocks.createDatabase = {
  init: function() {
    this.appendDummyInput()
        .appendField("DBMS");
    this.appendValueInput("host")
        .setCheck("String")
        .appendField("Host:");
    this.appendValueInput("user")
        .setCheck("String")
        .appendField("User:");
    this.appendValueInput("password")
        .setCheck("String")
        .appendField("Password:");    
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("Creates a database and tables in MySQL.");
    this.setHelpUrl("");
  }
};

Blockly.Blocks.mysqlConnection = {
  init: function() {
    this.appendDummyInput()
        .appendField("Connect to MySQL database");
    this.appendValueInput("host")
        .setCheck("String")
        .appendField("Host:");
    this.appendValueInput("user")
        .setCheck("String")
        .appendField("User:");
    this.appendValueInput("password")
        .setCheck("String")
        .appendField("Password:");
    this.appendValueInput("database")
        .setCheck("String")
        .appendField("Database:");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("Connects to the MySQL database.");
    this.setHelpUrl("");
  }
};

Blockly.Blocks.gerarTickets = {
  init: function() {
    this.appendDummyInput()
        .appendField("Generate tickets");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("Generates ticket records in the pharmacy database.");
    this.setHelpUrl("");
  }
};

Blockly.Blocks.tigeciclina = {
  init: function () {
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(150);
      this.appendDummyInput()
          .appendField("Medicine - Tigeciclina");
      this.setTooltip("Configure the robot movement with Cartesian coordinates.");
      this.setHelpUrl("");
  }
};

Blockly.Blocks.fentanila = {
  init: function () {
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(150);
    this.appendDummyInput()
        .appendField("Medicine - Fentanila");
    this.setTooltip("Configure the robot movement with Cartesian coordinates.");
    this.setHelpUrl("");
  }
  };

Blockly.Blocks.colistemato = {
  init: function () {
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(150);
      this.appendDummyInput()
          .appendField("Medicine - Colistemato de Sódio");     
      this.setTooltip("Configure the robot movement with Cartesian coordinates.");
      this.setHelpUrl("");
  }
};

Blockly.Blocks.safety = {
  init: function () {
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(65);
    this.appendDummyInput()
        .appendField("Safety pose");
        this.appendValueInput("joints_list")
        .setCheck("Array")
        .appendField("Joints:");      
    this.setTooltip("Configure robot movement with joint values.");
    this.setHelpUrl("");
}
};


Blockly.Blocks['move_to_end'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Move to end of trajectory");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(65);
    this.setTooltip("Move the robot to its home position based on the robot type.");
  }
};

// Generator Stubs


// Definindo a função JavaScript gerada pelo bloco Blockly
Blockly.JavaScript['create_ticket'] = function(block) {
  var value_medicamentos = Blockly.JavaScript.valueToCode(block, 'medicamentos', Blockly.JavaScript.ORDER_ATOMIC);
  var value_nomePaciente = Blockly.JavaScript.valueToCode(block, 'nomePaciente', Blockly.JavaScript.ORDER_ATOMIC);
  var value_poseMedicamento = Blockly.JavaScript.valueToCode(block, 'poseMedicamento', Blockly.JavaScript.ORDER_ATOMIC);
  var value_quantidade = Blockly.JavaScript.valueToCode(block, 'quantidade', Blockly.JavaScript.ORDER_ATOMIC);
  
  // Código JavaScript para criar um ticket usando os dados fornecidos
  var code = `
    // Criar um ticket com os dados fornecidos
    var ticket = {
      bloco: 'create ticket',
      medicamentos: ${value_medicamentos},
      nomePaciente: ${value_nomePaciente},
      poseMedicamento: ${value_poseMedicamento},
      quantidade: ${value_quantidade}
    };

    // Retornar o ticket criado
    JSON.stringify(ticket);
  `;
  return [code, Blockly.JavaScript.ORDER_NONE];
};




// Bloco 'run_python_file'
Blockly.Python['execute_python_script'] = function(block) {
  var value_path_file = Blockly.Python.valueToCode(block, 'PATH FILE', Blockly.Python.ORDER_ATOMIC);
  var code = 'obj.execute_python_script(' + value_path_file + ')\n';
  return code;
};

// Bloco 'connectToRobot'
Blockly.Python['connectToRobot'] = function(block) {
  var text_connection_ip = block.getFieldValue('connection_ip');
  var code = 'obj.connect(' + text_connection_ip + ')\n';
  return code;
};


// Bloco 'disconnectFromRobot'
Blockly.Python['disconnectFromRobot'] = function(block) {
  var code = 'obj.disconnect()\n';
  return code;
};

// Bloco 'move_to_home'
Blockly.Python['move_to_home'] = function(block) {
  var code = 'obj.move_joints([10.291,42.895,106.288,267.739,332.335,92.869])\nobj.move_joints([8.789, 340.573, 144.698, 269.934, 71.139, 90.942])\n';
  return code;
};


  
// Bloco 'moveJoints'
Blockly.Python['moveJoints'] = function(block) {
  var value_joints_list = Blockly.Python.valueToCode(block, 'joints_list', Blockly.Python.ORDER_ATOMIC);
  var code = 'obj.move_joints(' + value_joints_list + ')\n';
  return code;
};

// Bloco 'moveCartesian'
Blockly.Python['moveCartesian'] = function(block) {
  var value_pose_list = Blockly.Python.valueToCode(block, 'pose_list', Blockly.Python.ORDER_ATOMIC);
  var code = 'obj.move_cartesiann(' + value_pose_list + ')\n';
  return code;
};

// Bloco de geração 'open_tool'
Blockly.Python['open_tool'] = function(block) {
  var value_value = Blockly.Python.valueToCode(block, 'value', Blockly.Python.ORDER_ATOMIC) || '0.60';
  var code = 'obj.open_tool(' + value_value + ')\n';
  return code;
};


// Bloco 'close_tool'
Blockly.Python['close_tool'] = function(block) {    
  var code = 'obj.close_tool()\n';
  return code;
};


// Bloco 'createDatabase'
Blockly.Python['createDatabase'] = function(block) {
    var value_host = Blockly.Python.valueToCode(block, 'host', Blockly.Python.ORDER_ATOMIC);
    var value_user = Blockly.Python.valueToCode(block, 'user', Blockly.Python.ORDER_ATOMIC);
    var value_password = Blockly.Python.valueToCode(block, 'password', Blockly.Python.ORDER_ATOMIC);
    var code = 'obj.create_database(' + value_host + ', ' + value_user + ', ' + value_password + ')\n';
    return code;
};

// Bloco 'mysqlConnection'
Blockly.Python['mysqlConnection'] = function(block) {
    var value_host = Blockly.Python.valueToCode(block, 'host', Blockly.Python.ORDER_ATOMIC);
    var value_user = Blockly.Python.valueToCode(block, 'user', Blockly.Python.ORDER_ATOMIC);
    var value_password = Blockly.Python.valueToCode(block, 'password', Blockly.Python.ORDER_ATOMIC);
    var value_database = Blockly.Python.valueToCode(block, 'database', Blockly.Python.ORDER_ATOMIC);
    var code = 'obj.mysql_connection(' + value_host + ', ' + value_user + ', ' + value_password + ', ' + value_database + ')\n';
    return code;
};

// Bloco 'gerarTickets'
Blockly.Python['gerarTickets'] = function(block) {    
    var code = 'obj.gerar_tickets()\n';
    return code;
};

 // Bloco 'retrieve_tickets'
 Blockly.Python['retrieve_tickets'] = function(block) {
  var value_retrieve_tickets = Blockly.Python.valueToCode(block, 'retrieve_tickets', Blockly.Python.ORDER_ATOMIC);
  var code = 'obj.retrieve_tickets(' + value_retrieve_tickets + ')\n';
  return code;
};

// Bloco 'retrieve_items'
Blockly.Python['retrieve_items'] = function(block) {
  var value_name = Blockly.Python.valueToCode(block, 'NAME', Blockly.Python.ORDER_ATOMIC);
  var code = 'obj.retrieve_items(' + value_name + ')\n';
  return code;
};

//blooco 'tigeciclina
Blockly.Python['tigeciclina'] = function(block) {
  var value_pose_list = Blockly.Python.valueToCode(block, 'pose_list', Blockly.Python.ORDER_ATOMIC);
  var code = 'obj.move_joints([295.18951416015625, 309.2252197265625, 116.1842041015625, 295.02618408203125, 80.2393798828125, 85.50155639648438])\nobj.move_cartesiann([0.1557641625404358, -0.44633567333221436, 0.12219314277172089, 87.29951477050781, -0.5001964569091797, 15.019988059997559])\nobj.move_cartesiann([0.20072071254253387, -0.5997055172920227, 0.12531529366970062, 88.035400390625, -0.2923136055469513, 14.742742538452148])\nobj.close_tool()\nobj.move_joints([308.3565368652344, 293.7962341308594, 114.3787841796875, 293.5994873046875, 93.23373413085938, 90.71200561523438])\nobj.move_joints([15.547500610351562, 293.7962341308594, 114.3787841796875, 293.5994873046875, 93.23373413085938, 90.71200561523438])\nobj.move_joints([5.11016845703125, 338.84356689453125, 99.62835693359375, 266.817138671875, 325.823486328125, 12.781982421875])\nobj.move_joints([5.1771087646484375, 315.9814453125, 96.06057739257812, 262.8784484863281, 345.0887756347656, 17.115264892578125])\nobj.open_tool(0.60)\n';
  return code;
};

// Bloco 'fentanila'
Blockly.Python['fentanila'] = function(block) {
  var value_pose_list = Blockly.Python.valueToCode(block, 'pose_list', Blockly.Python.ORDER_ATOMIC);
  var code = 'obj.move_joints([295.18951416015625, 309.2252197265625, 116.1842041015625, 295.02618408203125, 80.2393798828125, 85.50155639648438])\nobj.move_cartesiann([-0.011559383943676949, -0.42786967754364014, 0.2772851288318634, 88.28321075439453, -0.8314085602760315, 0.5609025359153748])\nobj.move_cartesiann([-0.01142274122685194, -0.6069214344024658, 0.28211238980293274, 87.37435913085938, -0.9280807971954346, 0.5559726357460022])\nobj.close_tool()\nobj.move_joints([285.50921630859375, 338.14031982421875, 135.8863525390625, 285.9048156738281, 70.42501831054688, 84.9200439453125])\nobj.move_joints([15.547500610351562, 338.14031982421875, 135.8863525390625, 285.9048156738281, 70.42501831054688, 84.9200439453125])\nobj.move_joints([5.11016845703125, 338.84356689453125, 99.62835693359375, 266.817138671875, 325.823486328125, 12.781982421875])\nobj.move_joints([5.1771087646484375, 315.9814453125, 96.06057739257812, 262.8784484863281, 345.0887756347656, 17.115264892578125])\nobj.open_tool(0.60)\n';
  return code;
};
// Bloco 'colistemato de sodio'
Blockly.Python['colistemato de sodio'] = function(block) {
  var value_pose_list = Blockly.Python.valueToCode(block, 'pose_list', Blockly.Python.ORDER_ATOMIC);
  var code = 'obj.move_joints([295.18951416015625, 309.2252197265625, 116.1842041015625, 295.02618408203125, 80.2393798828125, 85.50155639648438])\nobj.move_cartesiann([0.29209989309310913, -0.3715454936027527, 0.1221068799495697, 87.32437133789062, -0.294109970331192, 33.949493408203125])\nobj.move_cartesiann([0.3670244812965393, -0.5136098861694336, 0.13054290413856506, 87.66592407226562, -0.3523963987827301, 34.886573791503906])\nobj.close_tool()\nobj.move_joints([327.1998291015625, 293.797119140625, 114.38198852539062, 293.6026611328125, 93.2352294921875, 90.56344604492188])\nobj.move_joints([15.547500610351562, 293.797119140625, 114.38198852539062, 293.6026611328125, 93.2352294921875, 90.56344604492188])\nobj.move_joints([5.11016845703125, 338.84356689453125, 99.62835693359375, 266.817138671875, 325.823486328125, 12.781982421875])\nobj.move_joints([5.1771087646484375, 315.9814453125, 96.06057739257812, 262.8784484863281, 345.0887756347656, 17.115264892578125])\nobj.open_tool(0.60)\n';
  return code;
};

Blockly.Python['safety'] = function(block) {
  var value_joints_list = Blockly.Python.valueToCode(block, 'joints_list', Blockly.Python.ORDER_ATOMIC);
  var code = 'obj.move_joints(' + value_joints_list + ')\n';
  return code;
};


Blockly.Python['move_to_end'] = function(block) {
  var code = 'obj.move_joints([10.291,42.895,106.288,267.739,332.335,92.869])\n';
  return code;
};





