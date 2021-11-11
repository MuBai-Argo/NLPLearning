# from 二元语法消歧.匹配模型 import Match, Dictionary
#
# class Node():
#     def __init__(self, text:str):
#         self.text = text
#         self.next = []
#         # self.parent
#
#     def addnext(self, nextnode):
#         self.next.append(nextnode)
#         self.parent = self
#
# class WordNet():
#     def __init__(self):
#         self.BOS = Node("")
#         self.nodes = []
#         self.words = []
#
#     def addFirst(self, first:Node):
#         self.BOS.next.append(first)
#         self.nodes.append(self.BOS)
#         self.nodes.append(first)
#
#     def addNode(self, parent:Node, next:Node):
#         parent.next.append(next)
#         self.nodes.append(next)
#
# # 构建词网
# error_senteces = []
# with open("./Script/歧义句子.txt", "r", encoding="utf-8") as f:
#     error_senteces=f.readlines().copy()
# # wordnet = [[""]]
# # forward_cut = []
# # backward_cut = []
# forward_cut = (Match(text=error_senteces[0], dictionary=Dictionary, Forward=True).text_cut(10)[:-1])
# backward_cut = (Match(text=error_senteces[0], dictionary=Dictionary, Forward=False).text_cut(10)[:-1])
# print(forward_cut)
# print(backward_cut)
# wordnet = WordNet()
