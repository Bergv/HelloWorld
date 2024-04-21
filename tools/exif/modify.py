import subprocess

def modify_exif(image_path, exif_tags):
    """
    请确保在运行脚本之前，已经正确安装了exiftool，并且exiftool的路径已经添加到了系统的环境变量中
    修改图片的EXIF信息
    :param image_path: 图片文件路径
    :param exif_tags: 字典，包含要修改的EXIF标签和值
    """
    for tag, value in exif_tags.items():
        subprocess.run(['exiftool', '-' + tag, value, image_path])

# 使用示例
image_path = 'path/to/your/image.jpg'
new_exif_tags = {
    'Artist': 'New Author',
    'Copyright': 'New Copyright Info',
    'DateTimeOriginal': '2023:03:15 10:00:00'  # 注意日期时间格式需要符合exiftool要求
}

modify_exif(image_path, new_exif_tags)
