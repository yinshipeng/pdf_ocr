import pytesseract
from PIL import Image
import os
import sys
from wand.image import Image as WandImage

input_file = sys.argv[1]
output_file = sys.argv[2]

# 将PDF文件转换为图像文件
with WandImage(filename=input_file, resolution=300) as img:
    img.compression_quality = 99
    img.save(filename='temp_images/page.jpg')

# 使用Pytesseract进行OCR
# 设置语言参数为中文
language = 'chi_sim'
text = ''
for i, file in enumerate(sorted(os.listdir('temp_images'))):
    with Image.open(f'temp_images/{file}') as img:
        text += pytesseract.image_to_string(img, lang=language)

# 将OCR文本保存到文件中
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(text)

# 清除临时图像
for file in os.listdir('temp_images'):
    os.remove(f'temp_images/{file}')
