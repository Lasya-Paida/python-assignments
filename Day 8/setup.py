from setuptools import setup, find_packages

setup(
    name="library_system",
    version="0.1",
    packages=find_packages(where="."),
    py_modules=["main", "book", "user", "library"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "library-cli = main:main"
        ]
    },
    author="Your Name",
    description="A simple CLI-based Library Management System",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
