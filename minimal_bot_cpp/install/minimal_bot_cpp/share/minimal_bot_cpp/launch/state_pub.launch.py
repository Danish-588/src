from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.substitutions import FindPackageShare
import os

def generate_launch_description():
    urdf_file = os.path.join(
        FindPackageShare("minimal_bot_cpp").find("minimal_bot_cpp"),
        "urdf",
        "minimal_bot.urdf.xacro"
    )

    return LaunchDescription([
        # Robot State Publisher
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            output="screen",
            parameters=[{
                "robot_description": Command(["xacro ", urdf_file])
            }]
        ),

        # Static TF Publisher
        Node(
            package="minimal_bot_cpp",
            executable="static_tf_publishers",
            name="static_tf_publishers",
            output="screen"
        )
    ])
