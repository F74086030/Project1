import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackTemplateAction, CarouselTemplate, CarouselColumn
from fsm import TocMachine
from utils import send_text_message, send_image_message
from transitions import Machine

load_dotenv()


machine = TocMachine(
    states=["user", "start", "breakfast", "lunch", "dinner",
            "breakfast_chinese", "breakfast_western", "chinese_omelet", "beef_soup", "savory_porridge", "breakfast_western1", "breakfast_western2",  "chinese_omelet1",  "chinese_omelet2", "chinese_omelet3", "beef_soup1", "beef_soup2", "beef_soup3", "savory_porridge1", "savory_porridge2", "savory_porridge3", "lunch_chinese", "lunch_western", "lunch_other", "lunch_chinese1", "lunch_chinese2", "lunch_chinese3", "lunch_western1", "lunch_western2", "lunch_western3", "lunch_other1", "lunch_other2", "lunch_other3", "dinner_chinese",  "dinner_western",  "dinner_chinese1", "dinner_chinese2", "dinner_chinese3", "dinner_western1", "dinner_western2", "dinner_western3"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "start",
            "conditions": "is_going_to_start",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "breakfast",
            "conditions": "is_going_to_breakfast",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "lunch",
            "conditions": "is_going_to_lunch",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "dinner",
            "conditions": "is_going_to_dinner",
        },
        {
            "trigger": "advance",
            "source": "breakfast",
            "dest": "breakfast_chinese",
            "conditions": "is_going_to_breakfast_chinese",
        },
        {
            "trigger": "advance",
            "source": "breakfast",
            "dest": "breakfast_western",
            "conditions": "is_going_to_breakfast_western",
        },
        {
            "trigger": "advance",
            "source": "lunch",
            "dest": "lunch_chinese",
            "conditions": "is_going_to_lunch_chinese",
        },
        {
            "trigger": "advance",
            "source": "lunch",
            "dest": "lunch_western",
            "conditions": "is_going_to_lunch_western",
        },
        {
            "trigger": "advance",
            "source": "lunch",
            "dest": "lunch_other",
            "conditions": "is_going_to_lunch_other",
        },
        {
            "trigger": "advance",
            "source": "dinner",
            "dest": "dinner_chinese",
            "conditions": "is_going_to_dinner_chinese",
        },
        {
            "trigger": "advance",
            "source": "dinner",
            "dest": "dinner_western",
            "conditions": "is_going_to_dinner_western",
        },
        {
            "trigger": "advance",
            "source": "breakfast_chinese",
            "dest": "chinese_omelet",
            "conditions": "is_going_to_chinese_omelet",
        },
        {
            "trigger": "advance",
            "source": "breakfast_chinese",
            "dest": "beef_soup",
            "conditions": "is_going_to_beef_soup",
        },
        {
            "trigger": "advance",
            "source": "breakfast_chinese",
            "dest": "savory_porridge",
            "conditions": "is_going_to_savory_porridge",
        },
        {
            "trigger": "advance",
            "source": "chinese_omelet",
            "dest": "chinese_omelet1",
            "conditions": "is_going_to_chinese_omelet1",
        },
        {
            "trigger": "advance",
            "source": "chinese_omelet",
            "dest": "chinese_omelet2",
            "conditions": "is_going_to_chinese_omelet2",
        },
        {
            "trigger": "advance",
            "source": "chinese_omelet",
            "dest": "chinese_omelet3",
            "conditions": "is_going_to_chinese_omelet3",
        },
        {
            "trigger": "advance",
            "source": "beef_soup",
            "dest": "beef_soup1",
            "conditions": "is_going_to_beef_soup1",
        },
        {
            "trigger": "advance",
            "source": "beef_soup",
            "dest": "beef_soup2",
            "conditions": "is_going_to_beef_soup2",
        },
        {
            "trigger": "advance",
            "source": "beef_soup",
            "dest": "beef_soup3",
            "conditions": "is_going_to_beef_soup3",
        },
        {
            "trigger": "advance",
            "source": "savory_porridge",
            "dest": "savory_porridge1",
            "conditions": "is_going_to_savory_porridge1",
        },
        {
            "trigger": "advance",
            "source": "savory_porridge",
            "dest": "savory_porridge2",
            "conditions": "is_going_to_savory_porridge2",
        },
        {
            "trigger": "advance",
            "source": "savory_porridge",
            "dest": "savory_porridge3",
            "conditions": "is_going_to_savory_porridge3",
        },
        {
            "trigger": "advance",
            "source": "breakfast_western",
            "dest": "breakfast_western1",
            "conditions": "is_going_to_breakfast_western1",
        },
        {
            "trigger": "advance",
            "source": "breakfast_western",
            "dest": "breakfast_western2",
            "conditions": "is_going_to_breakfast_western2",
        },
        {
            "trigger": "advance",
            "source": "lunch_chinese",
            "dest": "lunch_chinese1",
            "conditions": "is_going_to_lunch_chinese1",
        },
        {
            "trigger": "advance",
            "source": "lunch_chinese",
            "dest": "lunch_chinese2",
            "conditions": "is_going_to_lunch_chinese2",
        },
        {
            "trigger": "advance",
            "source": "lunch_chinese",
            "dest": "lunch_chinese3",
            "conditions": "is_going_to_lunch_chinese3",
        },
        {
            "trigger": "advance",
            "source": "lunch_western",
            "dest": "lunch_western1",
            "conditions": "is_going_to_lunch_western1",
        },
        {
            "trigger": "advance",
            "source": "lunch_western",
            "dest": "lunch_western2",
            "conditions": "is_going_to_lunch_western2",
        },
        {
            "trigger": "advance",
            "source": "lunch_western",
            "dest": "lunch_western3",
            "conditions": "is_going_to_lunch_western3",
        },
        {
            "trigger": "advance",
            "source": "lunch_other",
            "dest": "lunch_other1",
            "conditions": "is_going_to_lunch_other1",
        },
        {
            "trigger": "advance",
            "source": "lunch_other",
            "dest": "lunch_other2",
            "conditions": "is_going_to_lunch_other2",
        },
        {
            "trigger": "advance",
            "source": "lunch_other",
            "dest": "lunch_other3",
            "conditions": "is_going_to_lunch_other3",
        },
        {
            "trigger": "advance",
            "source": "dinner_chinese",
            "dest": "dinner_chinese1",
            "conditions": "is_going_to_dinner_chinese1",
        },
        {
            "trigger": "advance",
            "source": "dinner_chinese",
            "dest": "dinner_chinese2",
            "conditions": "is_going_to_dinner_chinese2",
        },
        {
            "trigger": "advance",
            "source": "dinner_chinese",
            "dest": "dinner_chinese3",
            "conditions": "is_going_to_dinner_chinese3",
        },
        {
            "trigger": "advance",
            "source": "dinner_western",
            "dest": "dinner_western1",
            "conditions": "is_going_to_dinner_western1",
        },
        {
            "trigger": "advance",
            "source": "dinner_western",
            "dest": "dinner_western2",
            "conditions": "is_going_to_dinner_western2",
        },
        {
            "trigger": "advance",
            "source": "dinner_western",
            "dest": "dinner_western3",
            "conditions": "is_going_to_dinner_western3",
        },
        {"trigger": "go_back", "source": [
            "user", "start", "breakfast", "lunch", "dinner","breakfast_chinese", "breakfast_western", "chinese_omelet", "beef_soup", "savory_porridge", "breakfast_western1", "breakfast_western2",  "chinese_omelet1",  "chinese_omelet2", "chinese_omelet3", "beef_soup1", "beef_soup2", "beef_soup3", "savory_porridge1", "savory_porridge2", "savory_porridge3", "lunch_chinese", "lunch_western", "lunch_other", "lunch_chinese1", "lunch_chinese2", "lunch_chinese3", "lunch_western1", "lunch_western2", "lunch_western3", "lunch_other1", "lunch_other2", "lunch_other3", "dinner_chinese",  "dinner_western",  "dinner_chinese1", "dinner_chinese2", "dinner_chinese3", "dinner_western1", "dinner_western2", "dinner_western3"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            if event.message.text == 'fsm':
                send_image_message(event.reply_token,
                                   ' https://ae41-115-43-209-187.ngrok.io/show-fsm')

            else:
                send_text_message(event.reply_token,
                                  "想吃甚麼呢?輸入'start'開始尋找吧!")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
