cmake_minimum_required(VERSION 3.0.2)
project(velodyne_description)


find_package(catkin REQUIRED COMPONENTS
	dynamic_reconfigure
	pcl_conversions
	pcl_ros
	roscpp
	rospy
	roslint
	sensor_msgs
)

generate_dynamic_reconfigure_options(
        config/Pcl.cfg      )
catkin_package()

include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)