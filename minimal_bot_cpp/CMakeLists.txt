cmake_minimum_required(VERSION 3.8)
project(minimal_bot_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(xacro REQUIRED)
find_package(rclcpp REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(geometry_msgs REQUIRED)

install(DIRECTORY launch urdf
  DESTINATION share/${PROJECT_NAME}
)

# ✅ This block is essential — move it outside of BUILD_TESTING
add_executable(static_tf_publishers src/static_tf_publishers.cpp)
ament_target_dependencies(static_tf_publishers rclcpp tf2_ros geometry_msgs)
install(TARGETS static_tf_publishers DESTINATION lib/${PROJECT_NAME})
install(DIRECTORY launch urdf
  DESTINATION share/${PROJECT_NAME}
)

# Optional testing block
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
