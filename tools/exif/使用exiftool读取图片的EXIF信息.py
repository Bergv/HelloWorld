import subprocess

def read_exif_with_exiftool(image_path):
    """
    使用exiftool读取图片的EXIF信息
    :param image_path: 图片文件路径
    """
    # 构造exiftool命令
    command = ['exiftool', image_path]
    
    # 执行命令并捕获输出
    result = subprocess.run(command, capture_output=True, text=True)
    
    # 检查命令是否成功执行
    if result.returncode == 0:
        # 打印EXIF信息
        print(result.stdout)
    else:
        print("Error executing exiftool:", result.stderr)

# 使用示例
image_path = 'path/to/your/image.jpg'
read_exif_with_exiftool(image_path)
