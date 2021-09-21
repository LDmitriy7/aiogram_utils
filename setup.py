from setuptools import find_packages, setup


def get_description():
    with open('README.md') as f:
        return f.read()


setup(
    name='aiogram_utils',
    version='0.0.1',
    packages=find_packages(exclude=('tests', 'tests.*', 'examples.*', 'docs',)),
    url='https://github.com/LDmitriy7/aiogram_utils',
    license='MIT',
    author='LDmitriy7',
    requires_python='>=3.7',
    author_email='ldm.work2019@gmail.com',
    description='Misc utils for aiogram',
    long_description=get_description(),
)
