# setup.py

from setuptools import setup, find_packages

setup(
    name='my_minipack',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    description='A small package with a progress bar and logger.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/my_minipack',  # Replace with your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
