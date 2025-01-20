"""
This file is for checking toml file, testing purposes only.
"""

import tomli

with open("pyproject.toml", "rb") as f:
    tomli.load(f)
