"""Setup for Data Structures project."""
from setuptools import setup

setup(
    name="data-structures",
    description="Data structures written in python",
    version=0.1,
    author="Philip Werner",
    author_email="philip.r.werner@gmail.com",
    license='MIT',
    py_modules=[],
    install_requires=['ipython'],
    extras_require={'test': ['pytest', 'pytest-cov', 'tox']},
    entry_points={
        'console_scripts': []
    }
)
