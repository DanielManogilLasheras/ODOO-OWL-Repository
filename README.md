# ODOO-OWL-Repository
## Guide to make ODOO Developer enviroment work
- First you download the odoo17 branch version: https://github.com/odoo/odoo.git
- Make sure you have the Python 3.12.4 version installed or the best version for the Odoo version, the latest version will result in error: https://www.python.org/downloads/release/python-3124/
- Install visual studio build tools selecting Desktop development with C++.
- Go to an IDE, and create a venv enviroment inside the Odoo folder: python -m venv venv. We can create virtual enviroments of different versions by: py -3.9 -m venv venv
- Activate the virtual enviroment: venv\Scripts\Activate.ps1
- After that install the setuptools wheel: pip install setuptools wheel
- Install the odoo requirements: pip install -r requirements.txt
- Connect to the database with the command, if it is the first time it's connecting, you must add "-i base": python odoo-bin -r dbuser -w dbpassword --addons-path=addons -d mydb
- When possible, Odoo will use the port 8069, so we will access by typing localhost:8069.
- In the development enviroment, the factory account is admin, and the password is admin.

## Setup odoo.conf and launch.json
- Use debian\odoo.conf to setup the configuration of addons and connection values.
- use a base of launch.json in this repository to setup the launch.

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


#ODOO TOOLS AND MODULES SETUP

## wkhtmlopdf tool

- This is for Windows:

First, download and install wkhtmltopdf for your version of windows (32 bit or 64 bit).
Once it's installed, go to Openerp/odoo and go to Settings> Users and click on your user
Click edit and scroll down and look for "Technical Features" is enabled / checked.
Click Apply, then log out of Odoo and then login
Go to Settings again and now you should see several new technical menu items on the left
Go to Settings -> Customization -> Parameters -> System Parameters
Click Add and for Key insert : webkit_path
For value insert: C:\Progra~1\wkhtmltopdf\bin\wkhtmltopdf.exe
Apply and exit and restart Windows.
After you do the above steps, go to System  in Control Panel.
Click on Advanced Settings. The System Properties window will pop up.
In the "Advanced" Tab, Click on "Environment Variables". 
In the "System variables", scroll down until you find the "Path" variable and double click. !!!!!NOT user variables
inside the "Variable value" field, add this to the end: ;C:\Program Files\wkhtmltopdf\bin
Click OK and then reboot your system.


#ODOO VERSIONS CONSIDERATIONS AND TIPS:

## Odoo 17 and above:

### XML tips:

- For making columns totally invisible, use : column_invisible="True"
- FORMS STRUCTURE:

          <record id="action_print_report_submittals" model="ir.actions.report">
                <field name="name">Print PDF</field>
                <field name="model">quotation.manager</field>
                <field name="report_type">qweb-pdf</field>
                <field name="report_name">quotation_manager.report_submittals</field>
                <field name="report_file">quotation_manager.report_submittals</field>
                <field name="print_report_name">(object.state in ('draft', 'sent') and 'Quotation - %s' % (object.name)) or 'Submittal- %s' % (object.name)</field>
                <field name="binding_model_id" ref="model_quotation_manager"/>
                <field name="binding_type">report</field>
        </record>
