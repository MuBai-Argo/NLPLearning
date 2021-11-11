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

Dictionary = []
with open("Dictionary.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        Dictionary.append(i[:-1])