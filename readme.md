### Oscilloscope

- 实现对can线数据（示波器效果）与摄像头的同步播放
- 场景片段标注

### 使用说明

1. 配置Config
    1. 'Start': 起始时间戳，默认为None，当需要中断程序添加新的示波器时，输入当前时间戳后可从此设置断点实现继续播放。
    2. 'Video': 视频文件路径
    3. 'Oscilloscope': 示波器相关配置
        1. 'Radar_path': 解析后的radar路劲
        2. 'show_oscilloscope_secen_time'： 示波器展示的时长宽度
        3. 'select': 示波器展示的表及属性字典
            1. 结构为 ‘表名后缀’:['属性1','属性2']
    4. 'SaveJsonPath'： json标注文件存储保存路径
    5. 'label_list'：场景标签列表
2. 依赖配置

- 该软件应在window系统下运行，在unbuntu中存在QT与cv2的冲突

   ```
   pip install -r requirements.txt
   ```

3. 运行

    ```
    python main_develop.py
    ```
### 冲突说明
1. 按键说明（方向键盘可能不可用，笔记本存在热键冲突）
    1. ‘空格’ 实现暂停
    2. ‘a’ 实现 回退
    3. ‘d’ 实现 快进
    

2. 示波器存在部分属性字符型数据，需转换为数字编码

3. 示波器请添加两个及以上的属性，单一属性展示会引发程序崩溃（可修复，待排期）