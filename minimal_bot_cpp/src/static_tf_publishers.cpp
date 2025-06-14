#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "tf2_ros/static_transform_broadcaster.h"
#include "geometry_msgs/msg/transform_stamped.hpp"

geometry_msgs::msg::TransformStamped make_tf(std::string parent, std::string child)
{
  geometry_msgs::msg::TransformStamped tf;
  tf.header.stamp = rclcpp::Clock().now();
  tf.header.frame_id = parent;
  tf.child_frame_id = child;
  tf.transform.translation.x = 0.0;
  tf.transform.translation.y = 0.0;
  tf.transform.translation.z = 0.0;
  tf.transform.rotation.x = 0.0;
  tf.transform.rotation.y = 0.0;
  tf.transform.rotation.z = 0.0;
  tf.transform.rotation.w = 1.0;
  return tf;
}

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<rclcpp::Node>("static_tf_broadcaster");

  auto broadcaster = std::make_shared<tf2_ros::StaticTransformBroadcaster>(node);

  std::vector<geometry_msgs::msg::TransformStamped> transforms;
  transforms.push_back(make_tf("map", "odom"));
  transforms.push_back(make_tf("odom", "base_footprint"));

  for (const auto & tf : transforms)
    broadcaster->sendTransform(tf);

  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
