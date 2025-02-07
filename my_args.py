import os, sys, re

from platform import python_version
from pathlib import Path

class MyVar

# accept 1 arguments 
args = sys.argv[1:3]

if not args:
    sys.exit(1)

if args[0] == '-f':
    if len(sys.argv) > 2:
        try:
            # filename most be alphanumeric characters and underscores only
            if re.match(r'[A-Za-z0-9_]+$', args[1]):
                Path(args[1]).mkdir()
            else:
              print('''
                    not supported filename
                    filename most be alphanumeric characters and underscores only
                    ''')
              sys.exit()
        except FileExistsError as inst:
            print(inst)
    else:
        print('''
        not supported filename
        filename most be alphanumeric characters and underscores only
        ''')
        sys.exit()