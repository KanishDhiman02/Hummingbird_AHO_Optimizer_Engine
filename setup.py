from setuptools import setup, find_packages

setup(
    name="optimizer_engine",
    version="0.1.0",
    packages=['optimizer_engine'],
    description="A high-performance Python library for metaheuristic optimization. Features a custom visit-table mechanism to minimize redundant CPU cycles and memory overhead.",
    author="Kanish Dhiman",
    install_requires=[
        "numpy",
        "pandas",
    ],
)