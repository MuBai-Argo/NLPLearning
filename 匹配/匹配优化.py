import jieba
import pandas
from 正向逆向匹配 import Match, prf, to_Region

text = ""
Dictionary = []
with open("克苏鲁神话-测试语料 黑太岁.txt", "r", encoding="utf-8")as f:
    text += f.read()
# print(text)
with open("Dictionary.txt", "r", encoding="utf-8") as f:
    for i in f.readlines():
        Dictionary.append(i[:-1])
# print(Dictionary)
forward_match = Match(text=text, dictionary=Dictionary, Forward=True)
backward_match = Match(text=text, dictionary=Dictionary, Forward=False)
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
print(text_backward)
print(text_forward)
with open("正向匹配.txt", "w", encoding="utf-8")as f:
    f.write(text_forward)
with open("逆向匹配.txt", "w", encoding="utf-8")as f:
    f.write(text_backward)
"""
    优化结果:
        优化前
            正向匹配准确率：p0.7358371326682617, r0.8515384213550645, f0.7894711352189075
            逆向匹配准确率：p0.7333303236874181, r0.8485608316355848, f0.78674868019567
        优化后
            正向匹配准确率：p0.8529483609360496, r0.9120305072350207, f0.8815005553872565
            逆向匹配准确率：p0.8450752393980848, r0.9035678838217626, f0.87334326323496
"""