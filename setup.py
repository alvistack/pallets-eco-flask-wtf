# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='flask-wtf',
    version='1.2.2',
    description='Form rendering, validation, and CSRF protection for Flask with WTForms.',
    maintainer='WTForms',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    install_requires=[
        'flask',
        'itsdangerous',
        'wtforms',
    ],
    extras_require={
        'email': [
            'email-validator',
        ],
    },
    packages=[
        'flask_wtf',
        'flask_wtf.recaptcha',
    ],
    package_dir={'': 'src'},
)
