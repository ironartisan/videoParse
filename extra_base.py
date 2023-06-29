import os
import json
from pymediainfo import MediaInfo
import argparse

# 将GUI上展示的字段名和JSON字段建立映射表output_type来存储
PROPERTIES_MAP = {
    'General': {
        'format': {'name': '视频类型', 'unit': ''},
        'file_size': {'name': '视频文件大小', 'unit': ''},
        'overall_bit_rate': {'name': '码率', 'unit': 'kbps'},
        'duration': {'name': '视频时长', 'unit': ''},
    },
    'Video': {
        'sampled_width': {'name': '帧宽', 'unit': ''},
        'sampled_height': {'name': '帧高', 'unit': ''},
    },
    'Audio': {
        'format': {'name': '音频格式', 'unit': ''},
        'sampling_rate': {'name': '音频采样率', 'unit': 'Hz'},
        'channel_s': {'name': '频道数量', 'unit': ''},
    }
}

TRACK_TYPE_MAP = {
    'General': '基本信息',
    'Video': '视频参数',
    'Audio': '音频参数',
}


# 创建方法，统计每个文件路径，并追加列表中
def get_all_file(dir_path, init_list):
    for file in os.listdir(dir_path):
        filepath = os.path.join(dir_path, file)
        if os.path.isdir(filepath):
            print('遇到子目录---%s---不提取子目录视频信息--' % (filepath))
        # get_all_file(filepath)
        else:
            if not file.endswith('exe'):
                init_list.append(filepath)
    return init_list


# 执行上面方法，把每个文件的绝对路径追加到列表中
def get_all_dict(file_list):
    for i in range(len(file_list)):
        file = file_list[i]  # file为文件路径
        filename = os.path.split(file)[1]  # filename为文件名
        print("（{0}）{1}".format(i + 1, filename))
        try:
            get_media_info(file)
        except Exception as e:
            print(filename, '------提取此文件信息失败------')
            print("错误信息：", e)
        print()


# 获取单个media文件的元数据
def get_media_info(filename):
    media_info = MediaInfo.parse(filename)  # MediaInfo对象
    data_json = media_info.to_json()  # str类型的json字符串
    data_dict = json.loads(data_json)  # 将str类型的json字符串转换为dict类型的数据

    for num in range(len(media_info.tracks)):  # 多媒体文件信息主要包含三个部分：General、Video、Audio，media_info.tracks表示当前视频有哪几个部分
        tr = media_info.tracks[num]  # 格式例如：<Track track_id='None', track_type='General'>
        print('【' + TRACK_TYPE_MAP[tr.track_type] + '】')
        data_type = data_dict["tracks"][num]  # 某个部分的所有属性信息
        properties = PROPERTIES_MAP[tr.track_type]
        for tr_type in properties:
            tr_key = properties[tr_type]["name"]
            tr_unit = properties[tr_type]["unit"]
            tr_value = data_type[tr_type]
            if (tr_key == "视频文件大小"):
                tr_value = sizeConvert(tr_value)
            if (tr_key == "视频时长"):
                tr_value = timeConvert(tr_value)
            if tr_type:  # 当指定的字段值为None时，则跳过
                print("{0}：{1} {2}".format(tr_key, tr_value, tr_unit))  # 左对齐，使用format格式输出


# 文件大小单位换算，函数参数的单位为字节
def sizeConvert(size):
    K, M, G = 1024, 1024 ** 2, 1024 ** 3
    if size >= G:
        return str(round(size / G, 3)) + ' GB'
    elif size >= M:
        return str(round(size / M, 3)) + ' MB'
    elif size >= K:
        return str(round(size / K, 3)) + ' KB'
    else:
        return str(size) + ' Bytes'


# 时长单位换算，函数参数的单位为毫秒
def timeConvert(size):
    size /= 1000  # 毫秒→秒
    M, H = 60, 60 ** 2
    if size < M:
        return str(size) + u'秒'
    if size < H:
        return u'%s分钟%s秒' % (int(size / M), int(size % M))
    else:
        hour = int(size / H)
        mine = int(size % H / M)
        second = int(size % H % M)
        tim_srt = u'%s小时%s分钟%s秒' % (hour, mine, second)
        return tim_srt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract video metadata')
    parser.add_argument('dir_path', type=str, nargs='?', default='./video', help='Path to the video file')
    args = parser.parse_args()

    dir_path = args.dir_path

    # 定义列表，存放每个文件绝对路径，便于后期操作
    init_list = []

    # 执行方法，获取所有文件的绝对路径
    file_list = get_all_file(dir_path, init_list)

    print("------视频文件读取完毕，开始获取视频信息------")

    get_all_dict(file_list)
