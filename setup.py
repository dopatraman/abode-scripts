import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "abode-scripts",
    version = "0.0.1",
    author = "Prakash Venkatraman",
    author_email = "prakash@asanet.com",
    description = ("Convenience scripts for Abode"),
    license = "BSD",
    url = "https://github.com/dopatraman/abode-scripts",
    long_description=read('README.md')
)