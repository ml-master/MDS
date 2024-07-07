import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
import json
# 指定Parquet文件的路径
file_path = './test-00000-of-00001-89390a11db7c6013.parquet'

# 读取Parquet文件
df = pd.read_parquet(file_path)
new_scentences = []
tgt_scentences = []
text=df.iloc[2]['document']

print(text)

# 根据"|||||"进行文本分割
parts = text.split("|||||")

sentences_re = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s+(?=[A-Z])|(?<=\.\s)')
nltk.download('punkt')
# 遍历分割后的文本部分，并将每个部分保存为单独的文档

for i, part in enumerate(parts):
    # 去除每个部分的首尾空白字符
    part = part.strip()

    if part:  # 确保不保存空的文档
        # 将每个部分保存为一个文本文件
        sentences = sentences_re.split(part)
        if part != len(parts):
            sentences.append("unused0")
        for sentences in sentences:
            # print(sentences)
            words = word_tokenize(sentences)
            # 输出结果
            new_scentences.append(words)
        with open(f"document_{i+1}.txt", "w", encoding="utf-8") as file:
            file.write(part)

new_scentences=[s for s in new_scentences if s]
new_json_data = {
          "src": new_scentences,
          "tgt":tgt_scentences,
          "id": 1
    }
new_json=[]
new_json.append(new_json_data)
# 将新的JSON对象转换为JSON格式的字符串
# new_json_str = json.dumps(new_json, indent=2, ensure_ascii=False)
with open("json_data2/multinew/test.0.json", 'w', encoding="utf-8") as f:
    # f.write(new_json_str)
    for chunk in json.JSONEncoder().iterencode(new_json):
        f.write(chunk)
print("所有文档已保存完毕。")
# # 查看数据框的前几行内容
# print(df.head())
#
# # 如果需要查看数据的统计信息，可以使用describe()方法
# print(df.describe())