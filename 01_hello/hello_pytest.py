#!/usr/bin/env python3
"""tests for hello.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './hello.py'

def test_exists():
    """exists"""

    assert os.path.isfile(prg)

def test_runnable():
    """runs using python"""

    out = getoutput(f'python {prg}')
    assert out.strip() == 'Hello, World!'