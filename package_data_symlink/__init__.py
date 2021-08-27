import sys
import os
import shutil

def greet():
    with open(os.path.join(os.path.dirname(__file__), 'data2', 'hello.txt')) as f:
        shutil.copyfileobj(f, sys.stdout)
