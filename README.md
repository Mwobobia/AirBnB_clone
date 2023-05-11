# AirBnB_clone

![image](https://github.com/Mwobobia/AirBnB_clone/assets/111277935/115aa338-fc2b-4bf9-8732-c08f19e2ee26)

Description of the project.
This is the first phase of building a full web application "The AirBnB"

The project is linked in the following ways: put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel create the first abstracted storage engine of the project: File storage. create all unittests to validate all our classes and storage engine

In this project, we want to manage the following objects: Create a new object (ex: a new User or a new Place) Retrieve an object from a file, a database etc… Do operations on objects (count, compute stats, etc…) Update attributes of an object Destroy an object
Data (python objects) generated are stored in a json file and can be accessed with the help of the json module in python

Description of the Command interpreter.

A command interpreter is used to manipulate data without a visual interface, like a shell (for development and debugging) A website (front-end) with static and dynamic functionalities. A comprehensive database to manage the backend functionalities.
This command line interpreter serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

Some of the commands available are:

show
create
update
destroy
count
And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the folowing actions can be performed:

Creating new objects (ex: a new User or a new Place)
Retrieving an object from a file, a database etc…
Doing operations on objects (count, compute stats, etc…)
Updating attributes of an object
Destroying an object

HOW TO APPROACH IT.

You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.
 
 git clone https://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@github.com/Mwobobia/AirBnB_clone.git

After cloning the repository you will have a folder called AirBnB_clone. In here there will be several files that allow the program to work.

/console.py : The main executable of the project, the command interpreter.

models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON file to instances

models/__ init __.py: A unique FileStorage instance for the application

models/base_model.py: Class that defines all common attributes/methods for other classes.

models/user.py: User class that inherits from BaseModel

models/state.py: State class that inherits from BaseModel

models/city.py: City class that inherits from BaseModel

models/amenity.py: Amenity class that inherits from BaseModel

models/place.py: Place class that inherits from BaseModel

models/review.py: Review class that inherits from BaseModel

HOW TO USE IT.
It works with both Interactive and non-interactive modes

IN INTERACTIVE MODE, it allows a developer to interact with their application in real-time and test new features and functionality. It's an essential when working on an application like the Airbnb clone. 
The console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.
Example:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
 
NON-INTERACTIVE MODE,(Like the shell project in C) in the Airbnb console is a way of running commands in a batch or script mode, without requiring user input. This mode is useful for automating tasks, performing repetitive actions, and running complex commands that require multiple inputs.
  Create script
  Import modules
  Write commands
  Save and run the script
  View the output
In this mode no prompt will appear, and no further input will be expected from the user.
Example:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
 

  
  

