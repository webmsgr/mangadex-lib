from setuptools import find_packages
from setuptools import setup

setup(
    name="mangadexlib",
    version="0.2.1",
    python_requires=">=3.6",
    author="webmsgr",
    author_email="zapcontact000@gmail.com",
    packages=find_packages("src"),
    install_requires=["cfscrape"],
    extras_require={"mangasync": ["numpy"]},
    entry_points={
        "console_scripts": ["mangasync = mangasync:main [mangasync]"]
    },
    url="https://github.com/webmsgr/mangadex-lib",
    package_dir={"": "src"},
    description="Various Mangadex tools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
