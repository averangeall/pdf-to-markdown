from setuptools import setup

setup(name='pdf_to_md',
      version='0.1.0',
      packages=[''],
      # package_dir = {'': './'},
      # scripts=['main'],
      entry_points={
          'console_scripts': [
              'pdf_to_md = main:main'
          ]
      },
      )