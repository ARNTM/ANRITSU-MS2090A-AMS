from setuptools import setup, Extension


setup(
    name='anritsu_ms2090a_ams',
    version='1.0.0',
    description='ANRITSU MS2090A Automatic Measurement System',
    package_dir={'': 'src'},
    install_requires=[
        'pyvisa',
        'pandas',
        'pyvisa-py'
    ],
    scripts=['src/anritsu_ms2090a_ams.py'],
    url='https://github.com/aruznieto/ANRITSU-MS2090A-AMS',
    author='Andres Ruz-Nieto',
    entry_points={
        'console_scripts': ['anritsu_ms2090a_ams=anritsu_ms2090a_ams:main']
    }
)