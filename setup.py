#!/usr/bin/env python3
import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open('README.md')) as readme:
    README = readme.read()

setup(
    name='WeatherServer',
    version='0.1',
    packages=['weather_server'],
    scripts=[],
    include_package_data=True,
    license='GPL License',  # example license
    description=("A webserver application for Full Stack Embedded's reference "
                 "weather station."),
    long_description=README,
    url='https://github.com/FullStackEmbedded/WeatherServer/',
    # Apparently PyPI doesn't allow multiple authors, which is disappointing
    author='Daniel Lee',
    author_email='lee@isi-solutions.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        "Django >= 1.5",
    ],
)
