from setuptools import setup
import distutils_symlink_enabler

setup(
    name='package_data_symlink',
    version='0.0.0.1',
    packages=['package_data_symlink'],
    # include_package_data=True,
    package_data={'package_data_symlink':['data1/hello.txt','data2']},
    license='0BSD',
)
