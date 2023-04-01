from setuptools import setup, find_packages

setup(
    name='HAC-API',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    url='https://github.com/Nazchanel/hac-api',
    license='Apache-2.0',
    author='Eshan Iyer',
    author_email='eshaniyer@duck.com',
    description='This is a simple API to access the Home Access Center (HAC)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)