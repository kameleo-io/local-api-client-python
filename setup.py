import setuptools
from distutils.util import convert_path

with open("README.md", "r") as fh:
    long_description = fh.read()

# Version parsing
main_ns = {}
ver_path = convert_path('kameleo/local_api_client/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)


setuptools.setup(
    name='kameleo.local_api_client',
    version=main_ns['VERSION'],
    author='Kameleo Team',
    author_email='support@kameleo.io',
    description='This Python package provides convenient access to the Local API REST interface of the Kameleo Client.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kameleo-io/local-api-client-python',
    packages=setuptools.find_packages(),
    install_requires=['msrest'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
 )
