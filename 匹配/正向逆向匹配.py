import os
import random
import re
from string import punctuation as puncEn
from zhon.hanzi import punctuation as puncZh
import jieba

class Match():

    def __init__(self, text:str, Forward:bool, dictionary:list):
        self.text = text
        self.Forward = Forward
        self.dictionary = dictionary
        self.after_cut = []
        # print(self.text)

    def text_cut(self, Maxsize = 5):
        """
        分词函数
        :Maxsize: 为默认的最大匹配跨度
        :return:
        """
        init_Maxsize = Maxsize
        if self.Forward == True:
            # print("正向最大匹配算法")
            start = 0
            while(True):
                if start >= len(self.text):
                    break
                if start + Maxsize >= len(self.text):
                    Maxsize = len(self.text) - start
                # print(self.text[start : start + Maxsize])
                if Maxsize == 1:
                    self.after_cut.append(self.text[start : start + Maxsize])
                    start += Maxsize
                    Maxsize = init_Maxsize
                elif self.text[start : start + Maxsize] in puncEn or self.text[start : start + Maxsize] in puncZh or self.text[start : start + Maxsize] == " " or self.text[start : start + Maxsize] == "\n":
                    # 若为标点
                    self.after_cut.append(self.text[start : start + Maxsize])
                    start = start + Maxsize
                    Maxsize = init_Maxsize
                elif self.text[start : start + Maxsize] in self.dictionary:
                    # 若在词典中
                    self.after_cut.append(self.text[start : start + Maxsize])
                    start = start + Maxsize
                    Maxsize = init_Maxsize
                elif self.text[start : start + Maxsize].isdigit() :
                    self.after_cut.append(self.text[start : start + Maxsize])
                    start = start + Maxsize
                    Maxsize = init_Maxsize
                else:
                    # 检测为英文的情况
                    En_text = self.text[start : start + Maxsize]
                    English_Bool = True
                    for i in En_text:
                        if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
                            pass
                        else:
                            English_Bool = False
                            break
                    if English_Bool == True:
                        self.after_cut.append(En_text)
                        start += Maxsize
                    else:
                        English_Bool = True
                        Maxsize -= 1
        else:
            start = len(self.text)
            while(True):
                # print("逆向最大匹配算法")
                if start <= 0:
                    break
                if start - Maxsize < 0:
                    Maxsize = start
                # print(self.text[start - Maxsize:start])
                if Maxsize == 1:
                    self.after_cut.append(self.text[start - Maxsize : start])
                    start -= Maxsize
                    Maxsize = init_Maxsize
                elif self.text[start - Maxsize:start] in puncEn or self.text[start - Maxsize:start] in puncZh or self.text[start - Maxsize:start] == " " or self.text[start - Maxsize:start] == "\n":
                    # 若为标点
                    self.after_cut.append(self.text[start - Maxsize:start])
                    start = start - Maxsize
                    Maxsize = init_Maxsize
                elif self.text[start - Maxsize:start] in self.dictionary:
                    # 若在词典中
                    self.after_cut.append(self.text[start - Maxsize:start])
                    start = start - Maxsize
                    Maxsize = init_Maxsize
                elif self.text[start - Maxsize:start].isdigit() :
                    self.after_cut.append(self.text[start - Maxsize:start])
                    start = start - Maxsize
                    Maxsize = init_Maxsize
                else:
                    # 检测为英文的情况
                    En_text = self.text[start - Maxsize:start]
                    English_Bool = True
                    for i in En_text:
                        if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
                            pass
                        else:
                            English_Bool = False
                            break
                    if English_Bool == True:
                        self.after_cut.append(En_text)
                        start -= Maxsize
                    else:
                        English_Bool = True
                        Maxsize -= 1
            self.after_cut.reverse()
        # print(self.after_cut)

        return self.after_cut

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

def prf(region_standard:list, region_result:list):
    region_standard = set(region_standard)
    region_result = set(region_result)
    A_size = 0
    B_size = 0
    C_size = 0
    A_size += len(region_standard)
    B_size += len(region_result)
    C_size += len(region_result & region_standard)
    P = C_size / B_size
    R = C_size / A_size
    F = 2 * P * R / (P + R)
    return (P, R, F)


# 提取测试语料
text = []
with open("克苏鲁神话-测试语料 黑太岁.txt", "r", encoding="utf-8") as f:
    text.append(str(f.read()))
# print(text[0])
text = text[0]

# 提取词典
dictionary = list(open("wordlist.Dic", "r"))
Dictionary = []
# print(dictionary)
dictionary.pop(0)
for word in dictionary:
    word = word.split(" ")[1]
    word = word.split("\n")
    # print(word[0])
    Dictionary.append(word[0])
# print(Dictionary)
forward_match = Match(text, True, Dictionary)
backward_match = Match(text, False, Dictionary)
# text_match = Match("那些住在青岛而且经常关注本地新闻的人and可能听beautiful说过我要提起的这件事there is no asd sdv", False, Dictionary)
forward_cut = forward_match.text_cut(10)
text_forward = " ".join(forward_cut)
forward_indexes = to_Region(text_forward)
backward_cut = backward_match.text_cut(10)
text_backward = " ".join(backward_cut)
backward_indexes = to_Region(text_backward)
text_jieba = " ".join(jieba.cut(text))
jieba_indexes = to_Region(text_jieba)
p1, r1, f1 = prf(jieba_indexes, forward_indexes)
p2, r2, f2 = prf(jieba_indexes, backward_indexes)
print(f"正向匹配准确率：p{p1}, r{r1}, f{f1}")
print(f"逆向匹配准确率：p{p2}, r{r2}, f{f2}")
# print(text_backward)
# print(text_forward)

# # 优化词典
# filePath = "D:\Study\Study in MUC\作业\自然语言处理\克苏鲁神话文本处理\匹配\训练语料"
# names = os.listdir(filePath)
# new_text = ""
# for name in names:
#     with open("./训练语料/" + name, "r", encoding="utf-8") as f:
#         new_text += str(f.read())
#     # print(len(new_text))
# jieba_cut = jieba.cut(new_text)
# print(len(Dictionary))
# for word in jieba_cut:
#     if word not in Dictionary:
#         Dictionary.append(word)
#         print(word)
# print(len(Dictionary))
# with open("Dictionary.txt", "w", encoding="utf-8") as fp:
#     for i in Dictionary:
#         fp.write(str(i))
#         fp.write("\n")

