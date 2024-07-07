import sys
import io

def convert_utf8_to_gbk(input_file, output_file):
    try:
        # 读取UTF-8编码的文件
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 将内容编码为GBK
        gbk_encoded_content = content.encode('gbk', errors='replace')

        # 写入GBK编码的文件
        with open(output_file, 'wb') as f:
            f.write(gbk_encoded_content)

        print(f"文件已成功从UTF-8编码转换为GBK编码，并保存为 {output_file}")

    except UnicodeDecodeError as e:
        print(f"读取文件时出错: {e}")
    except UnicodeEncodeError as e:
        print(f"写入文件时出错: {e}")

# 示例用法
input_file = '../raw_data/raw_src_reorder.txt'
output_file = '../raw_data_gbk/raw_src_reorder.txt'
convert_utf8_to_gbk(input_file, output_file)
