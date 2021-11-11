from 匹配模型 import Match, Dictionary
from 语料库 import Two_Gram
error_cut = []
forward_cut = []
backward_cut = []
final_choose = []
with open("./Script/歧义句子.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        error_cut.append(i[:-1])
for sentence in error_cut:
    forward_cut.append(Match(sentence, True, Dictionary).text_cut(10))
    backward_cut.append(Match(sentence, False, Dictionary).text_cut(10))
# 加载二元语法模型
two_gram = Two_Gram()
for forward, backward in zip(forward_cut, backward_cut):
    forward_score = two_gram.two_gram_model(forward)
    backward_score = two_gram.two_gram_model(backward)
    print(f"正向二元语法概率{forward_score}")
    print(f"逆向二元语法概率{backward_score}")
    print(forward)
    print(backward)
    if forward_score >= backward_score:
        print("选择正向")

        final_choose.append(" ".join(forward))
    else:
        print("选择逆向")

        final_choose.append(" ".join(backward))
    print()
# 输出选择的分词方式
with open("./Script/消歧结果.txt", "w", encoding="utf-8") as f:
    for i in final_choose:
        f.writelines(i)
        f.writelines("\n")

