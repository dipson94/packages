"""
Template-----------------------------------------------------------------------
pip install git+https://github.com/username/repo.git@branch#subdirectory=folder
-------------------------------------------------------------------------------
"""
from pyperclip import copy
def pip_code():
    split=str(input("enter url to package : ")).split("/")
    user=split[3]
    repo=split[4]
    branch=split[6]
    folder="/".join(split[7:])
    i="pip install git+https://github.com/"+user+"/"+repo+".git@"+branch+"#subdirectory="+folder
    copy(i)
    print("---> ",i)
    print("Also copied to clipboard")
