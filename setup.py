from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()
setup(name='TextString',
      version='0.0.2',
      author='T Williams',
      author_email='tirwilliams@gmail.com',
      description='Package for a challenge.',
      long_description=readme,
      packages=find_packages())
