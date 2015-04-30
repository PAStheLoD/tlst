from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tlst',
    version='0.1.0dev1',
    description='A simple TLS/SSL, X.509 toolkit.',
    url='https://github.com/PAStheLoD/tlst',
    author='pas',
    author_email='pasthelod@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4'
    ],

    keywords='tls ssl x509',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=['pyopenssl', 'Click'],

    entry_points={
        'console_scripts': [
            'tlst=tlst.tlst:main',
        ],
    }
)
