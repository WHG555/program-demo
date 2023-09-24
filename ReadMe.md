# ROS工作空间

1）src：代码空间（Source Space），开发过程中最常用的文件夹，用来存储所有ROS功能包的源码文件。
2）build：编译空间（Build Space），用来存储工作空间编译过程中产生的缓存信息和中间文件。
3）devel：开发空间（Development Space），用来放置编译生成的头文件、动态链接库、静态链接库、可执行文件等、环境变量
4）install：安装空间（Install Space），编译成功后，可以使用make install命令将可执行文件安装到该空间中，运行该空间中的环境变量脚本，即可在终端中运行这些可执行文件。安装空间并不是必需的，很多工作空间中可能并没有该文件夹。


# 创建工作空间
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace

# 编译
cd ~/catkin_ws/
catkin_make
source ~/catkin_ws/devel/setup.bash

# 创建功能包
cd ~/catkin_ws/src
catkin_create_pkg test_pkg std_msgs rospy roscpp

# 编译功能包
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
