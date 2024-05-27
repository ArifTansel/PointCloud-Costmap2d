#!/usr/bin/env python

import rospy
import tf2_ros
import geometry_msgs.msg

def publish_world_frame():
    rospy.init_node('world_frame_publisher', anonymous=True)
    tf_broadcaster = tf2_ros.StaticTransformBroadcaster()

    world_transform = geometry_msgs.msg.TransformStamped()
    world_transform.header.stamp = rospy.Time.now()
    world_transform.header.frame_id = "chassis"  # Parent frame
    world_transform.child_frame_id = "map"  # Child frame
    world_transform.transform.translation.x = 0.0
    world_transform.transform.translation.y = 0.0
    world_transform.transform.translation.z = 0.0
    world_transform.transform.rotation.x = 0.0
    world_transform.transform.rotation.y = 0.0
    world_transform.transform.rotation.z = 0.0
    world_transform.transform.rotation.w = 1.0

    while not rospy.is_shutdown():
        world_transform.header.stamp = rospy.Time.now()
        tf_broadcaster.sendTransform(world_transform)
        rospy.sleep(1.0)  # Publish every second

if __name__ == '__main__':
    try:
        publish_world_frame()
    except rospy.ROSInterruptException:
        pass
