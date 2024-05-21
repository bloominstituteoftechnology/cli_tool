from setuptools import setup, find_packages

setup(
    name='cli_tool',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cli_tool=cli_tool.main:main',
        ],
    },
    install_requires=[],
    author='Gabriel Cabrejas',
    author_email='gabriel@cabrejas.net',
    description='A simple CLI tool.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/bloominstituteoftechnology/cli_tool',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
