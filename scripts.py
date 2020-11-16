import sys
import os

args = sys.argv[1:]

scripts = [
    ('build', 'python setup.py sdist bdist_wheel'),
    ('publish', 'twine upload dist/*'),
]

commands = list(map(
    lambda script: script[1],
    filter(lambda script:  args.__contains__(script[0]), scripts)
))

[os.system(command) for command in commands]
