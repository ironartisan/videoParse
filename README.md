# videoParse

实现对视频的解析，可以解析出视频中的图像、音频及视频的基本信息。



## 环境要求

环境要求如下：

```bash
pymediainfo
moviepy
opencv-python
```


## 1.视频基本信息解析

功能：提取指定目录中的视频的基础信息

用法：

```bash
usage: extra_base.py [-h] [dir_path]

Extract video metadata

positional arguments:
  dir_path    Path to the video file

optional arguments:
  -h, --help  show this help message and exit

```



解析结果如下：

```text
【基本信息】
视频类型：MPEG-4 
视频文件大小：14.988 MB 
码率：2083437 kbps
视频时长：1分钟0秒 
【视频参数】
帧宽：1696 
帧高：720 
【音频参数】
音频格式：AAC 
音频采样率：44100 Hz
频道数量：2 
```


## 2.视频音频提取

功能：提取视频中的音频

用法：

```bash

usage: extra_audio.py [-h] [video_file_path] [output_file_path]

Extract audio from a video file

positional arguments:
  video_file_path   Path to the video file
  output_file_path  Path to save the extracted audio file

optional arguments:
  -h, --help        show this help message and exit
```

根据控制台提示，输入视频文件路径（绝对路径或相对路径都可以）

最终提取出的音频文件位于audio目录下


## 3.图像提取


功能：提取视频中指定时长的图像

用法：

```bash
usage: video2pic.py [-h] [--video_path VIDEO_PATH] [--start_time START_TIME] [--end_time END_TIME] [--output_path OUTPUT_PATH]

Video to Image Extraction

optional arguments:
  -h, --help            show this help message and exit
  --video_path VIDEO_PATH
                        Path to the video file
  --start_time START_TIME
                        Start time in seconds
  --end_time END_TIME   End time in seconds
  --output_path OUTPUT_PATH
                        Path to save the extracted frames
```



