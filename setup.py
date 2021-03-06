#!/usr/bin/env python

"""Installs cram."""

import os
import sys

import setuptools


class test(setuptools.Command):

    """Runs doctests and Cram tests."""
    description = 'run test suite'
    user_options = [('coverage', None, 'run tests using coverage.py')]

    def initialize_options(self):
        self.coverage = 0

    def finalize_options(self):
        pass

    def run(self):
        import doctest
        import cram
        failures, tests = doctest.testmod(cram)
        sys.stdout.write('doctests: %s/%s passed\n' %
                         (tests - failures, tests))
        os.environ['PYTHON'] = sys.executable
        if self.coverage:
            # Note that when coverage.py is run, it uses the version
            # of Python it was installed with, NOT the version
            # setup.py was run with.
            os.environ['COVERAGE'] = '1'
            os.environ['COVERAGE_FILE'] = os.path.abspath('./.coverage')
        cram.main(['-v', 'tests'])


def long_description():
    """Get the long description from the README."""
    with open(os.path.join(sys.path[0], 'README.rst')) as readme:
        return readme.read()

setuptools.setup(
    author='Brodie Rao',
    author_email='brodie@bitheap.org',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Unix Shell',
        'Topic :: Software Development :: Testing',
    ],
    cmdclass={'test': test},
    description='A simple testing framework for command line applications',
    keywords='automatic functional test framework',
    license='GNU GPL',
    long_description=long_description(),
    name='cram',
    py_modules=['cram'],
    entry_points={
        'console_scripts': ['cram = cram:run_main']},
    url='http://bitheap.org/cram/',
    version='0.5',
)
