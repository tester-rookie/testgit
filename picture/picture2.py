# from wordcloud import WordCloud
import wordcloud
import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
# 解决读取图片报错
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
import os


# 获取背景文字
def gen_text_img(text, font_size, font_path=None):
    '''
    输入：
    text：照片墙的样式文字
    font_size：字体的大小
    font_path：字体
    返回：
    文字图像
    '''
    font = ImageFont.truetype(font_path, font_size)
    (width, length) = font.getsize(text)
    text_img = Image.new('RGB', (width + 100, length + 100), color='white')
    draw = ImageDraw.Draw(text_img)
    # 从左上角开始绘制，每次调整位置用于加粗字体
    for i in range(100):
        draw.text((i, i), text, fill=(0, 0, 0), font=font)
    text_img.save('background.png')
    return text_img


def word_cloud(img, word, font_path=None):
    wc_mask = np.array(Image.open('background.png'))
    wc = wordcloud.WordCloud(
        # 设置字体格式
        font_path=font_path,
        # 设置背景图
        mask=wc_mask,
        # 最多显示词数
        max_words=200,
        # 字体最大值
        max_font_size=320,
        # 整体背景色
        background_color='White',
        # 词云的边框大小
        contour_width=2,
        # 词云的边框颜色
        contour_color='pink',
        # 设置字体重复
        repeat=True,
        color_func=lambda *args,
                          **kwargs: "pink")

    # 从字典生成词云
    wc.generate(word)
    # 从背景图建立颜色方案
    image_colors = wordcloud.ImageColorGenerator(wc_mask)
    # 显示词云
    plt.figure(figsize=[10, 10], dpi=300)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()


def main(font_path='buzz_cloud_font.ttf',
         font_size=2000,
         ):
    word = input('请输入填充词：')
    text = input('请输入背景词：')
    img = gen_text_img(text, font_size, font_path)
    word_cloud(img, word, font_path)


main()
