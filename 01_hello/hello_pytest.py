#!/usr/bin/env python
"""tests for hello.py"""

from cgitb import text
import sys
import subprocess
import os
from subprocess import run


prg = './hello.py'

def test_exists():
    """exists"""

    assert os.path.isfile(prg)

def test_runnable():
    """runs using python"""

    result = subprocess.run([sys.executable, prg], capture_output=True, text=True)
    assert result.stdout.strip() == 'Hello, World!'

def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        result = subprocess.run([sys.executable, prg, flag], check=True, capture_output=True, text=True)
        assert result.returncode == 0
        assert result.stdout.lower().startswith('usage')

def test_name():
    for flag in ['-n', '--name']:
        result = subprocess.run([sys.executable, prg, flag, 'Testing'], check=True, capture_output=True, text=True)
        assert result.returncode == 0
        assert result.stdout.strip() == 'Hello, Testing!'
