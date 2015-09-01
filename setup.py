#!/usr/bin/env python3
import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='WeatherServer',
    version='0.1',
    packages=['weather_server'],
    scripts=[],
    include_package_data=True,
    license='LGPL License',  # example license
    description='A Django app to act as a weather server.',
    long_description=README,
    url='https://github.com/FullStackEmbedded/WeatherServer/',
    author='Daniel Lee',
    author_email='example@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        "Django >= 1.5",
        "pandas >= 0.13",
    ],
)
