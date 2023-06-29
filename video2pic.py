import os.path

import cv2
import argparse


def extract_frames(video_path, start_time=0, end_time=None, output_path="frames_output"):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        # 打开视频文件
        video = cv2.VideoCapture(video_path)

        # 检查视频是否成功打开
        if not video.isOpened():
            raise Exception("Unable to open the video file.")

        # 获取视频的帧率
        fps = video.get(cv2.CAP_PROP_FPS)

        # 计算开始和结束的帧数
        start_frame = int(start_time * fps)

        if end_time is not None:
            end_frame = int(end_time * fps)
        else:
            end_frame = int(video.get(cv2.CAP_PROP_FRAME_COUNT)) - 1

        # 检查开始和结束帧数的范围是否有效
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        if start_frame < 0 or start_frame >= total_frames:
            raise Exception("无效的输入时间")
        if end_frame < start_frame or end_frame >= total_frames:
            raise Exception("无效的输出时间")

        # 设置当前帧数为开始帧数
        video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

        # 初始化帧计数器
        frame_count = 0

        # 循环读取帧，直到到达结束帧
        while video.isOpened() and frame_count <= (end_frame - start_frame):
            ret, frame = video.read()

            if ret:
                # 保存当前帧为图像文件
                frame_output_path = f"{output_path}/frame_{frame_count}.jpg"
                cv2.imwrite(frame_output_path, frame)
                print(f"Saved frame {frame_count}")

                frame_count += 1
            else:
                break

    except Exception as e:
        print(f"Error occurred: {str(e)}")

    finally:
        # 释放视频对象和窗口
        if video is not None:
            video.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # 创建解析器对象
    parser = argparse.ArgumentParser(description='Video to Image Extraction')

    # 添加命令行参数
    parser.add_argument('--video_path', type=str, default='./video/1.mp4', help='Path to the video file')
    parser.add_argument('--start_time', type=float, default=0, help='Start time in seconds')
    parser.add_argument('--end_time', type=float, help='End time in seconds')
    parser.add_argument('--output_path', type=str, default="frames_output", help='Path to save the extracted frames')

    # 解析命令行参数
    args = parser.parse_args()

    # 调用函数进行视频提取和转换为图片
    extract_frames(args.video_path, args.start_time, args.end_time, args.output_path)
