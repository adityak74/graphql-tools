from setuptools import setup

setup(
	name='graphql-tools',
	version='0.1.0',
	description='GraphQL Tools written in Python',
	author='Aditya Karnam',
	author_email='akarnam37@gmail.com',
	packages=['graphql_tools'],
	install_requires=[
		'graphql-core',
	],
)
