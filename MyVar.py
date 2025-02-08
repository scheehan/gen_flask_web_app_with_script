class myclassvar():

    licensecontent = '''MIT License

    Copyright (c) 2025 Han, <db_scheehan@gmx.com>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    '''
    flaskconfig = '''import os

    basedir = os.path.abspath(os.path.dirname(__name__))

    class Config(object):
        SECRET_KEY = 'put your darkest secret key here'
        # DATABASE = os.path.join(basedir, 'coninfo.db')
    '''
    myreadmenote = '''# Flask web app
    '''

    myhtmlindex = '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title> - FlaskApp - </title>
        <link rel="stylesheet" href="{{url_for('static', filename='css/main.css')}}">

    </head>
    <body>
        <hr>
        <br>
        <div class="container">
        <div class="centered-content">
        <p>Flask web app</p>
        <p>{{ myposts }}</p>
        <br>
        <iframe width="420" height="315"
        src="https://youtube.com/embed/JqLqYW-zdQY?html5=1">
        </iframe>
    </div>
    </div>
    </body>
    </html>
    '''

    mycsscontent = '''.container {
            display: flex;
            justify-content: center; /* Horizontally center content */
            align-items: center; /* Vertically center content */
            height: 100vh; /* Make the container take up the full viewport height (optional) */
            width: 100vw; /* Make the container take up the full viewport width (optional) */

    }
    .centered-content {
        /* Styling for the centered content (optional) */
        background-color: #f0f0f0;
        padding: 20px;
        border-radius: 5px;
    '''

    myinitcontent = '''from flask import Flask
    from app.db import init_app
    from config import Config

    # initialize Flask app with config ref
    app = Flask(__name__)
    app.config.from_object(Config)
    init_app(app)

    from app import routes
    '''
    mydbconfig = '''import sqlite3
    import click
    from flask import current_app, g
    from flask.cli import with_appcontext


    # Connect to the database specified in the config file
    def get_db():
        if 'db' not in g:
            g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            g.db.row_factory = sqlite3.Row

        return g.db


    # Close the database
    def close_db(e=None):
        db = g.pop('db', None)

        if db is not None:
            db.close()


    # Initialise the database with setup sql schema template - this only needs to be run once
    def init_db():
        db = get_db()

        with current_app.open_resource('schema.sql') as f:
            db.executescript(f.read().decode('utf8'))


    # Create a command that can be run with flask ("flask init-db") to initialise the database
    @click.command('init-db')
    @with_appcontext
    def init_db_command():
        """Clear the existing data and create new tables"""
        init_db()
        click.echo("Initialsed the database")


    def init_app(app):
        app.teardown_appcontext(close_db)
        app.cli.add_command(init_db_command)
    '''

    myroutesconfig = """from app import app
    from flask import render_template, request, redirect, url_for

    from app.db import get_db

    @app.route('/')
    def index():
        
        # conn = get_db()
        
        # myposts = conn.execute('''
        #                       SELECT * FROM users;
        #                       ''').fetchall()
        # conn.close()
        
        myposts = 'placeholder'
        
        return render_template('index.html', myposts=myposts)
    """

    dbschemasetup = '''DROP TABLE IF EXISTS users;

    CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    ext TEXT NOT NULL,
    email TEXT
    );
    '''