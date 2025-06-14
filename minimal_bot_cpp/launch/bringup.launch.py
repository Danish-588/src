from launch import LaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    # Absolute path to your map file
    map_path = "/ros2_ws/src/map_package/field2025.yaml"

    # Include the state publisher launch
    state_pub_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            FindPackageShare("minimal_bot_cpp"), "/launch/state_pub.launch.py"
        ])
    )

    return LaunchDescription([
        state_pub_launch,

        # Map Server node
        Node(
            package="nav2_map_server",
            executable="map_server",
            name="map_server",
            output="screen",
            parameters=[{
                "yaml_filename": "/ros2_ws/src/map_package/field2025.yaml"
            }]
        ),
            
        # AMCL node
        Node(
            package="nav2_amcl",
            executable="amcl",
            name="amcl",
            output="screen",
            parameters=[{
                "use_sim_time": False,
                "odom_frame_id": "odom",
                "base_frame_id": "base_footprint",
                "scan_topic": "scan"
            }]
        ),

        # Static transform map -> odom
        Node(
            package="tf2_ros",
            executable="static_transform_publisher",
            name="static_tf_map_odom",
            arguments=["0", "0", "0", "0", "0", "0", "map", "odom"],
            output="screen"
        ),

        Node(
            package="nav2_lifecycle_manager",
            executable="lifecycle_manager",
            name="lifecycle_manager_localization",
            output="screen",
            parameters=[{
                "use_sim_time": False,
                "autostart": True,
                "node_names": ["map_server", "amcl"]
            }]
        )


    ])
