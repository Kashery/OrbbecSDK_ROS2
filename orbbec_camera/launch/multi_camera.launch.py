from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, GroupAction, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    # Node configuration
    cleanup_node = Node(
        package='orbbec_camera',
        executable='ob_cleanup_shm_node',
        name='camera',
        output='screen'
    )

    # Include launch files
    package_dir = get_package_share_directory('orbbec_camera')
    launch_file_dir = os.path.join(package_dir, 'launch')
    launch1_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'dabai_dcw.launch.py')
        ),
        launch_arguments={
            'camera_name': 'camera_01',
            'usb_port': '5-3.4.4.2.1',
            'device_num': '2'
        }.items()
    )

    launch2_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'dabai_dcw.launch.py')
        ),
        launch_arguments={
            'camera_name': 'camera_02',
            'usb_port': '5-3.4.3.1',
            'device_num': '2'
        }.items()
    )

    # If you need more cameras, just add more launch_include here, and change the usb_port and device_num

    # Launch description
    ld = LaunchDescription([
        cleanup_node,
        GroupAction([launch1_include]),
        GroupAction([launch2_include]),
    ])

    return ld