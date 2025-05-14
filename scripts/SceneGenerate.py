#!/usr/bin/env python

import sys
import rospy
import moveit_commander
import geometry_msgs.msg

from math import pi, tau, dist, fabs, cos

class GenerateScene(object):
    
    def __init__(self):
        super(GenerateScene, self).__init__()
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node("scene_generate_node")  
        scene = moveit_commander.PlanningSceneInterface(synchronous = True)
        self.scene = scene  
             
    def scene_generate(self):
        
        scene = self.scene
        pose = geometry_msgs.msg.PoseStamped()
        pose.header.frame_id = "world"
        
        cube_side = 0.025
        
        #Box1
        pose.pose.position.y = 0.4
        pose.pose.position.z = (cube_side/2)
        pose.pose.orientation.w = 1.0
        scene.add_box('box1', pose, [cube_side]*3)
        
        #Box2
        pose.pose.position.y = 0.4+(cube_side)+0.005
        pose.pose.orientation.w = 1.0
        scene.add_box('box2', pose, [cube_side]*3)
        
        #Box3
        pose.pose.position.x = 0.2
        pose.pose.position.y = 0.35
        pose.pose.orientation.w = 1.0
        pose.pose.orientation.z = -0.45
        scene.add_box('box3', pose, [cube_side]*3)
        
        #cylinder
        pose.pose.position.x = -0.2
        pose.pose.position.y = 0.45
        pose.pose.position.z = 0.0375
        scene.add_cylinder('cylinder', pose, 0.075, 0.015)
        
        #goal_board
        pose.pose.position.x = -0.4
        pose.pose.position.y = -0.4
        pose.pose.position.z = 0.0025
        pose.pose.orientation.z = 0.3
        scene.add_box('board', pose, (0.15, 0.5, 0.005))       
    
    
if __name__ == "__main__":
    interface = GenerateScene()
    interface.scene_generate()
    
    