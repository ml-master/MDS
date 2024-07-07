import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
import json

# 假设文件名为 'example.txt'，你需要替换成你的文件路径
file_src = 'train_src.txt'
file_tgt = 'train_tgt.txt'

new_json = []
# 使用with语句打开文件，确保之后文件会被正确关闭
with open(file_src, 'r', encoding='utf-8') as file, \
     open(file_tgt, 'r', encoding='utf-8') as file2:

    for line_number, (line1, line2) in enumerate(zip(file, file2), start=1):
        new_scentences = []
        tgt_scentences = []
        # 根据"||||"进行文本分割
        parts = line1.split("|||||")
        print(len(parts))

        sentences_re = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s+(?=[A-Z])|(?<=\.\s)')
        sentences_tgt=sentences_re.split(line2)
        nltk.download('punkt')
        # 遍历分割后的文本部分，并将每个部分保存为单独的文档

        #处理src数据
        for i, part in enumerate(parts):
            # 去除每个部分的首尾空白字符
            part = part.strip()


            if part:  # 确保不保存空的文档
                # 将每个部分保存为一个文本文件
                sentences = sentences_re.split(part)
                if i != len(parts)-1:
                    sentences.append("unused0")
                for sentences in sentences:
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
                    new_scentences.append(replaced_words)


        #处理好的src
        new_scentences=[s for s in new_scentences if s and 'NEWLINE_CHAR'  not in s]

        #处理tgt
        for sentences in sentences_tgt:
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
            tgt_scentences.append(replaced_words)
        # # 创建新的JSON对象

        tgt_scentences = [s for s in tgt_scentences if s]
        new_json_data = {
                  "src": new_scentences,
                  "tgt": tgt_scentences,
                  "id": line_number
            }
        new_json.append(new_json_data)
        # 将新的JSON对象转换为JSON格式的字符串
# new_json_str = json.dumps(new_json, indent=2, ensure_ascii=False)
with open("./json_data/train.json", 'w',encoding="utf-8") as f:
    # f.write(new_json_str)
    for chunk in json.JSONEncoder().iterencode(new_json):
        f.write(chunk)
print("所有文档已保存完毕。")



'''
GOP Eyes Gains As Voters In 11 States Pick Governors NEWLINE_CHAR NEWLINE_CHAR Enlarge this image toggle caption Jim Cole/AP Jim Cole/AP NEWLINE_CHAR NEWLINE_CHAR Voters in 11 states will pick their governors tonight, and Republicans appear on track to increase their numbers by at least one, with the potential to extend their hold to more than two-thirds of the nation's top state offices. NEWLINE_CHAR NEWLINE_CHAR Eight of the gubernatorial seats up for grabs are now held by Democrats; three are in Republican hands. Republicans currently hold 29 governorships, Democrats have 20, and Rhode Island's Gov. Lincoln Chafee is an Independent. NEWLINE_CHAR NEWLINE_CHAR Polls and race analysts suggest that only three of tonight's contests are considered competitive, all in states where incumbent Democratic governors aren't running again: Montana, New Hampshire and Washington. NEWLINE_CHAR NEWLINE_CHAR While those state races remain too close to call, Republicans are expected to wrest the North Carolina governorship from Democratic control, and to easily win GOP-held seats in Utah, North Dakota and Indiana. NEWLINE_CHAR NEWLINE_CHAR Democrats are likely to hold on to their seats in West Virginia and Missouri, and are expected to notch safe wins in races for seats they hold in Vermont and Delaware. NEWLINE_CHAR NEWLINE_CHAR Holding Sway On Health Care NEWLINE_CHAR NEWLINE_CHAR While the occupant of the governor's office is historically far less important than the party that controls the state legislature, top state officials in coming years are expected to wield significant influence in at least one major area. NEWLINE_CHAR NEWLINE_CHAR And that's health care, says political scientist Thad Kousser, co-author of The Power of American Governors. NEWLINE_CHAR NEWLINE_CHAR "No matter who wins the presidency, national politics is going to be stalemated on the Affordable Care Act," says Kousser, of the University of California, San Diego. NEWLINE_CHAR NEWLINE_CHAR A recent U.S. Supreme Court decision giving states the ability to opt out of the law's expansion of Medicaid, the federal insurance program for poor, disabled and elderly Americans, confers "incredible power" on the states and their governors, Kousser says. NEWLINE_CHAR NEWLINE_CHAR Just look at what happened when the Obama administration in 2010 offered federal stimulus money to states to begin building a high-speed rail network. Three Republican governors, including Rick Scott of Florida and Scott Walker of Wisconsin, rejected a share of the money citing debt and deficit concerns. NEWLINE_CHAR NEWLINE_CHAR "A [Mitt] Romney victory would dramatically empower Republican governors," Kousser says. NEWLINE_CHAR NEWLINE_CHAR State-By-State View NEWLINE_CHAR NEWLINE_CHAR North Carolina: One-term incumbent Democratic Gov. Beverly Perdue, the first woman to hold the state's top office, announced in January that she would not seek re-election after polls showed her with high disapproval ratings and trailing Republican candidate Pat McCrory. NEWLINE_CHAR NEWLINE_CHAR The seat is expected to be won by McCrory, a former Charlotte mayor, who is facing Perdue's lieutenant governor, Walter Dalton. McCrory lost a close race to Perdue in 2008, when then-presidential candidate Barack Obama became the first Democrat to win North Carolina in more than three decades. The Real Clear Politics average for the race has McCrory maintaining a 14.3 percentage point lead. NEWLINE_CHAR NEWLINE_CHAR Montana: Popular Democratic Gov. Brian Schweitzer — he won his last election with 65 percent of the vote — has reached his two-term limit. The state's Democratic Attorney General Steve Bullock is trying to keep the seat in his party's column by associating himself with Schweitzer's legacy. He's in a tough race with former two-term GOP Rep. Rick Hill. NEWLINE_CHAR NEWLINE_CHAR New Hampshire: Former Democratic state Sen. Maggie Hassan has also promised a continuation of the policies of her predecessor, retiring Democratic Gov. John Lynch. Her opponent is lawyer Ovide Lamontagne, a Tea Party conservative who ran unsuccessfully for governor in 1996 and for the U.S. Senate in 2010. The national parties have invested in the campaigns, which have focused on fiscal and women's health care issues. NEWLINE_CHAR NEWLINE_CHAR Washington: The state's governorship has been in Democratic hands for 32 years, and former U.S. Rep. Jay Inslee is in a dead-heat battle to keep it that way. His opponent is the state's Republican Attorney General Rob McKenna. McKenna has a proven ability to win statewide, but working in Inslee's favor are Obama's poll numbers. The Real Clear Politics average shows Obama with an average 13.6 percentage point lead over Romney; Inslee is leading McKenna by an average of 1 percentage point. NEWLINE_CHAR NEWLINE_CHAR Pretty Much Sure Things NEWLINE_CHAR NEWLINE_CHAR Republican Govs. Jack Dalrymple in North Dakota and Gary Herbert in Utah, and GOP Rep. Mike Pence in Indiana are expected to win. So are Democratic Govs. Peter Shumlin in Vermont and Jack Markell in Delaware. NEWLINE_CHAR NEWLINE_CHAR Democrats are also hoping to hold on to the governorship in Missouri, where Jay Nixon is running for a second term against Republican Dave Spence; and in West Virginia, where Gov. Earl Ray Tomblin, former state senate president, is running for his first full term after winning a special election in 2011. GOP businessman Bill Maloney is his opponent, as he was last year. NEWLINE_CHAR NEWLINE_CHAR Nixon has been consistently outpolling Spence by an average of about 7 points in Missouri. Tomblin is seen as likely to retain his seat, even in a state where Romney is leading Obama by double digits. ||||| GOP Eyes Gains As Voters In 11 States Pick Governors NEWLINE_CHAR NEWLINE_CHAR Jim Cole / AP i Jim Cole / AP NEWLINE_CHAR NEWLINE_CHAR Voters in 11 states will pick their governors tonight, and Republicans appear on track to increase their numbers by at least one, and with the potential to extend their hold to more than two-thirds of the nation's top state offices. NEWLINE_CHAR NEWLINE_CHAR Eight of the gubernatorial seats up for grabs today are now held by Democrats; three are in Republican hands. Republicans currently hold 29 governorships, Democrats have 20; and Rhode Island's Gov. Lincoln Chafee is an Independent. NEWLINE_CHAR NEWLINE_CHAR Polls and race analysts suggest that only three of tonight's contests are considered competitive, all in states where incumbent Democratic governors aren't running again: Montana, New Hampshire and Washington. NEWLINE_CHAR NEWLINE_CHAR While those state races remain too close to call, Republicans are expected to wrest the North Carolina governorship from Democratic control, and to easily win GOP-held seats in Utah, North Dakota and Indiana. NEWLINE_CHAR NEWLINE_CHAR Democrats are likely hold on to their seats in West Virginia and Missouri; and expected to notch safe wins in races for seats they hold in Vermont and Delaware. NEWLINE_CHAR NEWLINE_CHAR Holding Sway On Health Care NEWLINE_CHAR NEWLINE_CHAR While the occupant of the governor's office is historically far less important than the party that controls the state legislature, top state officials in coming years are expected to wield significant influence in at least one major area. NEWLINE_CHAR NEWLINE_CHAR And that's health care, says political scientist Thad Kousser, co-author of The Power of American Governors. NEWLINE_CHAR NEWLINE_CHAR "No matter who wins the presidency, national politics is going to be stalemated on the Affordable Care Act," says Kousser, of the University of California-Berkeley. NEWLINE_CHAR NEWLINE_CHAR A recent U.S. Supreme Court decision giving states the ability to opt out of the law's expansion of Medicaid, the federal insurance program for poor, disabled and elderly Americans, confers "incredible power" on the states and their governors, Kousser says. NEWLINE_CHAR NEWLINE_CHAR Just look at what happened when the Obama administration in 2010 offered federal stimulus money to states to begin building a high-speed rail network. Three Republican governors, including Rick Scott of Florida and Scott Walker of Wisconsin, rejected a share of the money citing debt and deficit concerns. NEWLINE_CHAR NEWLINE_CHAR "A [Mitt] Romney victory would dramatically empower Republican governors," Kousser says. NEWLINE_CHAR NEWLINE_CHAR State-by-State View NEWLINE_CHAR NEWLINE_CHAR North Carolina: One-term incumbent Democratic Gov. Beverly Perdue, the first woman to hold the state's top office, announced in January she would not seek re-election after polls showed her with high disapproval ratings and trailing Republican candidate Pat McCrory. NEWLINE_CHAR NEWLINE_CHAR The seat is expected to be won by McCrory, a former Charlotte mayor, who is facing Perdue's lieutenant governor, Walter Dalton. McCrory lost a close race to Perdue in 2008, when then-presidential candidate Barack Obama became the first Democrat to win North Carolina in more than three decades. The Real Clear Politics average for the race has McCrory maintaining a 14.3 percentage point lead. NEWLINE_CHAR NEWLINE_CHAR Montana: Popular Democratic Gov. Brian Schweitzer — he won his last election with 65 percent of the vote — has reached his two-term limit. The state's Democratic Attorney General Steve Bullock is trying to keep the seat in his party's column by associating himself with Schweitzer's legacy. He's in a tough race with former two-term GOP Rep. Rick Hill. NEWLINE_CHAR NEWLINE_CHAR New Hampshire: Former Democratic state Sen. Maggie Hassan has also promised a continuation of the policies of her predecessor, retiring Democratic Gov. John Lynch. Her opponent is lawyer Ovide Lamontagne, a Tea Party conservative who ran unsuccessfully for governor in 1996 and for the U.S. Senate in 2010. The national parties have invested in the campaigns, which have focused on fiscal and women's health care issues. NEWLINE_CHAR NEWLINE_CHAR Washington: The state's governorship has been in Democratic hands for 32 years, and former Rep. Jay Inslee is in a dead-heat battle to keep it that way. His opponent is the state's Republican Attorney General Rob McKenna. McKenna has a proven ability to win statewide, but working in Inslee's favor are Obama's poll numbers. The Real Clear Politics average shows Obama with an average 13.6 point lead over Romney; Inslee's leading McKenna by an average of 1 percentage point. NEWLINE_CHAR NEWLINE_CHAR Pretty Much Sure Things NEWLINE_CHAR NEWLINE_CHAR Republican governors Jack Dalrymple in North Dakota and Gary Herbert in Utah, and GOP Rep. Mike Pence in Indiana are expected to win. So are Democratic governors Peter Shumlin in Vermont and Jack Markell in Delaware. NEWLINE_CHAR NEWLINE_CHAR Democrats are also hoping to hold on to the governorship in Missouri, where Jay Nixon is running for a second term against Republican Dave Spence; and in West Virginia, where Gov. Earl Ray Tomblin, former state senate president, is running for his first full term after willing a special election in 2011. GOP businessman Bill Maloney is his opponent, as he was last year. NEWLINE_CHAR NEWLINE_CHAR Nixon has been consistently out-polling Spence by an average of about 7 points in Missouri. Tomblin is seen as likely to retain his seat, even in a state where Romney is leading Obama by double digits.

'''