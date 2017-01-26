# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

DESCRIPTION = "A SlugField for MongoEngine."

try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    LONG_DESCRIPTION = DESCRIPTION


setup(name='mongoengine-slugfield',
      version='0.0.1',
      packages=find_packages(),
      author='Malthe Jørgensen',
      author_email='malthe.jorgensen@gmail.com',
      url='https://github.com/peergradeio/mongoengine-slugfield',
      license='Public Domain',
      include_package_data=True,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      platforms=['any'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: Public Domain',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Database',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      install_requires=['mongoengine', 'blinker', 'awesome-slugify'],
      test_suite='tests',
)
