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
                      'http://git.asheesh.org/?p=patched/mwclient.git;a=snapshot;h=2c900730c531cecd602f42c7eb8e818a0081b8e3;sf=tgz#egg=mwclient',
                      ],
)
