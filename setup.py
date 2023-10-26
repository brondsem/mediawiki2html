#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
    MediaWiki Syntax to HTML

    :copyright: (c) 2012 by Raimon Esteve.
    :license: GPLv3, see LICENSE for more details

    A simple to use python library to access convert wiki syntax
    to HTML
'''

from __future__ import unicode_literals
from __future__ import absolute_import
from setuptools import setup

__version__ = 'undefined'
exec(open('mediawiki/version.py').read())

setup(
    name='mediawiki2html',
    version=__version__,
    url='https://github.com/brondsem/mediawiki2html',
    license='GPLv3+',
    author='Raimon Esteve',
    author_email='zikzak@zikzakmedia.com',
    description='MediaWiki Syntax to HTML',
    packages=[
        'mediawiki',
        'mediawiki.wikimarkup',
        'mediawiki.doc',
    ],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'six',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

