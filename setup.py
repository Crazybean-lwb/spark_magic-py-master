#!/usr/bin/env python
from spark_magic import __version__
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Work around mbcs bug in distutils for py3k.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    func = lambda name, enc = ascii: {True: enc}.get(name == 'mbcs')
    codecs.register(func)

with open('README.md') as f:
    long_description = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='spark_magic',
    version=__version__,
    description='user define a pyspark magic',
    long_description=long_description,
    url='https://github.com/liuweibin6566396837/spark_magic-py-master',
    install_requires=[
        'findspark>=1.3.0',
    ],
    author='Crazybean',
    author_email='lwbxidian@163.com',
    keywords=['pyspark', 'magic'],
    license=license,
    packages=['spark_magic'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ]
)
