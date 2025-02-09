# How to create flask app with python script

This article elaborate a step-by-step guide on creating a basic Flask web application using Python.  We'll cover everything from setting up your development environment to displaying your first webpage. Perfect for beginners, this guide requires no prior web development experience and will equip you with the foundational knowledge to start building your own Python web apps with Flask Web templates.


simple blog page sample from [foundation][1]

allow to create flask app with single script

create necessary flask structure and basic files to get flask web app running

what this script can and cannot do

can
- create folders and files
- insert basic content and code

cannot
- setup virtual env
- install python package

```
python -m venv .venv
```

Python "Virtual Environments" are essential tools for managing dependencies in your Python projects.  They allow you to create isolated spaces where you can install specific versions of Python packages without affecting your system-wide Python installation or other projects.  Think of it like having separate containers for each of your projects, each with its own set of tools.  This is crucial because different projects often require different (and sometimes conflicting) versions of the same library.  Without virtual environments, installing a package for one project might break another project that relies on a different version.  By using virtual environments, you ensure that your projects remain independent and avoid dependency conflicts, leading to a much cleaner and more manageable development workflow.  This also makes it easier to share your projects, as you can specify the exact dependencies needed within the environment, ensuring anyone can recreate the same setup.

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
<button popovertarget="mypopover-1" popovertargetaction="show">
      Show popover #1
    </button>
<button popovertarget="mypopover-2" popovertargetaction="show">
      Show popover #2
    </button>
<div id="mypopover-1" popover="" style="background-color:#ededed;inset: unset;position: absolute;bottom: 5px;
  right: 5px;
  margin: 0;"><blockquote>Popover content #1</blockquote></div>
<div id="mypopover-2" popover="" style="background-color:#ededed;"><blockquote>Popover content #2</blockquote></div>

<button popovertarget="my-popover">Open Popover</button>

<div popover id="my-popover">```
python -m venv .venv
```</div>


[1]: https://get.foundation/templates.html