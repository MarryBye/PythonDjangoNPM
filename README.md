# Python NPM

It`s a test project, where Python (Django Framework), NPM (TS + Sass) works together!

## To install a new project:
1. Initialize npm ``npm init`` (already done in `frontend/` directory)
2. Install Typescript and SASS modules ``npm install typescript sass`` (already done in `frontend/` directory)
3. Initialize Typescript ``npx tsc --init``

## Usage
All settings for TS was already done. ``frontend/package.json`` is ready-to-go! Like the ``frontend/tsconfig.json``, where is ready ``rootDir``, ``outDir``, 
``include``, ``exclude`` settings  

To build updated frontend just type: ``npm run build`` or use PyCharm and run ``NPM Build`` Task  
To run Django Server just type ``python manage.py runserver`` or use PyCharm and run ``Run Server`` Task  