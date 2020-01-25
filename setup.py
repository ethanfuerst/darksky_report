from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='dark_skyreport',
    version='0.0.1',
    author='ethanfuerst',
    author_email='ethanfuerst@gmail.com',
    description='Python wrapper for darksky.net API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ethanfuerst/darksky_report',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 1 - Planning"
    ],
    zip_safe=False)