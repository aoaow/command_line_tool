'''
Package dbtool using setuptools
'''
from setuptools import setup, find_packages

setup(
    name='dbtool',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click==8.1.3',
    ],
    entry_points='''
        [console_scripts]
        dbtool=dbtool.cli:cli
    ''',
    author='Eleanor Jiang',
    author_email='eleanor.jiang@duke.edu',
    description='A simple command-line tool to interact with a database.',
    url='https://github.com/aoaow/dbtool',
)
