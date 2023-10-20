from setuptools import setup, find_packages

setup(
	name='beautifile',
	version='1.0.0',
	description='Organize files into separate categories.',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	author='Angelo Yana',
	author_email='angeloyana.dev@gmail.com',
	url='https://github.com/angeloyana-dev/beautifile',
	license='MIT',
	packages=find_packages(),
	install_requires=['termcolor'],
	entry_points={
		'console_scripts': [
			'beautifile = beautifile.main:main'
		]
	},
	classifiers=[
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3'
	]
)