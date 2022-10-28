#coding=utf-8

'''
pkuseg
北大分词
'''


import pkuseg


class ApiPkuseg:

    def __init__(self):
        pass

    def cut_word_singal(self, text):
        seg = pkuseg.pkuseg()  # 以默认配置加载模型
        text = seg.cut(text)  # 进行分词
        return text
