from distutils.core import setup

setup(
    name='524tool',
    version='0.1.0',
    author='Peter Lin',
    author_email='peter.tingyao@alumni.ubc.ca',
    packages=['524tool'],
    scripts=['bin/standard_dev.py','bin/square_root.py'],
    url='https://github.com/peter0083',
    license='LICENSE.txt',
    description='524 class demo for python package.',
    long_description=open('README.txt').read(),
    install_requires=[

    ],
)
