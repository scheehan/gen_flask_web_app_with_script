# How to create flask app with python script

allow to create flask app with single script

create necessary flask structure and basic files to get flask web app running

what this script can and cannot do

can
- create folders and files
- insert basic content and code

cannot
- setup virtual env
- install python package

what this repo can offer

- repo readme.md
- repo license
- flask config
- flask db
- flask templates
- flask static

what you need

clone repo

enable virtual env
install flask


    1. Install Flask: Open your terminal and run:
   pip install Flask
    
    1. Create a Project Directory: Create a new directory for your project and navigate into it:
   mkdir my_flask_app
   cd my_flask_app
    
    1. Create a Python File: Inside your project directory, create a new Python file, e.g., app.py.
    2. Write Your Flask App: Open app.py and add the following code:

from flask import Flask

app = Flask(__name__)
@app.route('/')
   def home():
       return "Hello, Flask!"
if __name__ == '__main__':
       app.run(debug=True)
    1. Run Your Flask App: In your terminal, run:
   python app.py

Your app should be running at http://127.0.0.1:5000/.

Additional Tips
    • Templates: Create an index.html file in a templates folder to render HTML.
    • Static Files: Use a static folder for CSS, JavaScript, and images.
