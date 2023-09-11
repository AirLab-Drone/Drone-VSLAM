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
                get_package_share_directory('drone_vslam'),
                'launch/realsenseD435i.launch.py'
            )
        )
    )

    # RTAB-Map launch
    RtabMapLaunchFile = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('drone_vslam'),
                'launch/rtabmap_mapping.launch.py'
            )
        )
    )
    
    ld.add_action(RealsenseD435iLaunchFile)
    ld.add_action(RtabMapLaunchFile)

    return ld


