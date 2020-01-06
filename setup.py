from setuptools import setup, find_packages
setup(
    name="mangadexlib",
    version="0.1",
    packages=find_packages("src"),
    install_requires=['cfscrape'],
    package_dir={'':'src'},
    author="webmsgr",
    description="Small module for getting info about manga and chapters on Mangadex"
)
