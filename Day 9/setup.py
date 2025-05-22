from setuptools import setup, find_packages

setup(
    name="library_system",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'library-cli = main:main',
        ],
    },
    install_requires=[],
)
