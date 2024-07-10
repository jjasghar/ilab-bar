"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

# Third Party
from setuptools import setup

APP = ["ilab_bar/__main__.py"]
DATA_FILES = [
    (
        "ilab_bar",
        [
            "ilab_bar/resources/ilab.png",
            "ilab_bar/resources/on.svg",
            "ilab_bar/resources/off.svg",
        ],
    ),
]
OPTIONS = {
    "plist": {
        "LSUIElement": True,
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
    packages=["rumps>=0.4.0,<0.5.0"],
    license_file="LICENSE",
)
