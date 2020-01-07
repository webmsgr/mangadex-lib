from setuptools import find_packages
from setuptools import setup

setup(
    name="mangadexlib",
    version="0.1",
    python_requires=">3.6",
    packages=find_packages("src"),
    install_requires=["cfscrape"],
    url="https://github.com/webmsgr/mangadex-lib",
    package_dir={"": "src"},
    author="webmsgr",
    description="Small module for getting info about manga and chapters on Mangadex",
)
