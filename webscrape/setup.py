from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="webscrape",
    version="0.0.10",
    description="An id generator that generated various types and lengths ids",
    package_dir={"": "webscrape"},
    packages=find_packages(where="webscrape"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dipson",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=['bs4','requests'],
    python_requires=">=3.10",
)
