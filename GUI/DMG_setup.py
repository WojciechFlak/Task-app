"""
This is a DMG_setup.py script generated by py2applet

Usage:
    python DMG_setup.py py2app
"""

from setuptools import setup

APP = ['GUI2.py']
DATA_FILES = []
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)