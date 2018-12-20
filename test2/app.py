from findurl import *
from proverb import *
# -*- coding: utf-8 -*-
import json
import os
import re
import urllib.request

from selenium import webdriver
from bs4 import BeautifulSoup
from slackclient import SlackClient
from flask import Flask, request, make_response, render_template

isDream = False
isList = False

app = Flask(__name__)

slack_token = "xoxb-502761537154-507692267477-g8OydTG0lbyNv1tKs5A8MOjF"
slack_client_id = "502761537154.506751972416"
slack_client_secret = "502761537154.506751972416"
slack_verification = "kov20Lf5pwBxadSJFoRGhZZ6"
sc = SlackClient(slack_token)


# 크롤링 함수 구현하기
def _crawl_naver_keywords(text):

    result = re.sub(r'<<@\S+>> ', '', text)  # text로부터 첫번째 인자의 패턴을 찾아서 두번째 인자로 바꾼다

    keywords = []

    if "안녕" in result:
        return "안녕하세요! 좋은 아침이에요\n\n 1.명언을 보고 싶다면 명언을 입력해주세요\n 2. 운세를 보고 싶다면\n*띠\별자리* 하나와\n *오늘\내일\이주\이달* 중 하나를 입력해주세요.\n 예시 : *게자리 오늘*"
    elif "Hi" in result:
        return "Hello! Good morning\n I want Korean"
    elif "명언" in result:
        if "1. 명언" not in result:
            return proverb()
    else:
        url = findURL(result)
        if url == 'urlnono':
            return "\nㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ\n\n1. 명언을 보고 싶다면 *명언* 을 입력해주세요\n\n 2. 운세를 보고 싶다면\n\n*띠\별자리* 하나와\n *오늘\내일\이주\이달* 중 하나를 입력해주세요.\n 예시 : *게자리 오늘*.\n\nㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ\n"
        source = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(source, "html.parser")
        for content in soup.find_all("p", class_='text _cs_fortune_text'):
            keywords.append(content.get_text().strip())

        if "오늘" in result:
            return keywords[0]
        elif "내일" in result:
            return keywords[1]
        elif "이주" in result:
            return keywords[2]
        elif "이달" in result:
            return keywords[3]
        else:
            return "*띠\별자리* 하나와\n *오늘\내일\이주\이달* 중 하나를 입력해주세요.\n 예시 : *게자리 오늘*"

#꿈이 이전에 입력 됬을 경우
#꿈의 키워드가 입력 값.
def _crawl_dream_keywords(text):
    #꿈 풀이의 목록을 출력
    print("a")

#입력 받은 넘버와 링크를 통해서 출력
#text 값에 넘버가 온다.

def _crawl_dream_print_keywords(text):
    #꿈 풀이의 목록을 출력
    print("a")

# 이벤트 핸들하는 함수
def _event_handler(event_type, slack_event):

    # print(slack_event["event"])

    if event_type == "app_mention":
        channel = slack_event["event"]["channel"]
        text = slack_event["event"]["text"]

        if isDream==True:
            if isList == True:
                keywords = _crawl_dream_print_keywords(text) #text = 번호
            else:
                keywords = _crawl_dream_keywords(text) #text 검색 키워드 #딕셔너리 저장하기

        else:
            keywords = _crawl_naver_keywords(text)

        sc.api_call(
            "chat.postMessage",
            channel=channel,
            text=keywords
        )

        return make_response("App mention message has been sent", 200,)

    # ============= Event Type Not Found! ============= #
    # If the event_type does not have a handler
    message = "You have not added an event handler for the %s" % event_type
    # Return a helpful error message
    return make_response(message, 200, {"X-Slack-No-Retry": 1})

@app.route("/listening", methods=["GET", "POST"])
def hears():

    slack_event = json.loads(request.data)

#    print(slack_event)

    if "challenge" in slack_event:
        return make_response(slack_event["challenge"], 200, {"content_type":
                                                                 "application/json"
                                                             })

    if slack_verification != slack_event.get("token"):
        message = "Invalid Slack verification token: %s" % (slack_event["token"])
        make_response(message, 403, {"X-Slack-No-Retry": 1})

    if "event" in slack_event:
        event_type = slack_event["event"]["type"]
        return _event_handler(event_type, slack_event)

    # If our bot hears things that are not events we've subscribed to,
    # send a quirky but helpful error response
    return make_response("[NO EVENT IN SLACK REQUEST] These are not the droids\
                         you're looking for.", 404, {"X-Slack-No-Retry": 1})


@app.route("/", methods=["GET"])
def index():
    return "<h1>Server is ready.</h1>"


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000)
