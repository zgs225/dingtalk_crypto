#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name='dingtalk_crypto',
    version='1.0.2',
    description='钉钉加密解密工具',
    long_description='',
    author='Yuez',
    author_email='i@yuez.me',
    url='https://github.com/zgs225/dingtalk_crypto',
    packages=['dingtalk_crypto', 'tests'],
    install_requires=['pycrypto'],
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ),
    license='MIT'
)
