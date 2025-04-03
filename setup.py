from setuptools import setup, find_packages
import os

version = "1.35"

setup(
    name="esdrt.theme",
    version=version,
    description="Installable theme: esdrt.theme",
    long_description=open("README.txt").read()
    + "\n"
    + open(os.path.join("docs", "HISTORY.txt")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="",
    author="Mikel Santamaria",
    author_email="msantamaria@bilbomatica.es",
    url="https://github.com/eea/esdrt.theme/",
    license="GPL",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["esdrt"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "z3c.jbot",
        "plone.api>=1.8.4",
        "plone.app.dexterity",
    ],
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
