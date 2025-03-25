# ODOO-OWL-Repository
## Guide to make ODOO Developer enviroment work
- First you download the odoo7 branch version: https://github.com/odoo/odoo.git
- Make sure you have the Python 3.12.4 version installed, the latest version will result in error: https://www.python.org/downloads/release/python-3124/
- Go to an IDE, and create a venv enviroment inside the Odoo folder: python -m venv venv
- After that install the setuptools wheel: pip install setuptools wheel
- Install the odoo requirements: pip install -r requirements.txt
- Connect to the database with the command, if it is the first time it's connecting, you must add "-i base": python odoo-bin -r dbuser -w dbpassword --addons-path=addons -d mydb
- When possible, Odoo will use the port 8069, so we will access by typing localhost:8069.
- In the development enviroment, the factory account is admin, and the password is admin.

## Parts of an Odoo module
- We can see the import file init.py, and the manifest.py which contains the information about the module
      The "data" section indicates where the views are contained.
- **Views:** contains the graphic interfaces like forms, user interfaces and graphic functionalities.
- **Security:** contains which modules will be integrated in Odoo. In this configuration we can also determine how the database operates and which users can write in it.
- **Models:** It defines what database is going to be created by defining classes that ressemble objects with attributes and properties
- **Demo:** Gives extra information.
- **Controllers:** It allows us to extend the application in case we use an API

## Developing modules with Odoo

- To create a module in the Odoo enviroment, we use the commmand "python odoo-bin scaffold 'name' modules
- In order to make Odoo read a module, we need to include the folder "modules" in our connection command: python odoo-bin -r dbuser -w dbpassword --addons-path=addons,modules -d mydb
- To allow Odoo access to modules in development, we need to access the interface settings and activate the developer mode at the end of the section.
- If you want the module to be updated as you develop it, you can include the extension -u "name_module"
- You only need the base init and  manifest to make your Odoo module appear

## Constraints:

- SQL constraints: https://www.postgresql.org/docs/12/ddl-constraints.html
- Python constraints: https://www.odoo.com/documentation/18.0/developer/reference/backend/orm.html#odoo.api.constrains
