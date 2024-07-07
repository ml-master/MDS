# from rouge_score import rouge_scorer
#
# def read_file(file_path):
#     with open(file_path, 'r', encoding='gbk') as file:
#         lines = file.readlines()
#     return [line.strip() for line in lines]
#
# def calculate_rouge_scores(reference_summaries, generated_summaries):
#     scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
#     scores = []
#     for ref, gen in zip(reference_summaries, generated_summaries):
#         score = scorer.score(ref, gen)
#         scores.append(score)
#     return scores
#
# def main(reference_file, generated_file1,generated_file2,output_file):
#     reference_summaries = read_file(reference_file)
#     #未排序
#     generated_summaries1 = read_file(generated_file1)
#     #排序后
#     generated_summaries2 = read_file(generated_file2)
#
#     #
#     # print("start cal")
#     # rouge_scores1 = calculate_rouge_scores(reference_summaries, generated_summaries1)
#     # rouge_scores2 = calculate_rouge_scores(reference_summaries, generated_summaries2)
#     # print("end cal")
#     #
#     #
#     # ROUGE_1_f=0
#     # ROUGE_1_f_r=0
#     # ROUGE_2_f=0
#     # ROUGE_2_f_r=0
#     # ROUGE_L_f=0
#     # ROUGE_L_f_r=0
#     # result=0;
#     # for i in range(len(rouge_scores2)):
#     #     print(i)
#     #     if (rouge_scores2[i]['rouge1'][2] > rouge_scores1[i]['rouge1'][2] and
#     #             rouge_scores2[i]['rouge2'][2] > rouge_scores1[i]['rouge2'][2] and
#     #             rouge_scores2[i]['rougeL'][2] > rouge_scores1[i]['rougeL'][2]):
#     #         result=i
#     #         break
#
#     write_example(reference_file,generated_file1,generated_file2,output_file,28)
#
#
# def write_example(reference_file, generated_file1, generated_file2, output_file, index):
#     """
#     从三个文件中读取第 index 条数据，并将其写入输出文件 example 中。
#
#     :param reference_file: 参考文件路径
#     :param generated_file1: 生成文件1的路径
#     :param generated_file2: 生成文件2的路径
#     :param output_file: 输出文件路径
#     :param index: 要提取的数据索引（从0开始）
#     """
#     with open(reference_file, 'r', encoding='gbk') as ref_file, \
#             open(generated_file1, 'r', encoding='gbk') as gen_file1, \
#             open(generated_file2, 'r', encoding='gbk') as gen_file2, \
#             open(output_file, 'w', encoding='utf-8') as out_file:
#
#         # 读取所有行
#         ref_lines = ref_file.readlines()
#         gen1_lines = gen_file1.readlines()
#         gen2_lines = gen_file2.readlines()
#
#         # 检查索引是否在范围内
#         if index < len(ref_lines) and index < len(gen1_lines) and index < len(gen2_lines):
#             ref_data = ref_lines[index].strip()
#             gen1_data = gen1_lines[index].strip()
#             gen2_data = gen2_lines[index].strip()
#
#             # 将数据写入输出文件
#             out_file.write(f"Reference: {ref_data}\n")
#             out_file.write(f"Generated1: {gen1_data}\n")
#             out_file.write(f"Generated2: {gen2_data}\n")
#         else:
#             print("索引超出范围")
#
# # 示例用法
# reference_file = '../results/ext_gossip_step-1.gold'
# generated_file1 = '../results/ext_gossip_step-1.candidate'
# generated_file2= '../results/reorder_ext_gossip_step-1.candidate'
# output_file = 'gossip_example.txt'
# main(reference_file , generated_file1, generated_file2, output_file)
#
from rouge_score import rouge_scorer

reference = "in the recent film girls trip , the character dina , played by tiffany haddish , demonstrated an oral sex technique called `` grapefruiting '' using a grapefruit and a banana as props .<q>this scene has sparked discussions about the technique ’ s realness and has become a viral sensation .<q>grapefruiting was originally popularized in 2014 by viral tutorial videos from auntie angel of angel ’ s erotic solutions .<q>haddish ’ s breakout role in girls trip has also led to her receiving love letters from the film ’ s crew and increased success in comedy shows .<q>additionally , haddish wore an authentic african princess dress to the 2018 oscars , honoring her late father who was from eritrea .<q>she is presenting at her first academy awards and is looking forward to meeting meryl streep and having drinks with whoopi goldberg ."
generated1 = "google girls trip right now , and you 'll see two major—and extremely different—results : first , and most importantly , are the headlines about the film ’ s success at the box office and what that means for more films led by women of color in hollywood ( all good things , hopefully ) . the second ? the grapefruit method , an oral sex technique demonstrated ( hilariously ) by tiffany haddish—without question the breakout star of girls trip . the grapefruit method is n't a new term or something invented by the film–it was actually first popularized back in 2014 by viral tutorial videos from auntie angel of angel ’ s erotic solutions . ( you can see that here . ) but in a scene-stealing moment of the film , haddish ’ s character , dina , demonstrates for her friends the oral sex act while using a grapefruit and a banana as props . since then , the scene has launched many discussions about whether it ’ s for real . the directions , according to dina , are simple : cut off the top and bottom of a room-temperature grapefruit , then cut a hole in the middle of it . place the grapefruit on your partner ’ s member , and then ... well , twist . you can see a portion of it in the clip below : `` grapefruiting is an act of love , '' haddish explained to entertainment weekly in an interview . `` make it mystical and magical . '' it certainly had an effect on-set : jada pinkett smith told ew that haddish started receiving love letters from the crew after filming . `` that ’ s true , '' haddish confirmed . `` somebody bought me something from jared jewelry . all the guys started coming to my comedy shows . '' there ’ s a special meaning behind tiffany haddish ’ s 2018 oscars look . the `` girls trip '' star told e ! ’ s ryan seacrest on the red carpet that the traditional african gown is a nod to her eritrean heritage , where her late father was from . reflecting on her whirlwind year , haddish shared , `` there have been really awesome , really great times and some bad times . my father passed away this year and he ’ s from eritrea . '' she recalled him telling her , `` 'one day you ’ re going to end up at the oscars and when you go , you have to honor your people . ' so i ’ m wearing an eritrean , authentic princess dress . and i ’ m proud of it . '' [ natl ] best moments from the 2018 oscars standout style moments from oscars 2018 heartwarming dedication aside , haddish is presenting at her very first academy awards . the comedienne said she ’ s most looking forward to `` meeting meryl streep and asking her to be my mama , '' adding , `` i ’ m looking forward to having drinks with whoopi goldberg . i ’ m looking forward to doing the 'nae , nae ' with everybody , and i ’ m definitely looking forward to presenting an oscar . ''"
generated2 = "there ’ s a special meaning behind tiffany haddish ’ s 2018 oscars look . the `` girls trip '' star told e ! ’ s ryan seacrest on the red carpet that the traditional african gown is a nod to her eritrean heritage , where her late father was from . reflecting on her whirlwind year , haddish shared , `` there have been really awesome , really great times and some bad times . my father passed away this year and he ’ s from eritrea . '' she recalled him telling her , `` 'one day you ’ re going to end up at the oscars and when you go , you have to honor your people . ' so i ’ m wearing an eritrean , authentic princess dress . and i ’ m proud of it . '' [ natl ] best moments from the 2018 oscars standout style moments from oscars 2018 heartwarming dedication aside , haddish is presenting at her very first academy awards . the comedienne said she ’ s most looking forward to `` meeting meryl streep and asking her to be my mama , '' adding , `` i ’ m looking forward to having drinks with whoopi goldberg . i ’ m looking forward to doing the 'nae , nae ' with everybody , and i ’ m definitely looking forward to presenting an oscar . '' . google girls trip right now , and you 'll see two major—and extremely different—results : first , and most importantly , are the headlines about the film ’ s success at the box office and what that means for more films led by women of color in hollywood ( all good things , hopefully ) . the second ? the grapefruit method , an oral sex technique demonstrated ( hilariously ) by tiffany haddish—without question the breakout star of girls trip . the grapefruit method is n't a new term or something invented by the film–it was actually first popularized back in 2014 by viral tutorial videos from auntie angel of angel ’ s erotic solutions . ( you can see that here . ) but in a scene-stealing moment of the film , haddish ’ s character , dina , demonstrates for her friends the oral sex act while using a grapefruit and a banana as props . since then , the scene has launched many discussions about whether it ’ s for real . the directions , according to dina , are simple : cut off the top and bottom of a room-temperature grapefruit , then cut a hole in the middle of it . place the grapefruit on your partner ’ s member , and then ... well , twist . you can see a portion of it in the clip below : `` grapefruiting is an act of love , '' haddish explained to entertainment weekly in an interview . `` make it mystical and magical . '' it certainly had an effect on-set : jada pinkett smith told ew that haddish started receiving love letters from the crew after filming . `` that ’ s true , '' haddish confirmed . `` somebody bought me something from jared jewelry . all the guys started coming to my comedy shows . ''"

def calculate_rouge_scores(reference, generated):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, generated)
    return scores

rouge_scores1 = calculate_rouge_scores(reference, generated1)
rouge_scores2 = calculate_rouge_scores(reference, generated2)

print("ROUGE scores for Generated1:")
for key, value in rouge_scores1.items():
    print(f"{key}: {value.fmeasure:.4f}")

print("\nROUGE scores for Generated2:")
for key, value in rouge_scores2.items():
    print(f"{key}: {value.fmeasure:.4f}")
