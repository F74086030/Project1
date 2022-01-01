import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, URITemplateAction, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackTemplateAction, CarouselTemplate, CarouselColumn


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_image_message(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        type='image',
        original_content_url=url,
        preview_image_url=url
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"


def send_restaurant_info(reply_token, image_url, info_url, map_url, rec_url):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='店家資訊',
            text='點擊看店家介紹、地圖及類似店家!',
            thumbnail_image_url=image_url,
            actions=[
                URITemplateAction(
                    label='店家介紹',
                    uri=info_url
                ), URITemplateAction(
                    label='地圖',
                    uri=map_url
                ), URITemplateAction(
                    label='類似店家',
                    uri=rec_url
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_breakfast_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='早餐類型',
            text='想吃中式還是西式早餐呢?',
            thumbnail_image_url='https://i.imgur.com/SSeToxn.jpg',
            actions=[
                MessageTemplateAction(
                    label='中式早餐',
                    text='breakfast_chinese'
                ),
                MessageTemplateAction(
                    label='西式早餐',
                    text='breakfast_western'
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_breakfast_chinese_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='中式早餐',
            text='點擊食物種類',
            thumbnail_image_url='https://i.imgur.com/3rllC2L.jpg',
            actions=[
                MessageTemplateAction(
                    label='蛋餅',
                    text='chinese_omelet'
                ),
                MessageTemplateAction(
                    label='牛肉湯',
                    text='beef_soup'
                ),
                MessageTemplateAction(
                    label='鹹粥',
                    text='savory_porridge'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_chinese_omelet_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='蛋餅',
            text='點擊店家看介紹',
            thumbnail_image_url='https://i.imgur.com/gPvkdFy.jpg',
            actions=[
                MessageTemplateAction(
                    label='阿公阿婆蛋餅',
                    text='chinese_omelet1'
                ),
                MessageTemplateAction(
                    label='少爺蛋餅',
                    text='chinese_omelet2'
                ),
                MessageTemplateAction(
                    label='好時辰手工蛋餅',
                    text='chinese_omelet3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_beef_soup_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='牛肉湯',
            text='點擊店家看介紹',
            thumbnail_image_url='https://i.imgur.com/Lp6nNb1.jpg',
            actions=[
                MessageTemplateAction(
                    label='新鮮牛肉湯',
                    text='beef_soup1'
                ),
                MessageTemplateAction(
                    label='圓環牛肉湯',
                    text='beef_soup2'
                ),
                MessageTemplateAction(
                    label='西羅殿牛肉湯',
                    text='beef_soup3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_savory_porridge_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='鹹粥',
            text='點擊店家看介紹',
            thumbnail_image_url='https://i.imgur.com/NMTkmAl.jpg',
            actions=[
                MessageTemplateAction(
                    label='悅津鹹粥',
                    text='savory_porridge1'
                ),
                MessageTemplateAction(
                    label='阿堂鹹粥',
                    text='savory_porridge2'
                ),
                MessageTemplateAction(
                    label='阿憨鹹粥',
                    text='savory_porridge3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_breakfast_western_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='西式早餐',
            text='點擊店家看介紹',
            thumbnail_image_url='https://i.imgur.com/HoYgmZp.jpg',
            actions=[
                MessageTemplateAction(
                    label='六吋盤',
                    text='breakfast_western1'
                ),
                MessageTemplateAction(
                    label='哈利8號',
                    text='breakfast_western2'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_lunch_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='午餐類型',
            text='想吃中式或西式午餐呢?也有其他選擇喔!',
            thumbnail_image_url='https://i.imgur.com/rzWqX45.jpg',
            actions=[
                MessageTemplateAction(
                    label='中式午餐',
                    text='lunch_chinese'
                ),
                MessageTemplateAction(
                    label='西式午餐',
                    text='lunch_western'
                ),
                MessageTemplateAction(
                    label='其他',
                    text='lunch_other'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_lunch_chinese_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='中式午餐',
            text='點擊店家看介紹',
            thumbnail_image_url='https://i.imgur.com/J7ceN0H.jpg',
            actions=[
                MessageTemplateAction(
                    label='國華街肉燥飯',
                    text='lunch_chinese1'
                ),
                MessageTemplateAction(
                    label='葉家小卷米粉',
                    text='lunch_chinese2'
                ),
                MessageTemplateAction(
                    label='手工鹽水意麵',
                    text='lunch_chinese3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_lunch_western_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='西式午餐',
            text='點擊店家看介紹',
            thumbnail_image_url='https://i.imgur.com/V5JF6oj.jpg',
            actions=[
                MessageTemplateAction(
                    label='飲食客 in Stock',
                    text='lunch_western1'
                ),
                MessageTemplateAction(
                    label='食べオム洋食歐姆',
                    text='lunch_western2'
                ),
                MessageTemplateAction(
                    label='SK尚恩',
                    text='lunch_western3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_lunch_other_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='其他種類',
            text='點擊店家看介紹',
            thumbnail_image_url='https://i.imgur.com/Tty1NxX.jpg',
            actions=[
                MessageTemplateAction(
                    label='ㄧ拉面',
                    text='lunch_other1'
                ),
                MessageTemplateAction(
                    label='櫻之庭',
                    text='lunch_other2'
                ),
                MessageTemplateAction(
                    label='歐八不是阿啾喜',
                    text='lunch_other3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_dinner_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='晚餐類型',
            text='想吃中式或西式晚餐呢?',
            thumbnail_image_url='https://i.imgur.com/CyFnXGD.jpg',
            actions=[
                MessageTemplateAction(
                    label='中式',
                    text='dinner_chinese'
                ),
                MessageTemplateAction(
                    label='西式',
                    text='dinner_western'
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_dinner_chinese_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='中式晚餐',
            text='點擊店家看介紹',
            thumbnail_image_url='https://i.imgur.com/H1ygK2p.jpg',
            actions=[
                MessageTemplateAction(
                    label='金元寶餐館',
                    text='dinner_chinese1'
                ),
                MessageTemplateAction(
                    label='七海魚皮',
                    text='dinner_chinese2'
                ),
                MessageTemplateAction(
                    label='龍來現代炒館',
                    text='dinner_chinese3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"

def send_dinner_western_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='西式晚餐',
            text='點擊店家看介紹',
            thumbnail_image_url='https://i.imgur.com/NMUM8wo.jpg',
            actions=[
                MessageTemplateAction(
                    label='胖廚西式餐廳',
                    text='dinner_western1'
                ),
                MessageTemplateAction(
                    label='台南木棉道餐廳',
                    text='dinner_western2'
                ),
                MessageTemplateAction(
                    label='餵胃',
                    text='dinner_western3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"

def send_button_carousel(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/IDEmUpM.jpg',
                    title='店家推薦',
                    text='想吃什麼呢??',
                    actions=[
                        MessageTemplateAction(
                            label='早餐',
                            text='breakfast'
                        ),
                        MessageTemplateAction(
                            label='午餐',
                            text='lunch'
                        ),
                        MessageTemplateAction(
                            label='晚餐',
                            text='dinner'
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.push_message(id, message)

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
