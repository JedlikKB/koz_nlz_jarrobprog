"""A távolságszenzor és a biztonsági monitor együttes indítása."""
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='koz_nlz_jarrobprog',
            executable='distance_publisher',
            name='distance_publisher',
            output='screen',
        ),
        Node(
            package='koz_nlz_jarrobprog',
            executable='safety_monitor',
            name='safety_monitor',
            output='screen',
        ),
    ])
