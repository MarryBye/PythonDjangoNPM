# Python NPM

It`s a test project, which used to create a web app, with using a modern technologies like Django Framework for Backend + Typescript, SASS for frontend.

## Requirements

### Python dependencies:
1. Recommended Python 3.13.7
2. Django 5.2.7
3. Dotenv 1.2.1

### NodeJS Dependencies

1. NodeJS 11.6.1
2. Typescript 5.9.3
3. SASS 1.93.3

## To install a new project
1. Initialize npm ``npm init`` (already done in `frontend/` directory)
2. Install Typescript and SASS modules ``npm install typescript sass`` (already done in `frontend/` directory)
3. Initialize Typescript ``npx tsc --init`` (already done in `frontend/` directory)
4. Install python requirements with terminal: ``pip install -r requirements.txt``
5. Create .env file in the root directory with next secrets:
   1. ``DJANGO_KEY`` - secret key for your Django Server
   2. ``SETTINGS_FILE`` - name of the settings file, which will be used (dev, prod or default)

## Usage
All settings for TS was already done. ``frontend/package.json`` is ready-to-go! Like the ``frontend/tsconfig.json``, where is ready ``rootDir``, ``outDir``, 
``include``, ``exclude`` settings  

To build updated frontend just type: ``npm run build`` or use PyCharm and run ``NPM Build`` Task  
To run Django Server just type ``python manage.py runserver`` or use PyCharm and run ``Run Server`` Task  