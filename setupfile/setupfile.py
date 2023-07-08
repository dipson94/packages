from pyperclip import copy
readme=str(input("enter path to readme file : "))
name=str(input("enter name of the package : "))
version=str(input("enter version of the package : "))
description=str(input("enter short description aboout package : "))
packagedir=str(input("enter path to package directory : "))
url=str(input("enter url to github : "))
authorname=str(input("enter name of the author : "))
authoremail=str(input("enter e-mail of author : "))
license=str(input("enter the type of license : "))
print("\nenter the classifiers : ")
print("""
Example (enter each line one by one)
----------------------------------------
"License :: OSI Approved :: MIT License",
"Programming Language :: Python :: 3.10",
"Operating System :: OS Independent"
----------------------------------------
""")
classifier=[]
while True:
    x=str(input("enter classifier line :"))
    if x=="":
        break    
    classifier.append(x)
print("\nenter install_requires packages : ")
print("""
Example
----------------------------------------
bson >= 0.5.10
----------------------------------------
only add version if necessary
""")
installrequire=[]
while True:
        x=str(input("enter package :"))
        if x=="":
            break
        installrequire.append(x)
print("\nenter dev require packages : ")
print("""
Example
----------------------------------------
pytest >= 7.0
----------------------------------------
only add version if necessary
""")
extrarequire=[]
while True:
        x=str(input("enter package :"))
        if x=="":
            break
        extrarequire.append(x)
print("\nenter python version requires : ")
print("""
Example
----------------------------------------
>=3.10
----------------------------------------
only add version if necessary
""")
pythonrequires=str(input("enter version :"))
print("\nThe setup.py codes \n------------------------------------------------------------------")
s='''from setuptools import find_packages, setup

with open("'''
s=s+readme+'''", "r") as f:
    long_description = f.read()

setup(
    name="'''+name+'''",
    version="'''+version+'''",
    description="'''+description+'''",
    package_dir={"": "'''+packagedir+'''"},
    packages=find_packages(where="'''+packagedir+'''"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="'''+url+'''",
    author="'''+authorname+'''",
    author_email="'''+authoremail+'''",
    license="'''+license+'''",'''
if len(classifier)!=0:
    s=s+'''
    classifiers='''
    c='["'
    for i in classifier:
        c=c+i+'",'
    c=c[:-1]+']'
    s=s+c
if len(installrequire)!=0:
    s=s+''',
    install_requires='''
    
    ir='["'
    for i in installrequire:
        ir=ir+i+'",'
    ir=ir[:-1]+'],'
    s=s+ir
if len(extrarequire)!=0:
    s=s+''',
    extras_require={
            "dev": '''
    exr='["'
    for i in extrarequire:
        exr=exr+i+'",'
    exr=exr[:-1]+']'
    s=s+exr+''',
    },'''
if pythonrequires!="":
    s=s+'''
    python_requires="'''+pythonrequires+'''",'''
s=s+'''    
)'''
print(s)
print("------------------------------------------------------------------")
copy(s)
print("code is copied to clipboard")
