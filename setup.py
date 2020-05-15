from setuptools import setup, find_packages

setup(
    name='arena',
    version='0.1.0',
    description='python interface to the are.na api',
    url='https://github.com/BTBTravis/arena',
    author='Travis Shears (@btbtravis)',
    license='MIT',

    packages=find_packages(),
    install_requires=[
        'requests'
    ]
)