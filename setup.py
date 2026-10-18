from glob import glob
from os.path import join
from setuptools import setup

package_name = 'koz_nlz_jarrobprog'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='JedlikKB',
    maintainer_email='noreply@users.noreply.github.com',
    description='ROS 2 robot proximity monitoring demo',
    entry_points={
        'console_scripts': [
            'distance_publisher = koz_nlz_jarrobprog.distance_publisher:main',
            'safety_monitor = koz_nlz_jarrobprog.safety_monitor:main',
        ],
    },
)
