from setuptools import setup, find_packages
setup(
    name="mangadexlib",
    version="0.1",
    packages=find_packages(),
    install_requires=['cfscrape'],
    author="webmsgr",
    description="Small module for getting info about manga and chapters on Mangadex"
)
