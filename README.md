# Assignment-2
This pacakge moves the husky robot in a circular path of specified radius using the differntial drive controller (skid steer method).  

## Getting Started

  * Clone this project in your catkin workspace under the **src** folder.  
    ```
    git clone https://github.com/Narendranthangavelu/Assignment-2.git 
    ```
    Build the project using the following command before that make sure you are in catkin workspace directory.  
    ```
    catkin_make
    ```   
### Launching Gazebo Model:
  * Husky_bot package has all the things that needs to spawn the husky robot in Gazebo. Husky robot can be launched using the following launch command.   
    ```
    roslaunch husky_bot husky.launch
    ```
    Note: Launch file of preinstalled husky robot can also be used instead of above mentioned launch file.   

### Circular Trajectory:
  * This node creates a publisher for the topic **/husky_velocity_controller/cmd_vel**. It takes the linear velocity and radius of circle as input and publishes linear and angular velocities.  
    To launch this node use the following command,  
 
    ```
    roslaunch husky_bot circle.launch
    ```
   
    And then give linear velocity and radius of circle to start the circular motion.  

    To change the radius and velocity of circular motion, **stop the process** by pressing the **ENTER** key.
    

    
    
    




