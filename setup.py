from setuptools import setup

setup(name='jiracloudinpython',
      version='0.1',
      description='Tools to access Jira Cloud using Python',
      url='https://github.com/markusmorawitz77/jiracloudinpython.git',
      author='Markus Morawitz',
      author_email='markus.morawitz@gmx.com',
      license='NONE',
      packages=['jiracloudinpython'],
      install_requires=[
          'requests'
      ],
      zip_safe=False)