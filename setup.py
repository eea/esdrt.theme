from setuptools import setup, find_packages
import os

version = '1.6'

setup(name='esdrt.theme',
      version=version,
      description="Installable theme: esdrt.theme",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Mikel Santamaria',
      author_email='msantamaria@bilbomatica.es',
      url='https://github.com/eea/esdrt.theme/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['esdrt'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.jbot',
          'five.grok',
          'eea.icons',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """
      )
