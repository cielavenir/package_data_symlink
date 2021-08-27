import sys
import os
import shutil

def greetfile():
    with open(os.path.join(os.path.dirname(__file__), 'file2.txt')) as f:
        shutil.copyfileobj(f, sys.stdout)

def greetdir():
    with open(os.path.join(os.path.dirname(__file__), 'data2', 'hello.txt')) as f:
        shutil.copyfileobj(f, sys.stdout)
