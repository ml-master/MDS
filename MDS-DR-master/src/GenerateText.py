import json

# 读取JSON文件并逐行处理
with open('../results2/gossip_doc_cls/test_step10000_test.json', 'r',encoding='utf-8') as file:
    lines = file.readlines()

# 获取特定的一行数据，例如第二行数据
# line_index = 1  # 行索引，从0开始
for line_index in range(len(lines)):
    if line_index < len(lines):
        row_data = json.loads(lines[line_index])
        # print(row_data)
        # print(row_data['src'])
        text_list=row_data['src']
        src_text = ' '.join([text for text in text_list if text != 'unused0'])
        print(src_text)
        with open('../raw_data/gossip_src.txt', 'a', encoding='utf-8') as f:
            f.write(src_text+'\n')

        text_tgt=row_data['tgt']
        text_tgt.replace("<q>", "")
        with open('../raw_data/gossip_tgt.txt', 'a', encoding='utf-8') as f:
            f.write(text_tgt+'\n')

        # 分割src文本
        split_texts = []
        current_text = []
        for text in row_data['src']:
            if text == 'unused0':
                split_texts.append(' '.join(current_text))
                current_text = []
            else:
                current_text.append(text)
        current_text.append('.')
        split_texts.append(' '.join(current_text))


        # 根据src_rank重新排列文本
        ordered_texts = [split_texts[i] for i in row_data['src_rank']]

        # 拼接成一个完整的文本
        src_reorder = ' '.join(ordered_texts)
        print(src_reorder)
        with open('../raw_data/gossip_reorder.txt', 'a', encoding='utf-8') as f:
            f.write(src_reorder+'\n')