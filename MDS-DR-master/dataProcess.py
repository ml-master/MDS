import json

def read_json_file(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)
  return data
# 假设第二个JSON格式的数据已经被加载到data变量中
json_file_path = './json_data2/gossip/valid.0.json'
data = read_json_file(json_file_path)

# 将第二个JSON格式转换为第一个JSON格式
def convert_format(story):
    new_src = []
    new_tgt = []

    # 遍历原始的src和tgt列表
    for src_paragraph in story["src"]:
        # 将每个段落的单词列表转换为一个嵌套数组，并添加到new_src
        new_src.append(src_paragraph)

    for tgt_sentence in story["tgt"]:
        # 将每个句子的单词列表转换为一个嵌套数组，并添加到new_tgt
        new_tgt.append(tgt_sentence)

    # 返回转换后的故事格式
    return {
        "src": new_src,
        "tgt": new_tgt,
        "id": story["id"]
    }


# 应用转换函数到每个故事
converted_data = [convert_format(story) for story in data]

# 将转换后的数据输出为JSON字符串
json_output = json.dump(converted_data, indent=2, ensure_ascii=False)
with open('./json_data2/gossip/valid.0.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_output)

print(json_output)