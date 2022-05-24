from setuptools import setup
import os


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="spicy_snake",            # name of your package
    version="0.0.1",
    description="a terminal-based snake game",
    long_description=open_file("README.md"),  # only if you have a README.md
    author="Siamak and the Stationary Srirarcha cohort",
    author_email="maxmustermann@posteo.de",
    packages=["spicy_snake"],      # same as folder name
    url="https://github.com/siamakn/srirarcha_snake",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ]
)
