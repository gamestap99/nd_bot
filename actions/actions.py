# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

DATABASE = ["bún đậu mắm tôm",
            "bún đậu nước mắm",
            "bún cá",
            "bún hải sản",
            "cơm văn phòng",
            "cơm sườn",
            "xôi",
            "bún ốc",
            "mì vằn thắn",
            "hủ tiếu",
            "bún chả",
            "bún ngan",
            "ngan xào tỏi",
            "bún bò huế",
            "mì tôm hải sản",
            "bánh mì trứng xúc xích rắc thêm ít ngải cứu",
            "bánh mì trứng",
            "bánh mì xúc xích",
            "bánh mì pate"]


class ActionRecommend(Action):

    def name(self) -> Text:
        return "action_recommend"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food = []
        for i in range(2):
            food_number = random.randrange(len(DATABASE))
            food.append(DATABASE[food_number])

        dispatcher.utter_message(
            text="Em nghĩ hôm nay anh chị có thể thử món '{}' hoặc bên cạnh đó cũng có thể là món '{}' ạ".format(food[0], food[1]))

        return []
        
class action_get_lottery(Action):
	def name(self):
            # Doan nay khai bao giong het ten ham ben tren la okie
		    return 'action_get_lottery'
	def run(self, dispatcher, tracker, domain):
            # Khai bao dia chi luu tru ket qua so xo. O day lam vi du nen minh lay ket qua SX Mien Bac
            url = 'https://xskt.com.vn/rss-feed/mien-bac-xsmb.rss'
            # Tien hanh lay thong tin tu URL
            feed_cnt = feedparser.parse(url)
            # Lay ket qua so xo moi nhat
            first_node = feed_cnt['entries']
            # Lay thong tin ve ngay va chi tiet cac giai
            return_msg = first_node[0]['title'] + "\n" + first_node[0]['description']
            # Tra ve cho nguoi dung
            dispatcher.utter_message(return_msg)
            return []