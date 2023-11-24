Blockly.Blocks['run_python_file'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Run Python file");
    this.appendValueInput("PATH FILE")
        .setCheck("String")
        .appendField("Path file");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("Run a Python file specified by the user.");
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
    this.setColour(230);
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
    this.setColour(230);
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
      this.setTooltip("Move the robot to its home position based on the robot type.");
    }
  };
  
  Blockly.Blocks.moveJoints = {
    init: function() {
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.appendDummyInput()
          .appendField("Move Joints");
      this.appendValueInput("joints_list")
          .setCheck("Array")
          .appendField("Joints:");      
      this.setTooltip("Configure robot movement with joint values.");
      this.setHelpUrl("");
    }
  };
  
  Blockly.Blocks.moveCartesian = {
    init: function () {
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.appendDummyInput()
            .appendField("Move to Cartesian");
        this.appendValueInput("pose_list")
            .setCheck("Array")
            .appendField("Poses [x, y, z, roll, pitch, yaw]:");
        this.setTooltip("Configure the robot movement with Cartesian coordinates.");
        this.setHelpUrl("");
    }
};

Blockly.Blocks.open_tool = {
  init: function() {
    this.appendDummyInput()
        .appendField("Open tool with value");
    this.appendValueInput("value")
        .setCheck("Number")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField("value");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
    this.setTooltip("Open gripper with the specified value.");
    this.setHelpUrl("");
  }
};


Blockly.Blocks.close_tool = {
  init: function() {
    this.appendDummyInput()
        .appendField("close tool");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("This function closes the gripper and tries to detect an object.");
 this.setHelpUrl("");
  }
};

  
  Blockly.Blocks['retrieve_tickets'] = {
    init: function() {
      this.appendValueInput("retrieve_tickets")
          .setCheck(null)
          .appendField("retrieve tickets ID");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

  Blockly.Blocks['retrieve_items'] = {
    init: function() {
      this.appendValueInput("NAME")
          .setCheck(null)
          .appendField("retrieve items");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(230);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };
  
  
  Blockly.Blocks.createDatabase = {
    init: function() {
      this.appendDummyInput()
          .appendField("Connected to DBMS");
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
          .appendField("Usuário:");
      this.appendValueInput("password")
          .setCheck("String")
          .appendField("Senha:");
      this.appendValueInput("database")
          .setCheck("String")
          .appendField("Banco de Dados:");
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
          .appendField("Generate Tickets");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(230);
      this.setTooltip("Generates ticket records in the pharmacy database.");
      this.setHelpUrl("");
    }
  };

  Blockly.Blocks.colistemato = {
    init: function () {
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.appendDummyInput()
            .appendField("Colistemato de sódio");
        this.appendValueInput("pose_list")
            .setCheck("Array")
            .appendField("Poses [x, y, z, roll, pitch, yaw]:");
        this.setTooltip("Configure the robot movement with Cartesian coordinates.");
        this.setHelpUrl("");
    }
};

Blockly.Blocks.fentanila = {
  init: function () {
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(230);
      this.appendDummyInput()
          .appendField("Fentanila");
      this.appendValueInput("pose_list")
          .setCheck("Array")
          .appendField("Poses [x, y, z, roll, pitch, yaw]:");
      this.setTooltip("Configure the robot movement with Cartesian coordinates.");
      this.setHelpUrl("");
  }
};

Blockly.Blocks.tigeciclina = {
  init: function () {
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(230);
      this.appendDummyInput()
          .appendField("Tigeciclina");
      this.appendValueInput("pose_list")
          .setCheck("Array")
          .appendField("Poses [x, y, z, roll, pitch, yaw]:");
      this.setTooltip("Configure the robot movement with Cartesian coordinates.");
      this.setHelpUrl("");
  }
};

// Generator Stubs

// Bloco 'run_python_file'
Blockly.Python['run_python_file'] = function(block) {
  var value_path_file = Blockly.Python.valueToCode(block, 'PATH FILE', Blockly.Python.ORDER_ATOMIC);
  var code = 'obj.run_python_file(' + value_path_file + ')\n';
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
  var code = 'obj.move_to_home()\n';


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
  var code = 'obj.move_cartesian(' + value_pose_list + ')\n';
  return code;
};


// Bloco 'open_tool'
Blockly.Python['open_tool'] = function(block) {
  var value_value = Blockly.Python.valueToCode(block, 'value', Blockly.Python.ORDER_ATOMIC);
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

// Bloco 'colistemato de sodio'
Blockly.Python['colistemato'] = function(block) {
  var value_pose_list = Blockly.Python.valueToCode(block, 'pose_list', Blockly.Python.ORDER_ATOMIC);
  var code = 'obj.move_cartesian(' + value_pose_list + ')\n';
  return code;
};

// Bloco 'fentanila'
Blockly.Python['fentanila'] = function(block) {
  var value_pose_list = Blockly.Python.valueToCode(block, 'pose_list', Blockly.Python.ORDER_ATOMIC);
  var code = 'obj.move_cartesian(' + value_pose_list + ')\n';
  return code;
};

// Bloco 'tigeciclina'
Blockly.Python['tigeciclina'] = function(block) {
  var value_pose_list = Blockly.Python.valueToCode(block, 'pose_list', Blockly.Python.ORDER_ATOMIC);
  var code = 'obj.move_cartesian(' + value_pose_list + ')\n';
  return code;
};


