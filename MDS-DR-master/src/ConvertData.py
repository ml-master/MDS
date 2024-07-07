import json
import re
import nltk
from nltk.tokenize import word_tokenize

'''
 {
    "src": [
      "national archives yes , it's that time again , folks .",
      "it's the first friday of the month , when for one ever-so-brief moment the interests of wall street , washington and main street are all aligned on one thing : jobs .",
      "a fresh update on the u.s. employment situation for january hits the wires at 8:30 a.m. new york time offering one of the most important snapshots on how the economy fared during the previous month .",
      "expectations are for 203,000 new jobs to be created , according to economists polled by dow jones newswires , compared to 227,000 jobs added in february .",
      "the unemployment rate is expected to hold steady at 8.3 % .",
      "here at marketbeat hq , we'll be offering color commentary before and after the data crosses the wires .",
      "feel free to weigh-in yourself , via the comments section .",
      "and while you're here , why don't you sign up to .",
      "unused0",
      "employers pulled back sharply on hiring last month , a reminder that the u.s. economy may not be growing fast enough to sustain robust job growth .",
      "the unemployment rate dipped , but mostly because more americans stopped looking for work .",
      "the labor department says the economy added 120,000 jobs in march , down from more than 200,000 in each of the previous three months .",
      "the unemployment rate fell to 8.2 percent , the lowest since january 2009.",
      "the rate dropped because fewer people searched for jobs .",
      "the official unemployment tally only includes those seeking work .",
      "the economy has added 858,000 jobs since december _ the best four months of hiring in two years .",
      "but federal reserve chairman ben bernanke has cautioned that the current hiring pace is unlikely to continue without more consumer spending ."
    ],
    "tgt": [
      "the unemployment rate dropped to 8.2 % last month , but the economy only added 120,000 jobs , when 203,000 new jobs had been predicted , according to today's jobs report .",
      "reaction on the wall street journal's marketbeat blog was swift : 'woah !'",
      "'!!'",
      "bad number .",
      "the unemployment rate , however , is better news ; it had been expected to hold steady at 8.3 % .",
      "but the ap notes that the dip is mostly due to more americans giving up on seeking employment ."
    ],
    "id": "0.story.json"
  },
'''

def read_json_file(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
  return data


# 假设json_file_path是包含JSON文件路径的字符串
json_file_path = '../gossipcop_v3-7_integration_based_legitimate_tn300.json'
data = read_json_file(json_file_path)
id_keys = data.keys()

# 将 dict_keys 对象转换为 list
id_keys_list = list(id_keys)


# 现在 id_keys_list 是一个 list，可以进行索引和切片操作
print(type(id_keys_list))  #


sentences_re = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s+(?=[A-Z])|(?<=\.\s)')
# 确保已经下载了nltk的分词器
nltk.download('punkt')
new_json=[]
for key in id_keys_list:
    new_sentences = []
    tgt_sentences = []
    row_data=data[key]
    # 使用正则表达式分割文本
    # 分割第一段文本
    sentences1 = sentences_re.split(row_data['doc_1_text'])
    # sentences1 = sentences_re.split( "national archives yes , it's that time again , folks . it's the first friday of the month , when for one ever-so-brief moment the interests of wall street , washington and main street are all aligned on one thing : jobs .")
    # print(sentences1)
    # 分割第二段文本
    sentences2 = sentences_re.split(row_data['doc_2_text'])
    # sentences2 = sentences_re.split("employers pulled back sharply on hiring last month , a reminder that the u.s. economy may not be growing fast enough to sustain robust job growth . the unemployment rate dipped , but mostly because more americans stopped looking for work .")

    sentences3=sentences_re.split(row_data["generated_text_t01"])
    # 在两个列表中适当位置插入“unused0”
    sentences1.append("unused0")  # 在第一个列表的末尾插入



    for sentences in sentences1:
        # print(sentences)
        words = word_tokenize(sentences)
        replaced_words = []
        for word in words:
            if word == "'s":
                replaced_words.append('\u2019')
                replaced_words.append('s')

            elif word == "'m":
                replaced_words.append('\u2019')
                replaced_words.append('m')

            elif word == "'t":
                replaced_words.append('\u2019')
                replaced_words.append('t')

            elif word == "'re":
                replaced_words.append('\u2019')
                replaced_words.append('re')

            else:
                replaced_words.append(word)
        # 输出结果
        new_sentences.append(replaced_words)


    for sentences in sentences2:
        # print(sentences)
        words = word_tokenize(sentences)
        replaced_words = []
        for word in words:
            if word == "'s":
                replaced_words.append('\u2019')
                replaced_words.append('s')

            elif word == "'m":
                replaced_words.append('\u2019')
                replaced_words.append('m')

            elif word == "'t":
                replaced_words.append('\u2019')
                replaced_words.append('t')

            elif word == "'re":
                replaced_words.append('\u2019')
                replaced_words.append('re')

            else:
                replaced_words.append(word)
        # 输出结果
        new_sentences.append(replaced_words)

    new_sentences=[s for s in new_sentences if s]




    for sentences in sentences3:
        # print(sentences)
        words = word_tokenize(sentences)
        replaced_words = []
        for word in words:
            if word == "'s":
                replaced_words.append('\u2019')
                replaced_words.append('s')

            elif word == "'m":
                replaced_words.append('\u2019')
                replaced_words.append('m')

            elif word == "'t":
                replaced_words.append('\u2019')
                replaced_words.append('t')

            elif word == "'re":
                replaced_words.append('\u2019')
                replaced_words.append('re')

            else:
                replaced_words.append(word)
        # 输出结果
        tgt_sentences.append(replaced_words)
    # # 创建新的JSON对象

    tgt_sentences=[s for s in tgt_sentences if s]

    new_json_data = {
          "src": new_sentences,
          "tgt":tgt_sentences,
          "id": key
    }
    new_json.append(new_json_data)
# 将新的JSON对象转换为JSON格式的字符串
# new_json_str = json.dumps(new_json, indent=2, ensure_ascii=False)
with open("../json_data2/gossip/test.0.json", 'w',encoding="utf-8") as f:
    # f.write(new_json_str)
    for chunk in json.JSONEncoder().iterencode(new_json):
        f.write(chunk)
# print(new_json_str)

