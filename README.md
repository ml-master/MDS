# MDS
多文档摘要生成-文档重排序复现实验
复现论文：Read Top News First: A Document Reordering Approach for Multi-Document News Summarization

## Structure

* MDS-DR-master文件夹是本论文重排序的代码，具体运行设置请参考该目录下的README.md文件。
  
* PreSumm-dev文件夹是论文中使用的摘要生成模型，将排序前和排序后的元文档在此进行摘要生成处理和ROUGE分数计算，具体运行设置请参考该目录下的README.md文件。
  
* Result文件夹是复现实验得到的结果整理，其中包括generated_summarization(PreSumm模型对未排序和排序后的元文档生成的摘要)、reorder（对实验数据集重排序的结果）、ROUGE（对数据集生成的摘要进行ROUGE分数计算）

## DataSets
复现数据集包括原论文实验数据集multinews和课程提供数据集GossipCop

MDS-DR-master需要的数据可以通过下面链接下载后放在目录\MDS-DR-master\bert_data2\
获取链接：https://drive.google.com/drive/folders/1d8VZ-TuPdQm3zkB5MwjnKhm_Xt0Z2DOe?usp=drive_link

MDS-DR-master生成的排序结果放在\MDS-DR-master\results2\

PreSumm-dev需要的数据已处理好放在目录\PreSumm-dev\raw_data_gbk\

PreSumm-dev生成的摘要结果放在\PreSumm-dev\results\

## Models
论文提供的源码没有提供训练好的模型，本人训练好的模型包括重排序模型和摘要生成模型。

本人训练好的模型下载https://drive.google.com/drive/folders/1Q4yjoCZYh-sN_mlCLa6mv3iFCWXKaiyH?usp=drive_link

重排序模型为model_step_10000.pt

摘要生成模型为model_step_30000.pt

重排序模型放在\MDS-DR-master\models2\multinew_doc_cls\

摘要生成模型放在\PreSumm-dev\models\PreSumm\

## Run
1、对多文档数据进行排序（以multinews数据集为例）

```bash
cd ./MDS-DR-master/src
python train.py  -task ext -mode test_doc -input test -batch_size 1000 -test_batch_size 5 \
-bert_data_path ../bert_data2/multinew_doc_cls/ -log_file ../logs/multinews.log \
-model_path ../models/multinew_doc_cls -test_from ../models/multinew_doc_cls/model_step_10000.pt -sep_optim true \
-use_interval true -visible_gpus 1 -max_pos 512 -max_length 200 -alpha 0.95 -min_length 50 \
-result_path ../results2/multinew_doc_cls/test
```

2、生成摘要（以重排序后的multinews数据集为例）

```bash
cd ./PreSumm-dev/src
python train.py -task ext -mode test_text -text_src ../raw_data_gbk/multinews_src_reorder.txt -text_tgt ../raw_data_gbk/multinews_tgt.txt -test_from ../models/PreSumm/model_step_30000.pt -result_path ../results/reorder_ext_multinew
```

3、ROUGE评分计算
```bash
cd ./PreSumm-dev/src
python calScore.py
```

## Result

复现结果

![image](https://github.com/ml-master/MDS-DR/assets/79297614/03d1dd27-58a9-4940-93ad-31f8d293644a)

