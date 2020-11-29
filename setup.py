from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()
import setuptools


setup(name='asyncbs4',
version='1.0.4',
description='Asynchronous BeautifulSoup Library.',
long_description=long_description,
long_description_content_type="text/markdown",
url='https://github.com/muntakim1/asyncBeautifulSoup',
author='Muntakimur rahaman',
author_email='muntakim1104001@gmail.com',
license='MIT',
packages=setuptools.find_packages(),
zip_safe=True,
python_requires='>=3.6',
install_requires=[
    'bs4',
    'asyncio',
    'aiohttp'
]
)