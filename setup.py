from setuptools import setup, find_packages

setup(name='tokenizer',
      packages=find_packages(),
      version="0.1.0",
      description='A light weight word tokenizer',
      author='Satchel Grant',
      author_email='grantsrb@gmail.com',
      url='',
      install_requires=[i.strip() for i in open("requirements.txt").readlines()],
      long_description='''
          A light weight word tokenizer.
          ''',
      classifiers=[
          'Intended Audience :: Science/Research',
          'Operating System :: MacOS :: MacOS X :: Ubuntu',
          'Topic :: Scientific/Engineering :: Information Analysis'],
      )
