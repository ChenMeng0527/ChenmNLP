'''
pip install snownlp

SnowNLP，中文语言处理的必备工具
https://zhuanlan.zhihu.com/p/391608286

'''

from snownlp import SnowNLP
from snownlp.classification.bayes import Bayes

class ApiSnow:
    '''
    apiSnow
    '''
    def __init__(self):
        self.s = SnowNLP
        pass

    def cut_word_singal(self, text):
        '''
        切词
        :param text:
        :return:
        '''
        words = self.s(text).words
        return words

    def word_category(self, text):
        '''
        词性
        :param text:
        :return:
        '''
        tags = list(self.s(text).tags)
        return tags

    def text_sentiments(self, text):
        '''
        情感分析
        :param text:
        :return: 0.88
        '''
        sentiments = self.s(text).sentiments
        return sentiments

    def text_classify(self, text):
        '''
        文本分类
        :param text:
        :return:
        '''
        cls = Bayes()
        # cls.load(r'需要加载的文件名')
        return cls.classify(text)

    def text_2_pinyin(self, text):
        '''
        转拼音
        :param text:
        :return:
        '''
        return self.s(text).pinyin(text)

    def get_keywords(self, text, topN=3):
        '''
        关键词
        :param text:
        :param topN:
        :return:
        '''
        return self.s(text).keywords(topN)


if __name__ == '__main__':
    aipsnow = ApiSnow()
    text = '通过对源码的阅读，我们可以看到情感分析模型是通过朴素贝叶斯方法实现的。我们可以调用Bayes接口，通过自己的数据进行训练、或加载自己的模型，实现自定义的文本分类功能'
    print(aipsnow.get_keywords(text))
    print(aipsnow.text_classify(text))