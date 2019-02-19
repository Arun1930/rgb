
from setuptools import setup

setup(
    name='rgbd',
    version='0.1',
    description='turn lights on',
    url='https://github.com/Arun1930/rgb',
    author='Arun prasad',
    author_email='arun.prasad@xyzinnotech.com',
    license='apache 2.0',
    package_dir={'': 'src'},
    packages=['rgb', 'rgb.modbus_module'],
    entry_points={
        'console_scripts': ['say-hello=datahub.modbus_module.say_hello:main'],
    },
    zip_safe=False)
