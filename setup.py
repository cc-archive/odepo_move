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
                      'http://git.asheesh.org/?p=patched/mwclient.git;a=snapshot;h=8edac3e3c62bd78b3a47dbc59a3788f193bc16bc;sf=tgz#egg=mwclient',
                      ],
)
