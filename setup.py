import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='kameleo.local_api_client',
    version='2.3.2',
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
