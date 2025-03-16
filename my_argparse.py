import argparse, os, sys, re

# collection of files content to be insert into respective docs
from MyVar import myclassvar

from pathlib import Path

# locate base directory of this python file
basedir = os.path.abspath(os.path.dirname(__name__))

# setup argument 
parser = argparse.ArgumentParser(description='create python flask web app and others')

# create positional and optional arguments 
parser.add_argument('foldername', metavar='foldername', nargs='?', action='store', default='myproject')
parser.add_argument('-p', '--path', dest='path', metavar='path name', action='store', default=Path(basedir).parents[0])
parser.add_argument('-a', '--app', dest='progr', metavar='app name', action='store', default='flask')

args = parser.parse_args()

# map respective parameter data into local variable
myfoldername = args.foldername
mypath = args.path
myapp = args.progr

# Flask file structure filename and foldername
toplistoffiles = ['LICENSE', 'README.md', 'config.py', ]
sublistoffiles = ['__init__.py', 'routes.py', 'db.py', 'schema.sql']
subfoldernames = ['templates', 'static']

def main():
    try:
        # filename most be alphanumeric characters, underscores and hyphen only
        if re.match(r'[A-Za-z0-9_-]+$', myfoldername):
            Path(mypath, myfoldername).mkdir()
            Path(mypath, myfoldername, 'app').mkdir()
        else:
            print('''
                not supported filename
                filename most be alphanumeric characters and underscores only
                ''')
            sys.exit(1)
    except FileExistsError as inst:
        print(inst)
        sys.exit(1)
    except TypeError as inst:
        print(inst)
        sys.exit(1)


    for i in toplistoffiles:
        
        with open(Path(mypath, myfoldername, i ), 'w') as f:
            if i == 'LICENSE':
                f.write(myclassvar.licensecontent)
            if i == 'README.md':
                f.write(myclassvar.myreadmenote)
            if i == 'config.py':
                f.write(myclassvar.flaskconfig)


    for j in subfoldernames:
        Path(Path(mypath, myfoldername, 'app', j)).mkdir()
        for k in sublistoffiles:
            with open(Path(mypath, myfoldername, 'app', k ), 'w') as f:
                if k == '__init__.py':
                    f.write(myclassvar.myinitcontent)
                if k == 'routes.py':
                    f.write(myclassvar.myroutesconfig)
                if k == 'db.py':
                    f.write(myclassvar.mydbconfig)
                if k == 'schema.sql':
                    f.write(myclassvar.dbschemasetup)
        if j == 'templates':
            with open(Path(mypath, myfoldername, 'app', j, 'index.html'), 'w') as f:
                f.write(myclassvar.myhtmlindex)
        if j == 'static':
            os.mkdir(Path(mypath, myfoldername, 'app', j, 'css'))
            with open(Path(mypath, myfoldername, 'app', j, 'css', 'main.css'), 'w') as f:
                f.write(myclassvar.mycsscontent)
            
if __name__ == '__main__':
    main()