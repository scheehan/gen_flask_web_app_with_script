import argparse
import os, sys, re
from MyVar import myclassvar

from platform import python_version
from pathlib import Path

basedir = os.path.abspath(os.path.dirname(__name__))

parser = argparse.ArgumentParser(description='create python flask web app and others')
parser.add_argument('-p', '--path', dest='path', metavar='path name', action='store', default=Path(basedir).parents[0])
parser.add_argument(dest='foldername', metavar='foldername', nargs='?', action='store')
parser.add_argument('-a', '--app', metavar='app name', dest='progr', action='store', default='flask')

args = parser.parse_args()
myfoldername = args.foldername
mypath = args.path

toplistoffiles = ['LICENSE', 'README.md', 'config.py', ]
sublistoffiles = ['__init__.py', 'routes.py', 'db.py', 'schema.sql']
subfoldernames = ['templates', 'static']

def main():
    try:
        # filename most be alphanumeric characters and underscores only
        if re.match(r'[A-Za-z0-9_-]+$', myfoldername):
            Path(mypath, myfoldername).mkdir()
            Path(os.path.join(basedir, myfoldername, 'app')).mkdir()
        else:
            print('''
                not supported filename
                filename most be alphanumeric characters and underscores only
                ''')
            sys.exit(1)
    except FileExistsError as inst:
        print(inst)
        sys.exit(1)


    for i in toplistoffiles:
        
        with open(os.path.join(basedir, myfoldername, i ), 'w') as f:
            if i == 'LICENSE':
                f.write(myclassvar.licensecontent)
            if i == 'README.md':
                f.write(myclassvar.myreadmenote)
            if i == 'config.py':
                f.write(myclassvar.flaskconfig)


    for j in subfoldernames:
        Path(os.path.join(basedir, myfoldername, 'app', j)).mkdir()
        for k in sublistoffiles:
            with open(os.path.join(basedir, myfoldername, 'app', k ), 'w') as f:
                if k == '__init__.py':
                    f.write(myclassvar.myinitcontent)
                if k == 'routes.py':
                    f.write(myclassvar.myroutesconfig)
                if k == 'db.py':
                    f.write(myclassvar.mydbconfig)
                if k == 'schema.sql':
                    f.write(myclassvar.dbschemasetup)
        if j == 'templates':
            with open(os.path.join(basedir, myfoldername, 'app', j, 'index.html'), 'w') as f:
                f.write(myclassvar.myhtmlindex)
        if j == 'static':
            os.mkdir(os.path.join(basedir, myfoldername, 'app', j, 'css'))
            with open(os.path.join(basedir, myfoldername, 'app', j, 'css', 'main.css'), 'w') as f:
                f.write(myclassvar.mycsscontent)
            
if __name__ == '__main__':
    main()