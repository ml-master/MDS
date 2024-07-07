



with open('../raw_data_gbk/raw_src.txt', 'r',encoding='gbk') as file:
    lines = file.readlines()

# 获取特定的一行数据，例如第二行数据
# line_index = 1  # 行索引，从0开始
for line_index in range(len(lines)):
    text=lines[line_index]
    # Split the text into sentences
    sentences = text.split('. ')

    # Join sentences with '[CLS] [SEP]' in between
    processed_text = ' . [CLS] [SEP] '.join(sentences)

    with open('../raw_data_gbk/raw_src_ext.txt', 'a', encoding='gbk') as f:
        f.write(processed_text )


    print(processed_text)
