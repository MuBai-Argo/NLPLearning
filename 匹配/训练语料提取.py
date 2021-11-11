import os

import jieba

filePath = "D:\Study\Study in MUC\作业\自然语言处理\克苏鲁神话文本处理\匹配\训练语料"
names = os.listdir(filePath)
new_text = ""
for name in names:
    with open("./训练语料/" + name, "r", encoding="utf-8") as f:
        new_text += str(f.read())
    # print(len(new_text))
jieba_cut = " ".join(jieba.cut(new_text))
with open("训练语料整合.txt", "w", encoding="utf-8")as f:
    f.write(jieba_cut)
