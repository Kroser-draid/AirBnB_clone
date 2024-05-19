# AirBnB Clone Project

Welcome to the AirBnB clone project! This project aims to build a complete web application similar to AirBnB. This includes backend, frontend, and database integration.

## Description of the Project

This project is divided into multiple stages:
1. **Command Interpreter**: Create a command interpreter to manage AirBnB objects.
2. **Backend Development**: Develop a backend system to handle object storage and retrieval.
3. **Frontend Development**: Build a frontend to interact with the backend.
4. **Database Integration**: Integrate a database to store and manage data.

## Description of the Command Interpreter

The command interpreter is a shell-like tool that allows users to create, update, and manage AirBnB objects. It provides an interface to interact with the backend system.

### How to Start It

To start the command interpreter, run the following command in your terminal:

```bash
./console.py
```
## How To Use it
The command interpreter supports several commands:

1. create <class>: Creates a new instance of the specified class.

2. show <class> <id>: Retrieves an instance based on its class and id.

3. destroy <class> <id>: Deletes an instance based on its class and id.

4. all <class>: Retrieves all instances of the specified class.

5. update <class> <id> <attribute name> "<attribute value>": Updates an instance based on its class, id, and attribute.
## Examples
```bash
$ ./console.py
(hbnb) create User
(hbnb) show User 1234-5678-9012
(hbnb) destroy User 1234-5678-9012
(hbnb) all User
(hbnb) update User 1234-5678-9012 name "John Doe"
(hbnb) quit
```
## Contributors

### 2. `AUTHORS`




# This is the list of individuals who have contributed content to the repository.
```markdown
Ayoub Draid <draidayoub3@gmail.com>
Hajar <Hajar@example.com>
```
