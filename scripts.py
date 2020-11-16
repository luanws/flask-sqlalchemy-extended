import sys
import os
import shutil
from contextlib import suppress

args = sys.argv[1:]


def clear_build():
    folders = ['build', 'dist', 'flask_sqlalchemy_extended.egg-info']
    for folder in folders:
        with suppress(FileNotFoundError):
            shutil.rmtree(folder)


scripts = {
    'build': 'python setup.py sdist bdist_wheel',
    'publish': 'twine upload dist/*',
    'clear_build': clear_build,
}

commands = []
for arg in args:
    if scripts.keys().__contains__(arg):
        commands.append(scripts[arg])

for command in commands:
    if isinstance(command, list):
        [os.system(c) for c in command]
    elif isinstance(command, str):
        os.system(command)
    elif callable(command):
        command()

if (len(args) == 0):
    print(list(scripts.keys()))
