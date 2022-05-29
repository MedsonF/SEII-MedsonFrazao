#!/usr/bin/python3

import subprocess

echo_data = subprocess.call ("echo 'hello world'", shell=True)

subprocess.call (["ls", "/usr/", "-la"])