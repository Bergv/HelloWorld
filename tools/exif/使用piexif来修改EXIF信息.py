import piexif
import io
from PIL import Image

'''
在这个脚本中，我们首先打开图片文件并读取原始数据。
然后，我们使用piexif加载原始EXIF数据，并创建一个新的字典来包含要更新的EXIF字段。
我们更新这个字典，并将其转换回字节格式。
最后，我们使用PIL（Pillow）库来打开图片，将新的EXIF数据写入图片，并保存修改后的图片。
'''

def modify_exif_and_save(image_path, new_exif_dict):
    # 打开图片文件
    with open(image_path, 'rb') as src:
        raw_data = src.read()

    # 加载原始EXIF数据
    exif_bytes = piexif.dump(piexif.load(raw_data))

    # 合并新的EXIF数据
    exif_dict = piexif.load(exif_bytes)
    exif_dict.update(new_exif_dict)
    exif_bytes_new = piexif.dump(exif_dict)

    # 将新的EXIF数据写入到图片中
    img = Image.open(image_path)
    rgb_im = img.convert('RGB')
    out = io.BytesIO()
    rgb_im.save(out, format='JPEG', exif=exif_bytes_new)

    # 保存修改后的图片
    with open(image_path, 'wb') as dest:
        dest.write(out.getvalue())

# 使用示例
image_path = 'path/to/your/image.jpg'
new_exif_data = {
    piexif.ImageIFD.Artist: 'Your Name',
    piexif.ImageIFD.Copyright: 'Your Copyright Info',
    # 更多字段可以根据需要添加
}

modify_exif_and_save(image_path, new_exif_data)
