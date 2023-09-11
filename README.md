### Realsense D435i VSLAM in RTAB-Map  ###


## structure
```
launch
    │  
    ├──realsenseD435i.launch.py         (啟動realsense D435i Node)
    │  
    ├──rtabmap.launch.py                (啟動RTAB-Map)
    │  
    ├──drone_mapping.launch.py          (同時啟動realsene D435i & RTAB-Map 建圖模式)
    │  
    ├──drone_localization.launch.py     (同時啟動realsene D435i & RTAB-Map 定位模式)
    │  
    ├──test.launch.py                   (just for test the launch file)
```

## paramters
rtabmap_args,   default_value='',       description='Can be used to pass RTAB-Map\'s parameters or other flags like --udebug and --delete_db_on_start/-d' 
mode            default_value='true',   description='Launch in localization mode.' 
rtabmap_viz,    default_value='false',  description='Launch RTAB-Map UI (optional).' 
rviz,           default_value='true',   description='Launch RVIZ (optional).' 