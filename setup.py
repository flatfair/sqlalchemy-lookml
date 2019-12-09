from setuptools import setup, find_packages

VERSION = "0.0.1"

with open("requirements.txt", "r") as req:
    install_reqs = req.read().splitlines()

setup(
    name="sqlalchemy-lookml",
    version=VERSION,
    author="Marcin Szymanski",
    description="SQLAlchemy LookML Dialect",
    install_requires=install_reqs,
    include_package_data=True,
    python_requires=">= 3.7",
    packages=find_packages(),
    entry_points={
        "sqlalchemy.dialects": ["lookml=sqlalchemy_lookml.dialect:LookMLDialect"]
    },
)
