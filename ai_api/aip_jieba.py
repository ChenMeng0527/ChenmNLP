'''
jieba工具的功能汇总
'''

import jieba.posseg as pseg
import jieba.analyse

class ApiJieba:
    '''
    jieba类
    '''
    def __init__(self):
        print()


    def cut_word_singal(self, text, wordclasses=None):
        '''
        单个句子分词
        :param text: 文本 string
        :param wordclasses: 词性,为list
        :return:
        '''
        # pseg.cut输出格式: [pair('中华人民共和国', 'ns'), pair(',', 'x'),
        text = list(pseg.cut(text))
        if wordclasses:
            result = [word for word, wc in text if wc in wordclasses]
        else:
            result = [word for word, wc in text]
        return result


    def cut_word_batch(self, text_list, wordclasses=None):
        '''
        批量切词
        :param text_list: list文本集合
        :param wordclasses: 词性
        :return:
        '''
        print('xxx')


    def get_key_word(self, text, model, topK, withWeight=True):
        '''
        关键词
        :param text: 文本,string,不支持list
        :param model: tf-idf or textrank
        :param topK: 返回最大K个
        :param withWeight: True  返回[('玄德', 0.1038549799467099), ('程远志', 0.07787459004363208),
                           False 返回 ['玄德', '程远志', '张角', '云长'
        :return:
        '''
        if model == 'tfidf':
            return jieba.analyse.extract_tags(text, topK=topK, withWeight=withWeight)
        if model == 'textrank':
            return jieba.analyse.textrank(text, topK=topK, withWeight=withWeight)


if __name__ == '__main__':
    apijieba = ApiJieba()
    TEXT = '中华人民共和国,你为什么这么爱吃雪糕'
    print(apijieba.cut_word_singal(TEXT, wordclasses=['n']))
    print(apijieba.get_key_word(TEXT, model='tfidf', topK=3))