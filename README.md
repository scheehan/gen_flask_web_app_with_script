# How to create flask app with python script

![my_intro](/images/web_app_generator.png)

Need a Flask project spun up fast?  Like, "I need it yesterday" fast? within minute? Forget boilerplate headaches and wrestling with Flask project structure. This Flask web app generator might just be your new best friend. 
Get up and running in minutes, and still have complete control. 
Intrigued?  You should be. 

Instead of manually setting up the basic project structure, creating files, and installing core dependencies, a generator automates these repetitive tasks.  

It typically provides a pre-configured template or skeleton project that includes:

**Basic file structure**: This includes essential files like app.py (or __init__.py for larger projects), templates directories, static files directories (for CSS, JavaScript, images), and potentially a tests directory.

**Essential dependencies**: The generator often pre-installs core Flask packages and other commonly used libraries, like those for database interaction, form handling, or user authentication.

**Configuration files**: It might set up basic configuration files for database connections, secret keys, or other project-specific settings.
Example code: A generator usually provides a simple "Hello, World" example or a more complex demo application to illustrate the basic functionality and structure.

Using a Flask web app generator significantly speeds up the initial development process, allowing developers to focus on the core logic of their application rather than spending time on boilerplate setup.  It also promotes consistency across projects by providing a standardized starting point. While generators are great for getting started quickly, it's still important to understand the underlying structure and configuration they create to effectively customize and extend your Flask applications.

This article elaborate a step-by-step guide on creating a basic Flask web application using Python, covering everything from setting up your development environment to running your first webpage default with a simple blog web site template.
Perfect for beginners, this guide requires no prior web development experience and will equip you with the foundational knowledge to start building your own Python web apps with Flask Web framework.

This Flask web app generator is a [command-line tool][2] with the goal to quickly bootstrap the creation of new Flask projects.  

## Generator accepted arguments

```python
> python3 my_argparse.py <foldername> -p <path> -a <app>

*** give a foldername; positional argument. accept alphanumeric characters, hyphen and underscores symbols only 
** path to create flask files structure; optional argument with default value parent directory
* app file structure to be generate; optional argument with default value "flask", for future usage.
```

## Basic file structure layout

What you will get once ran the script.

```python
/home/user/Projects/file-structure
├── app/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── routes.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── css/
│           └── main.css
│
├── config.py
├── LICENSE
└── README.md
```

## Output of file structure after script ran 

![my_intro](/images/list_re.png)

<img src="/images/mac_output2.gif" alt="mac output" width="600" height="400">


Simple blog page sample from [foundation][1]

![my_intro](/images/blog_page.png)

---

 ## Installation steps

### clone repo

```html
git clone https://
cd 
```

### enable virtual env

By using virtual environments, you ensure that your projects remain independent and avoid dependency conflicts, leading to a much cleaner and more manageable development workflow. 
This also makes it easier to share your projects, as you can specify the exact dependencies needed within the environment, ensuring anyone can recreate the same setup.

```python
> python -m venv .venv

Linux | MacOS 
> python3 -m venv \<path\>  
> source \<path\>/bin/activate

Windows
> py -m venv \<path\>  
> \<DIR\>\Scripts\activate
```

### install dependencies

```python
python3 -m pip install -r requirements.txt
```

### Run flask app

    flask run --debug

Your app should be running at http://127.0.0.1:5000/.

Additional Tips  
    • Templates: Create an index.html file in a templates folder to render HTML.  
    • Static Files: Use a static folder for CSS, JavaScript, and images.


[1]: https://get.foundation/templates.html
[2]: https://docs.python.org/3/library/argparse.html