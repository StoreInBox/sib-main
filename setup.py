#!/usr/bin/env python

from setuptools import setup, find_packages


dev_requires = [
    'ipython==4.0.0',
]

tests_requires = []

install_requires = [
    # '--process-dependency-links',
    'Django==1.8.4',
    'Unidecode==0.04.18',
    'django-model-utils==2.3.1',
    # SIB applications
    "products",
]

dependency_links = [
    'git+https://github.com/StoreInBox/sib-products.git#egg=products',
]

setup(
    name='sib-assembly',
    version='0.1.0',
    author='zymud',
    author_email='zymud@i.ua',
    url='https://github.com/StoreInBox/SIB-assembly',
    description='Part of SIB project',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=install_requires,
    dependency_links=dependency_links,
    extras_require={
        'dev': dev_requires,
        'tests': tests_requires,
    },
    # tests_require=tests_requires,
    # test_suite='nodeconductor.server.test_runner.run_tests',
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
    ],
)
