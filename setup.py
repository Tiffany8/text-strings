from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()
setup(name='trw_text_string',
      version='0.0.4',
      author='T Williams',
      description='Package for a challenge.',
      long_description=readme,
      packages=find_packages())
