import argparse
import moviepy.editor as mp
import os


def extract_audio(video_file_path, output_file_path):
    """
    从视频中提取出音频文件
    :param video_file_path: 视频文件路径
    :param output_file_path: 音频文件保存路径
    :return: 音频文件路径
    """
    path = os.getcwd()
    my_clip = mp.VideoFileClip(video_file_path)
    output_dir_path = os.path.join(path, output_file_path)
    audio_path = os.path.join(output_dir_path, os.path.basename(video_file_path)) + ".mp3"
    # 创建保存路径文件夹（存在则跳过）
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)
    my_clip.audio.write_audiofile(audio_path)
    return audio_path


def file_exists(file_path):
    """
    检查文件路径是否存在
    :param file_path: 文件路径
    :return: 存在则返回文件路径，否则返回False
    """
    path = os.getcwd()
    if os.path.isfile(os.path.join(path, file_path)):
        return os.path.join(path, file_path)
    elif os.path.isfile(file_path):
        return file_path
    else:
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract audio from a video file')
    parser.add_argument('video_file_path', type=str, nargs='?', default='./video/1.mp4', help='Path to the video file')
    parser.add_argument('output_file_path', type=str, nargs='?', default='audio', help='Path to save the extracted audio file')
    args = parser.parse_args()

    video_file_path = file_exists(args.video_file_path)
    output_file_path = args.output_file_path

    if video_file_path:
        try:
            audio_path = extract_audio(video_file_path, output_file_path)
            print("提取视频音频文件成功")
            print("音频文件已保存至" + audio_path)
        except Exception as e:
            print('提取视频音频文件失败')
            print("错误信息：", e)
    else:
        print("文件路径错误!")
