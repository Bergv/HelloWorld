import piexif

def read_exif_with_piexif(file_path):
  # 首先，你需要安装这些库 pip install piexif pillow  
  # 读取文件二进制数据
    with open(file_path, 'rb') as f:
        raw_exif_data = f.read()

    # 解析EXIF数据
    exif_dict = piexif.load(raw_exif_data)

    # 打印EXIF信息
    if exif_dict['0th']:
        for tag_id, value in exif_dict['0th'].items():
            tag = piexif.TAGS['0th'][tag_id]
            print(f"{tag}: {value}")

# 使用示例
image_path = 'path/to/your/image.jpg'
read_exif_with_piexif(image_path)
