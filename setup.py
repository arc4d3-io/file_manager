from setuptools import setup, find_packages

setup(
    name='file_manager',
    version='0.1.3-beta',
    description='Module for file management operations.',
    author='ARC4D3',
    author_email='repo@arc4d3.com',
    packages=find_packages(),
    install_requires=[
        'logger>=0.1.0-beta',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
