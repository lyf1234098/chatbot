# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


#This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import pymysql
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import logging


def get_action(keyword):
    # 连接到MySQL数据库
      connection = pymysql.connect(
         host='127.0.0.1',  # 数据库主机地址
           user='root',  # 数据库用户名
            password='lyf123456',  # 数据库密码
            database='shop'  # 数据库名称
        )


      cursor = connection.cursor()
      sql = "SELECT * FROM shopdata WHERE keywords = %s"
      cursor.execute(sql, (keyword,))
      results = cursor.fetchall()


      for row in results:
            # 根据表结构访问数据

           return row[0]


      cursor.close()
      connection.close()


class action_weather_init(Action):

    def name(self) -> Text:
        return "action_weather_init"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        keyword = tracker.get_slot('team')
        text=get_action(keyword)

        dispatcher.utter_message(text)
        logging.info(f"action_weather_init 被调用，生成响应: {text}")
        return []

# 添加更多自定义操作
