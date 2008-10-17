from setuptools import setup, find_packages

setup(
    name='odepo_move',
    version="0.0",
    description='',
    author='Asheesh Laroia',
    author_email='asheesh@creativecommons.org',
    url='',
    install_requires=['setuptools',
                      'mwclient',
                      ],

    dependency_links=[
                      'http://git.asheesh.org/?p=patched/mwclient.git;a=snapshot;h=24326c561c2596eb9bff09b53ad7fdce65ad5305;sf=tgz#egg=mwclient',
                      ],
)
