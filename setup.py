# @Time    : 2022/9/15 14:08
# @Author  : tk
# @FileName: setup.py

import os
import sys

from distutils.core import setup
from setuptools import find_packages


# List of runtime dependencies required by this built package
install_requires = []

install_requires += ['protobuf']

# read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'),mode='r',encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='data_serialize',
    version='0.3.0',
    description='data serialize',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='ssbuild',
    author_email='9727464@qq.com',
    url='https://github.com/ssbuild/fastdatasets',
    packages=find_packages(),
    license='MIT',
    install_requires=install_requires,
    keywords=['data_serialize','serialize','deserialize'],
    include_package_data=True,
    package_data={'': ['*.pyd','*.dll','*.so','*.h','*.c','*.proto']},
)