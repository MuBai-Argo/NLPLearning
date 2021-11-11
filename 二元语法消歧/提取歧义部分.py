def to_Region(result : str):
    """
    转换分词结果为分词索引，从而提取歧义部分
    :params
        result: 以空格为分词界限的字符串
    :return: 分词索引，每一格词语的首尾坐标集合
    """
    space_index = []
    # print(result)
    last = 0
    start = 0
    for i in result:
        # print(i)
        if i != " ":
            last += 1
        else:
            space_index.append((start, last - 1))
            start = last

    # print(space_index)
    return space_index

# 首先获取正向与逆向匹配的结果
text_forward = ""
with open(".\Script\正向匹配.txt", "r", encoding="utf-8")as f:
    text_forward += f.read()

text_backward = ""
with open(".\Script\逆向匹配.txt", "r", encoding="utf-8")as f:
    text_backward += f.read()
text_ori = ""
with open(".\Script\原始语料.txt", "r", encoding="utf-8")as f:
    text_ori += f.read()

# 获取歧义位置
error_indexes = []
forward_indexes = to_Region(text_forward)
backward_indexes = to_Region(text_backward)
for i in forward_indexes:
    if i not in backward_indexes:
        error_indexes.append(i)
# 提取原始语料语句分割位置
error_sentence_indexes = []
error_sentence = []
punc_indexes = []
last = 0
puncs = ["，", "。", "……", "\n", ",", "、"]
for i in range(len(text_ori)):
    if text_ori[i] in puncs:
        punc_indexes.append((last, i))
        last = i
last = 0
for i in punc_indexes:
    for j in error_indexes:
        if j[0]>= i[0] and j[1] <= i[1]:
            if (i[0] + 1, i[1]) not in error_sentence_indexes:
                print(text_ori[i[0] + 1:i[1]])
                error_sentence.append((text_ori[i[0] + 1:i[1]], text_ori[j[0]: j[1] + 1]))
                error_sentence_indexes.append((i[0] + 1, i[1]))


print(error_sentence_indexes)
print(text_ori[error_sentence_indexes[0][0]:error_sentence_indexes[0][1] + 1])
with open("./Script/歧义句子.txt", "w", encoding="utf-8") as f:
    for i in error_sentence:
        f.write(f"{i[0]}")
        f.write("\n")


