|-- CMakeLists.txt  # （必须）当前package的编译规则。通常需要为c++代码添加编译时的依赖，执行等操作。
|—— package.xml     # （必须）package的描述信息。通常添加一些ros库的支持。
|—— include文件夹    # 存放c++ 头文件的 
|—— config文件夹     # 存放参数配置文件
|—— launch文件夹     # 存放launch文件(.launch或.xml) 
|—— meshes文件夹     # 存放机器人或仿真场景的3D模型(.sda, .stl, .dae等) ； 
|—— urdf文件夹       # 存放机器人的模型描述(.urdf或.xacro) ；
|—— rviz文件夹       # rviz文件
|—— src文件夹        # c++源代码
|—— scripts文件夹    # 可执行脚本；例如shell脚本(.sh)、Python脚本(.py) 脚本要有可执行权限； 
|—— srv文件夹        # 自定义service 
|—— msg文件夹        # 自定义topic
|—— action文件夹     # 自定义action
