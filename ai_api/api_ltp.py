# coding=utf-8
'''
哈工大ltp工具的功能汇总
https://blog.csdn.net/qq_39309652/article/details/119039924
'''

from ltp import LTP
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

class ApiLtp:
    '''
    ltp类
    '''

    def __init__(self):
        print("------加载ltp成功-----")
        self.ltp = LTP()  # 默认加载 Small 模型


    def cut_word_singal(self, text, if_category=0, if_ner=0, if_dependency=0):
        '''
        根据ltp框架 计算切词后的数据 / 词性数据 / 句法分析 结果
        :param text: 文本
        :param ltp: 哈工大 LPT 模型
        :return: {}
        '''

        result = {}

        # 切词
        seg, hidden = self.ltp.seg([text])
        seg = seg[0]  # ['通话', '质量', '很', '特别', '，', '送货', '及时', '操作', '简单']
        result['cut'] = seg

        if if_category:
            # 词性标注
            pos = self.ltp.pos(hidden)[0]  # ['v', 'n', 'd', 'a', 'wp', 'v', 'a', 'v', 'a']
            result['category'] = pos

        if if_ner:
            # 命名实体
            ner = self.ltp.ner(hidden)
            # tag, start, end = ner[0][0]
            result['ner'] = ner
            ner_word = []
            if len(ner[0])>0:
                for i in ner[0]:
                    start = i[1]
                    end = i[2]
                    if start == end:
                        ner_word.append(seg[start])
                    else:
                        ner_word.append(''.join(seg[start:end+1]))
            result['ner_word'] = ner_word

        if if_dependency:
            # 句法分析
            # ！！！注意：0为空，下标1就是第一个切词
            dependency = self.ltp.dep(hidden)[0]  # [(1, 2, 'SBV'), (2, 0, 'HED'), (3, 2, 'WP'), (4, 5, 'ATT'), (5, 6, 'SBV'), (6, 2, 'COO'), (7, 2, 'WP')]
            result['dependency'] = dependency

        return result


    def cut_sentence_signal(self, text):
        '''
        分句子
        :param text: 可以放一个句子，也可以放入多个
        :return:
        '''
        return self.ltp.sent_split([text])



if __name__ == '__main__':
    apiltp = ApiLtp()

    # TEXT = '你为什么这么爱吃雪糕,乔丹与毛泽东啊,刘德华与张学友'
    TEXT = 'twins是香港殿堂级女子歌唱团体，成员包括蔡卓妍和钟欣潼，她们与2000年签约“英皇娱乐”'
    print(apiltp.cut_sentence_signal(TEXT))
    print(apiltp.cut_word_singal(TEXT, if_category=1, if_ner=1, if_dependency=1))


    # print(apiltp.cut_word_singal(TEXT, wordclasses=['n']))
    # print(apiltp.get_key_word(TEXT, model='tfidf', topK=3))
