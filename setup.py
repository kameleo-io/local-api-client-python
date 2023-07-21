import setuptools
from distutils.util import convert_path

VERSION = '1.0.0'
exec(open(convert_path('kameleo/local_api_client/_version.py')).read())

setuptools.setup(
    name='kameleo.local_api_client',
    version=VERSION,
    author='Kameleo Team',
    author_email='support@kameleo.io',
    description='This Python package provides convenient access to the Local API REST interface of the Kameleo Client.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kameleo-io/local-api-client-python',
    packages=setuptools.find_packages(),
    setup_requires=['wheel'],
    install_requires=['msrest'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
 )
