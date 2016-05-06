#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tornado-uifields
--------------

Reusable UI Modules for tornado
"""
import os
import os.path
from setuptools import setup

pkg = 'tornado_uifields'
data_files = []
os.chdir(pkg)
for d in os.listdir('.'):
    if os.path.isdir(d) and '.' not in d:
        folder = '{}/{}'.format(pkg, d)
        files = ['{}/{}'.format(folder, f)
                 for f in os.listdir(d) if f.endswith('.html')]
        data_files.append((folder, files))

os.chdir('..')

setup(
    name='tornado-uifields',
    version='0.0.1',
    url='https://github.com/lixxu/tornado-uifields',
    license='BSD',
    author='Lix Xu',
    author_email='xuzenglin@gmail.com',
    description='Simple paginate support for python web frameworks',
    long_description=__doc__,
    packages=['tornado_uifields', 'tornado_uifields.semanticui'],
    # package_dir={'semanticui': 'tornado_uifields/semanticui'},
    # package_data={'semanticui': '*.html'},
    data_files=data_files,
    # include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['tornado'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ]
)
