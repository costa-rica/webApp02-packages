from setuptools import setup

setup (
    name="nr_packages",
    version = "0.1",
    author="NickRodriguez",
    author_email="nick@dashanddata.com",
    description = "weather app models and sqlalchemy objects",
    packages=['nr_config','nr_models'],
    python_requires=">=3.6",
    )