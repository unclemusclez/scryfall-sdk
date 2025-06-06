from setuptools import setup, find_packages

setup(
    name='scryfall-sdk',
    version='0.0.1',
    packages=['scryfall'],
    install_requires=[
        'requests',
    ],
    author='Devin J. Dawson',
    author_email='devin@waterpistol.co',
    description='Scryfall SDK for interacting with Scryfall API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/unclemusclez/scryfall-sdk-python',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: GPL-3.0-or-later',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)