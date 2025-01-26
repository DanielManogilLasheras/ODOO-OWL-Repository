# OWL-Repository
## +About OWL and Odoo
* -OWL is the underlying component system Odoo is based on. *
* -Odoo is a user interface component framework. *
* -OWL is a custom made framework for Odoo. *
        -- It creates the components as classes instead of functions.
        -- Uses XML documents as templates to modify and store tem
        -- It uses hooks to implement additional features and functionalities.
        -- It follows a descriptive way of programming, and applies in real time modifications as it interprets the componets


## +How to create an OWL project using VITE:
* -Install vite if it wasn't installed: 
        npm create vite@latest 

* -Set up the Vite project: 
    -- ✔ Project name: … owl-vite-project
    -- ✔ Select a framework: › vanilla
    -- ✔ Select a variant: › JavaScript 

* -Navigate to the OWL directory: 

* -Install OWL:  
        npm install @odoo/owl

* -Set up Vite configuration:
        --Edit the vite.config.js to open the app in the browser automatically every time the server starts. If vite.config.js it does not exist, create it at the root of your project: *

        import { defineConfig } from 'vite';
        export default defineConfig({
            server: {
                open: true
            }
        });

* You are ready to create your components:
    In your src directory, create a file main.js to initialize and mount your Owl components. For example:
        import { Component, mount, useState, xml } from '@odoo/owl';
        class Counter extends Component {
        static template = xml`
            <button t-on-click="() => state.value += props.increment">
            Click Me! [<t t-esc="state.value"/>]
            </button>`;

        state = useState({ value: 0 });
        }

        class Root extends Component {
        static template = xml`
            <span>Hello Owl</span>
            <Counter increment="2"/>`;

        static components = { Counter };
        }
        mount(Root, document.body);
