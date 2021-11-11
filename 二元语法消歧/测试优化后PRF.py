import jieba

from 匹配模型 import to_Region, prf

text = ""
text_ori = ""
with open("./Script/二元语法消歧结果.txt", "r", encoding="utf-8")as f:
    text += f.read()
with open("./Script/原始语料.txt", "r", encoding="utf-8") as f:
    text_ori += f.read()
print(text)
standard_region = to_Region(" ".join(jieba.cut(text_ori)))
result_region = to_Region(text)
p, r, f = prf(standard_region, result_region)
print(f"经二元语法消歧后：\n P = {p}, R = {r}, F = {f}")
with open("./Script/jieba分词结果.txt", "w", encoding="utf-8")as f:
    f.write(" ".join(jieba.cut(text_ori)))



"""
消歧前：
    优化结果:
        优化前
            正向匹配准确率：p.7358371326682617, r0.8515384213550645, f0.7894711352189075
            逆向匹配准确率：p.7333303236874181, r0.8485608316355848, f0.78674868019567
        优化后
            正向匹配准确率：p 0.8529483609360496, r 0.9120305072350207, f 0.8815005553872565
            逆向匹配准确率：p 0.8450752393980848, r 0.9035678838217626, f 0.87334326323496
经二元语法消歧后：
                          P = 0.8498499951611342, R = 0.9174633025126678, F = 0.8823632846843679
"""
