from __future__ import unicode_literals

import re
from setuptools import find_packages
from setuptools import setup


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-MQTT-NG',
    version=get_version('mopidy_mqtt/__init__.py'),
    license='Apache License, Version 2.0',
    description='Mopidy extension for remote control via MQTT broker',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Michal Odnous',
    author_email='odiroot@users.noreply.github.com',
    url='https://github.com/odiroot/mopidy-mqtt',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'Environment :: No Input/Output (Daemon)',
    ],
    install_requires=[
        'Mopidy >= 3.0',
        'paho-mqtt',
        'Pykka >= 2.0',
        'setuptools',
    ],
    entry_points={
        'mopidy.ext': [
            'mqtt = mopidy_mqtt:Extension',
        ],
    },
)
