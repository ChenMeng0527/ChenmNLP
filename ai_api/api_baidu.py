# coding=utf-8
'''
baidu 接口实现nlp功能
'''

from aip import AipNlp

class ApiBaidu:
    '''
    baidu_api类
    '''
    def __init__(self,
                       # APP_ID = '20488258',
                       # API_KEY = '2HU4eUSilVOfAbGQiChDBqKG',
                       # SECRET_KEY = 'BaDGsVzIX9jjSnLbhGCABg0HtGPO53MR'

                       # youshu
                       APP_ID = '23767146',
                       API_KEY = '2HU4eUSilVOfAbGQiChDBqKG',
                       SECRET_KEY = 'BaDGsVzIX9jjSnLbhGCABg0HtGPO53MR'
                ):

        self.client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


    def get_sentiment_classify(self, text):
        """
        情感分类
        :param text:
        :return: ['正相概率','负相概率','置信度','分类']  分类：2：正 / 1：中 / 0：负
        """
        result_temp = self.client.sentimentClassify(text)
        result = []

        if result_temp.get('items'):
            item_ = result_temp['items'][0]
            print(item_)
            result.append(round(item_['positive_prob'],4))
            result.append(round(item_['negative_prob'],4))
            result.append(round(item_['confidence'],4))
            result.append(item_['sentiment'])
        return result


    def get_comment_tag(self, text, category_type=4):
        '''

        :param text:
        :param category_type: 类别编号
            1 - 酒店
            2 - KTV
            3 - 丽人
            4 - 美食餐饮(默认)
            5 - 旅游
            6 - 健康
            7 - 教育
            8 - 商业
            9 - 房产
            10 - 汽车
            11 - 生活
            12 - 购物
            13 - 3C
        :return: [['屏幕漂亮',2],['售后差',0],[]]  0-负 / 1-中 / 2-正
        '''
        result = []

        options = {}
        options["type"] = category_type
        result_temp = self.client.commentTag(text, options)
        print(result_temp)
        # 调用返回
        # {
        #     "items": [
        #         {
        #         "prop":"电池",
        #         "adj": "不给力",
        #         "sentiment": 0,
        #         "begin_pos": 8,
        #         "end_pos": 18,
        #         "abstract":"三星电脑<span>电池不给力</span>"
        #         }
        #     ]
        # }
        # prop	string	匹配上的属性词
        # adj	string	匹配上的描述词
        # sentiment	int	该情感搭配的极性（0表示消极，1表示中性，2表示积极）
        # begin_pos	int	该情感搭配在句子中的开始位置
        # end_pos	int	该情感搭配在句子中的结束位置
        # abstract	string	对应于该情感搭配的短句摘要
        if result_temp.get('items'):
            temps = result_temp['items']
            for i in temps:
                result.append([i['prop'] + i['adj'], i['sentiment']])
        return result


if __name__ == '__main__':
    api = ApiBaidu()
    api.get_sentiment_classify('老师声音很好听')
