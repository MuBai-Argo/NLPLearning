# 这一部分有问题，注意插入文本的空格



def getclean(sentence : str):
    """
    返回当前句子去除分词符的版本
    :param sentence:
    :return:
    """
    temp = sentence.split(" ")
    temp = "".join(temp)
    return temp
puncs = ["，", "。", "……", "\n", ",", "、"]
forward_text = ""
sentences = []
After_Disambiguation = []
Clean_Disambiguation = []

with open("./Script/正向匹配.txt", "r", encoding="utf-8")as f:
    for i in f.read():
        forward_text += i
with open("./Script/消歧结果.txt", "r", encoding="utf-8")as f:
    for i in f.readlines():
        After_Disambiguation.append(i)
with open("./Script/歧义句子.txt", "r", encoding="utf-8")as f:
    for i in f.readlines():
        Clean_Disambiguation.append(i[:-1])
# print(After_Disambiguation)
# 需要去除末尾的换行符
After_Disambiguation = [i[:-1] for i in After_Disambiguation]
print(After_Disambiguation)
print(Clean_Disambiguation)


# print(forward_text)
clean_forward = []
# # 首先将forward中的文本提取为sentence
last = 0
for i in range(len(forward_text)):
    if forward_text[i] in puncs:
        sentences.append(forward_text[last])
        if forward_text[i - 1] == " ":
            if forward_text[last + 1] == " ":
                sentences.append(forward_text[last + 1])
                sentences.append(forward_text[last + 2 : i - 1])
            else:
                sentences.append(forward_text[last + 1: i - 1])
            sentences.append(forward_text[i - 1])
        else:
            if forward_text[last + 1] == " ":
                sentences.append(forward_text[last + 2 : i])
            else:
                sentences.append(forward_text[last + 1: i])

        last = i

print(sentences)
Dis_sentence = []
clean_sentences = []
j = 0
for i in range(len(sentences)):
    clean_sentence = getclean(sentences[i])[:]
    clean_sentences.append(clean_sentence)
    if clean_sentence in Clean_Disambiguation:
        Dis_sentence.append(sentences[i])
        index = Clean_Disambiguation.index(clean_sentence)
        sentences[i] = After_Disambiguation[index]
        print(clean_sentences[i])
        print(sentences[i])
        print(j)
        j += 1
print(sentences)
print("".join(sentences))
with open("./Script/二元语法消歧结果.txt", "w", encoding="utf-8")as f:
    for i in sentences:
        f.write(i)

with open("./Script/按句划分.txt", "w", encoding="utf-8")as f:
    for i in sentences:
        if i not in puncs:
            f.write(i)
        else:
            f.write("\n")

print(clean_sentences)
print(Dis_sentence)