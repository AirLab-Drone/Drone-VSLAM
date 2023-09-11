from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python import get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()

    # Realsense D435i launch
    RealsenseD435iLaunchFile = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('realsense2_camera'),
                'launch/rs_launch.py'
            )
        ),
        launch_arguments = {
            'enable_gyro': 'True',
            'enable_accel': 'True',
            'unite_imu_method': '1',
            'enable_infra1': 'True',
            'enable_infra2': 'True',
            'enable_sync': 'True',
            'depth_module.emitter_enabled': '0'
                            }.items()
    )

    # RTAB-Map launch
    RtabMapLaunchFile = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('rtabmap_examples'),
                'launch/realsense_d435i_infra.launch.py'
            )
        )
    )
    


    ld.add_action(RealsenseD435iLaunchFile)
    ld.add_action(RtabMapLaunchFile)

    return ld


