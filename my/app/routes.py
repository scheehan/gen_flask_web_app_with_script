from app import app
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
    