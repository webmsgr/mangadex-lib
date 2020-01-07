from setuptools import find_packages
from setuptools import setup

setup(
    name="mangadexlib",
    version="0.1",
    python_requires=">3.6",
    packages=find_packages("src"),
    install_requires=["cfscrape"],
    extras_require={
        'mangasync':  ["numpy"]
    },
    url="https://github.com/webmsgr/mangadex-lib",
    package_dir={"": "src"},
    description="Various Mangadex tools",
)
