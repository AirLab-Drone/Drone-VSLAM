### Realsense D435i VSLAM in RTAB-Map  ###



```
launch
    │  
    ├──realsenseD435i.launch.py         (啟動realsense D435i Node)
    │  
    ├──rtabmap_mapping.launch.py        (啟動RTAB-Map 建圖模式)
    │  
    ├──rtabmap_localization.launch.py   (啟動RTAB-Map 定位模式)
    │  
    ├──drone_mapping.launch.py          (同時啟動realsene D435i & RTAB-Map 建圖模式)
    │  
    ├──drone_localization.launch.py     (同時啟動realsene D435i & RTAB-Map 定位模式)
    │  
    ├──test.launch.py                   (just for test the launch file)
```