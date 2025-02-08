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
