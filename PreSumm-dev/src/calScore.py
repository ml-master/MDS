from rouge_score import rouge_scorer

def read_file(file_path):
    with open(file_path, 'r', encoding='gbk') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def calculate_rouge_scores(reference_summaries, generated_summaries):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = []
    for ref, gen in zip(reference_summaries, generated_summaries):
        score = scorer.score(ref, gen)
        scores.append(score)
    return scores

def main(reference_file, generated_file,output_file):
    reference_summaries = read_file(reference_file)
    generated_summaries = read_file(generated_file)

    print(len(reference_summaries))
    print(len(generated_summaries))

    if len(reference_summaries) != len(generated_summaries):
        print("两个文件的行数不匹配。")
        return

    rouge_scores = calculate_rouge_scores(reference_summaries, generated_summaries)

    ROUGE_1_p=0
    ROUGE_2_p=0
    ROUGE_L_p=0
    ROUGE_1_r=0
    ROUGE_2_r=0
    ROUGE_L_r=0
    ROUGE_1_f=0
    ROUGE_2_f=0
    ROUGE_L_f=0

    count=0
    for i, score in enumerate(rouge_scores):
        # count+=1
        # if count==1475:
        #     break
        ROUGE_1_p+=score['rouge1'][0]
        ROUGE_2_p+=score['rouge2'][0]
        ROUGE_L_p+=score['rougeL'][0]
        ROUGE_1_r+=score['rouge1'][1]
        ROUGE_2_r+=score['rouge2'][1]
        ROUGE_L_r+=score['rougeL'][1]
        ROUGE_1_f+=score['rouge1'][2]
        ROUGE_2_f+=score['rouge2'][2]
        ROUGE_L_f+=score['rougeL'][2]

        # print(f"摘要 {i+1} 的 ROUGE 分数：")
        # print(f"ROUGE-1: {score['rouge1']}")
        # print(f"ROUGE-2: {score['rouge2']}")
        # print(f"ROUGE-L: {score['rougeL']}")
        # print()

    # ROUGE_1_p = ROUGE_1_p / count
    # ROUGE_2_p = ROUGE_2_p / count
    # ROUGE_L_p = ROUGE_L_p / count
    # ROUGE_1_r = ROUGE_1_r / count
    # ROUGE_2_r = ROUGE_2_r / count
    # ROUGE_L_r = ROUGE_L_r / count
    # ROUGE_1_f = ROUGE_1_f / count
    # ROUGE_2_f = ROUGE_2_f / count
    # ROUGE_L_f = ROUGE_L_f / count
    ROUGE_1_p=ROUGE_1_p/len(rouge_scores)
    ROUGE_2_p=ROUGE_2_p/len(rouge_scores)
    ROUGE_L_p=ROUGE_L_p/len(rouge_scores)
    ROUGE_1_r=ROUGE_1_r/len(rouge_scores)
    ROUGE_2_r=ROUGE_2_r/len(rouge_scores)
    ROUGE_L_r=ROUGE_L_r/len(rouge_scores)
    ROUGE_1_f=ROUGE_1_f/len(rouge_scores)
    ROUGE_2_f=ROUGE_2_f/len(rouge_scores)
    ROUGE_L_f=ROUGE_L_f/len(rouge_scores)
    # print(f"ROUGE-1-r: {ROUGE_1_r}")

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("整个数据集的平均 ROUGE 分数：\n")
        file.write(
            f"ROUGE-1: P:{ROUGE_1_p}, R: {ROUGE_1_r}, F:{ROUGE_1_f}\n")
        file.write(
            f"ROUGE-2: P:{ROUGE_2_p}, R: {ROUGE_2_r}, F: {ROUGE_2_f}\n")
        file.write(
            f"ROUGE-L: P: {ROUGE_L_p}, R: {ROUGE_L_r}, F: {ROUGE_L_f}\n")

# 示例用法
reference_file = '../results/reorder_ext_multinew_step-1.gold'
generated_file = '../results/reorder_ext_multinew_step-1.candidate'
output_file = 'multinew_reorder_rouge.txt'
main(reference_file, generated_file,output_file)

