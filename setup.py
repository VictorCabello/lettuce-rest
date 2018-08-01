from setuptools import setup
from setuptools import find_packages

lineiter = (line.strip() for line in open('requirements/base.txt'))
required = [line for line in lineiter if line and not line.startswith("#")]
required = list(map(lambda x: x.split(' ')[0], required))


setup(
    name='lettuce_rest',
    version='0.0.1',
    license='BSD',
    author='Victor Cabello',
    author_email='vmeca87@gmail.com',
    packages=find_packages(exclude=['tests']),
    package_data={},
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=required,
)
