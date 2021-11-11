from 语料库 import Two_Gram
import pandas as pd

# 首先按句提取文本内容
sentences = []
probilities = []
with open("./Script/按句划分.txt", "r", encoding="utf-8")as f:
    for i in f.readlines():
        if len(i) > 5:
            sentences.append(i[:-1])
two_Gram = Two_Gram()
for sentence in sentences:
    if sentence == " 留着 辫子 ":
        print(sentence)
    probilities.append(two_Gram.two_gram_model(sentence.split(" ")))

with open("./Script/每句话的概率.csv", "w", encoding="utf-8")as f:
    f.write(f"Sentence, Probility\n")
    for i in range(len(sentences)):
        f.write(sentences[i])
        f.write(",")
        f.write(str(probilities[i]))
        f.write("\n")