# 英文詞雲

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

with open("text17_28.txt") as fp:   # 英文字的文字檔
    txt = fp.read()                 # 讀取檔案

wd = WordCloud(
    font_path='C:\\Windows\\Fonts\\LHANDW.TTF',
    background_color='white',
    width=1000, height=880
).generate(txt)                 # 由txt文字產生WordCloud物件(此處設定個個參數)
imageCloud = wd.to_image()          # 由WordCloud物件建立詞雲影像檔
imageCloud.show()                   # 顯示詞雲影像檔


# 中文詞雲
with open('chinese_traditional.txt') as fn:
    txt = fn.read()
cut_text = ' '.join(jieba.cut(txt))
wd = WordCloud(
    font_path='C:\\Users\\88698\\AppData\\Local\\Microsoft\\Windows\\Fonts\\蘋果儷中黑.TTF',
    background_color='white',
    width=1000, height=800).generate(cut_text)

imageCloud = wd.to_image()
imageCloud.show()

# 有圖型的詞雲

txt = ''''
浪板舵腳繩臘短板板長內長板趴板防寒衣防摩衣槍板
魚板滑水起乘歪爆長板站板頭衝單腳站板頭雙腳同時在板頭
右腳在前左腳在前背向衝正向浪底浪頂轉向浪壁加速
切迴轉向浪頂甩浪崩潰點漂浮轉向浪頂騰空波管駕乘'''
cut_text = ' '.join(jieba.cut(txt))

bgimage = np.array(Image.open('surf.png'))  # 背景圖

wd = WordCloud(
    font_path='C:\\Users\\88698\\AppData\\Local\\Microsoft\\Windows\\Fonts\\蘋果儷中黑.TTF',
    background_color='white',
    mask=bgimage
).generate(cut_text)

plt.imshow(wd)
plt.axis("off")
plt.show()
