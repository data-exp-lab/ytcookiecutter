# !/usr/bin/env python

from distutils.core import setup
setup(
    name='dxlcookiecutter',
    packages=['dxlcookiecutter'],
    version='0.1.0',
    description='Cookiecutter template for a Python package',
    author='Chris Havlin',
    license='BSD',
    author_email='chavlin@illinois.edu',
    url='https://github.com/chrishavlin/dxlcookiecutter',
    keywords=['cookiecutter', 'template', 'package', ],
    python_requires='>=3.6',
    install_requires=["yt", "Click>=7.0", "PyGithub"],
    entry_points={
        'console_scripts': [
            'dxlcookiecutter=dxlcookiecutter.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
    ],
)
