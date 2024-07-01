from setuptools import setup, find_packages

setup(
    name='tlog',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'cryptography',
    ],
    author='Tanbin Hassan Bappi',
    author_email='mds.tanbin@gmaile.com',
    description='A logging library with ISO 8601 timestamp format',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/smtanbin/tlog',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
