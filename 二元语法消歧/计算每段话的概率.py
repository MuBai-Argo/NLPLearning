from 语料库 import Two_Gram
import pandas as pd

# 首先按句提取文本内容
sentences = []
paragraphs = []
probilities = []
paragraphs_probilities = []
with open("./Script/按句划分.txt", "r", encoding="utf-8")as f:
    for i in f.readlines():
        if len(i) > 5:
            sentences.append(i[:-1])
two_Gram = Two_Gram()
for sentence in sentences:
    probilities.append(two_Gram.two_gram_model(sentence.split(" ")))

with open("./Script/每句话的概率.csv", "w", encoding="utf-8")as f:
    f.write(f"Sentence, Probility\n")
    for i in range(len(sentences)):
        f.write(sentences[i])
        f.write(",")
        f.write(str(probilities[i]))
        f.write("\n")

with open('./Script/二元语法消歧结果.txt', "r", encoding="utf-8")as f:
    for paragraph in f.readlines():
        if len(paragraph) > 10:
            paragraphs.append(paragraph)
for paragraph in paragraphs:
    paragraphs_probilities.append(two_Gram.two_gram_model(paragraph.split(" ")))

with open("./Script/每段话的概率.csv", "w", encoding="utf-8")as f:
    f.write(f"Paragraph, Probility\n")
    for i in range(len(paragraphs)):
        f.write(paragraphs[i])
        f.write(",")
        f.write(str(paragraphs_probilities[i]))
        f.write("\n")
