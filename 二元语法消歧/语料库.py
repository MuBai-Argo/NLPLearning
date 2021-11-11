import collections

import jieba

from string import punctuation as puncEn
from zhon.hanzi import punctuation as puncZh
# 对语料库进行处理
yuliaoku = []
text = ""
with open("./Script/1998人民日报（分词）.txt", "r") as f:
    for i in f.read():
        if i in puncZh or i in puncEn or i == "\n":
            yuliaoku.append(i)
            continue
        if i == " " :
            if text != "":
                yuliaoku.append(text)
            text = ""
        else:
            text += i

with open("./Script/训练语料整合.txt", "r", encoding="utf-8") as f:
    for i in f.read():
        if i in puncZh or i in puncEn or i == "\n":
            yuliaoku.append(i)
            continue
        if i == " " :
            if text != "":
                yuliaoku.append(text)
            text = ""
        else:
            text += i

# word_number = len(yuliaoku)

# yuliaoku = ["克苏鲁"]
class Two_Gram():

    def __init__(self):
        # 单个词频统计
        self.words_count = collections.Counter(yuliaoku)
        # print(words_count)
        # 计算相邻两个词的词频
        self.two_gram_words = [yuliaoku[i] + yuliaoku[i + 1] for i in range(len(yuliaoku) - 1)]
        self.two_gram_words_count = collections.Counter(self.two_gram_words)


    def get_Gram_count(self, word, word_count ):
        """
        获取词在word_count中的词频
        :param word: 待统计的单词
        :param word_count: Counter词频
        :return:
        """
        if word in word_count:
            return word_count[word]
        else:
            # 返回最小词频
            # return word_count.most_common()[-1][-1]
            return 1

    def two_gram_model(self, sentense_cut:list):
        """
        二元语法模型
        :param sentense: 分词结果
        :return: 该句子的二元语法概率
        """
        probility = 1
        # 计算可能性
        sentense = []
        for i in sentense_cut:
            if i != " " and i != "":
                sentense.append(i)
        for i in range(1, len(sentense)):
            lamba = 0.7
            word = sentense[i]
            pre_word = sentense[i - 1]
            two_word_count = self.get_Gram_count(pre_word + word, self.two_gram_words_count)
            one_word_count = self.get_Gram_count(pre_word, self.words_count)
            pro = (two_word_count + 1) / one_word_count
            # 线性插值
            probility *= (lamba * pro + (1 - lamba) * one_word_count / len(yuliaoku))

        return probility


# print(yuliaoku)
# test = " ".join(jieba.cut("迈向 充满 希望 的 新 世纪 —— 一九九八年 新年 讲话"))
# two_Gram = Two_Gram()
# probility = two_Gram.two_gram_model(test.split(" "))
# print(probility)
#
#











