cmake_minimum_required(VERSION 3.0.2)
project(node_basics_p)
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
)
target_link_libraries(hello_log_cpp_e 
 ${catkin_LIBRARIES}
)

catkin_package()
#include_directories(
#  ${catkin_INCLUDE_DIRS}
#)
add_executable(hello_log_cpp_e src/hello_log.cpp)
