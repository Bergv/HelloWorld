from PIL import Image
from PIL.ExifTags import TAGS

def read_exif_with_pillow(file_path):
    # 打开图片
    img = Image.open(file_path)

    # 获取EXIF数据
    exif_data = img._getexif()

    # 如果存在EXIF数据，则打印
    if exif_data is not None:
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"{tag}: {value}")

# 使用示例
image_path = 'path/to/your/image.jpg'
read_exif_with_pillow(image_path)
