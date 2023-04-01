from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    url='https://your_package_url.com',
    license='',
    author='Your Name',
    author_email='your_email@domain.com',
    description='A short description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)