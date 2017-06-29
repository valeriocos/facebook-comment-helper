__author__ = 'valerio cosentino'

from setuptools import setup, find_packages

setup(
    name = 'facebook-comment-helper',
    version='0.1',
    description='Facebook Comment Helper',
    long_description='This tool helps community managers to find and answer relevant comments in their pages.'
                     'Currently, a relevant comment is supposed to contain a photo or a video',
    author='Valerio Cosentino',
    author_email='valerio.cosentino@gmail.com',
    packages=find_packages(include=['resource', 'helper', 'gui']),
    install_requires=['facebook-sdk', 'selenium', 'requests'],
    include_package_data=True,
    package_data={
        'resource': ['resource/chromedriver.exe'],
    },
    data_files=[('resource', ['resource/chromedriver.exe'])]
)