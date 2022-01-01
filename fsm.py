from transitions.extensions import GraphMachine
import graphviz
from utils import send_text_message, send_image_message, send_restaurant_info, send_breakfast_type, send_breakfast_chinese_type, send_chinese_omelet_type, send_beef_soup_type, send_savory_porridge_type, send_breakfast_western_type, send_lunch_type, send_lunch_chinese_type, send_lunch_western_type, send_lunch_other_type, send_dinner_type, send_dinner_chinese_type, send_dinner_western_type, send_button_carousel


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"

    def is_going_to_breakfast(self, event):
        text = event.message.text
        return text.lower() == "breakfast"

    def is_going_to_lunch(self, event):
        text = event.message.text
        return text.lower() == "lunch"

    def is_going_to_dinner(self, event):
        text = event.message.text
        return text.lower() == "dinner"

    def is_going_to_breakfast_chinese(self, event):
        text = event.message.text
        return text.lower() == "breakfast_chinese"

    def is_going_to_breakfast_western(self, event):
        text = event.message.text
        return text.lower() == "breakfast_western"

    def is_going_to_lunch_chinese(self, event):
        text = event.message.text
        return text.lower() == "lunch_chinese"

    def is_going_to_lunch_western(self, event):
        text = event.message.text
        return text.lower() == "lunch_western"

    def is_going_to_lunch_other(self, event):
        text = event.message.text
        return text.lower() == "lunch_other"

    def is_going_to_dinner_chinese(self, event):
        text = event.message.text
        return text.lower() == "dinner_chinese"

    def is_going_to_dinner_western(self, event):
        text = event.message.text
        return text.lower() == "dinner_western"

    def is_going_to_chinese_omelet(self, event):
        text = event.message.text
        return text.lower() == "chinese_omelet"

    def is_going_to_beef_soup(self, event):
        text = event.message.text
        return text.lower() == "beef_soup"

    def is_going_to_savory_porridge(self, event):
        text = event.message.text
        return text.lower() == "savory_porridge"

    def is_going_to_chinese_omelet1(self, event):
        text = event.message.text
        return text.lower() == "chinese_omelet1"

    def is_going_to_chinese_omelet2(self, event):
        text = event.message.text
        return text.lower() == "chinese_omelet2"

    def is_going_to_chinese_omelet3(self, event):
        text = event.message.text
        return text.lower() == "chinese_omelet3"
    
    def is_going_to_beef_soup1(self, event):
        text = event.message.text
        return text.lower() == "beef_soup1"

    def is_going_to_beef_soup2(self, event):
        text = event.message.text
        return text.lower() == "beef_soup2"

    def is_going_to_beef_soup3(self, event):
        text = event.message.text
        return text.lower() == "beef_soup3"
    
    def is_going_to_savory_porridge1(self, event):
        text = event.message.text
        return text.lower() == "savory_porridge1"

    def is_going_to_savory_porridge2(self, event):
        text = event.message.text
        return text.lower() == "savory_porridge2"

    def is_going_to_savory_porridge3(self, event):
        text = event.message.text
        return text.lower() == "savory_porridge3"

    def is_going_to_breakfast_western1(self, event):
        text = event.message.text
        return text.lower() == "breakfast_western1"

    def is_going_to_breakfast_western2(self, event):
        text = event.message.text
        return text.lower() == "breakfast_western2"

    def is_going_to_lunch_chinese1(self, event):
        text = event.message.text
        return text.lower() == "lunch_chinese1"

    def is_going_to_lunch_chinese2(self, event):
        text = event.message.text
        return text.lower() == "lunch_chinese2"

    def is_going_to_lunch_chinese3(self, event):
        text = event.message.text
        return text.lower() == "lunch_chinese3"

    def is_going_to_lunch_western1(self, event):
        text = event.message.text
        return text.lower() == "lunch_western1"

    def is_going_to_lunch_western2(self, event):
        text = event.message.text
        return text.lower() == "lunch_western2"

    def is_going_to_lunch_western3(self, event):
        text = event.message.text
        return text.lower() == "lunch_western3"

    def is_going_to_lunch_other1(self, event):
        text = event.message.text
        return text.lower() == "lunch_other1"

    def is_going_to_lunch_other2(self, event):
        text = event.message.text
        return text.lower() == "lunch_other2"

    def is_going_to_lunch_other3(self, event):
        text = event.message.text
        return text.lower() == "lunch_other3"

    def is_going_to_dinner_chinese1(self, event):
        text = event.message.text
        return text.lower() == "dinner_chinese1"

    def is_going_to_dinner_chinese2(self, event):
        text = event.message.text
        return text.lower() == "dinner_chinese2"

    def is_going_to_dinner_chinese3(self, event):
        text = event.message.text
        return text.lower() == "dinner_chinese3"

    def is_going_to_dinner_western1(self, event):
        text = event.message.text
        return text.lower() == "dinner_western1"

    def is_going_to_dinner_western2(self, event):
        text = event.message.text
        return text.lower() == "dinner_western2"

    def is_going_to_dinner_western3(self, event):
        text = event.message.text
        return text.lower() == "dinner_western3"

    def on_enter_start(self, event):
        print("I'm entering start")

        userid = event.source.user_id
        send_button_carousel(userid)

    def on_enter_breakfast(self, event):
        print("I'm entering breakfast")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_breakfast_type(reply_token, userid)

    def on_enter_lunch(self, event):
        print("I'm entering lunch")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_lunch_type(reply_token, userid)
    
    def on_enter_lunch_chinese(self, event):
        print("I'm entering lunch_chinese")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_lunch_chinese_type(reply_token, userid)
    
    def on_enter_lunch_chinese1(self, event):
        print("I'm entering lunch_chinese1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/58kPkpH.jpg'
        info_url = 'https://foodieteller.com/kuohau-street-rice/'
        map_url = 'https://www.google.com/maps/place/%E5%9C%8B%E8%8F%AF%E8%A1%97%E8%82%89%E7%87%A5%E9%A3%AF/@22.9985698,120.1950084,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76641bf02645:0x1b8ef251199afea2!8m2!3d22.9985698!4d120.1971971?hl=zh-TW'
        rec_url = 'https://tainanfoodeat.blogspot.com/2020/04/tainan-porkrice.html'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_lunch_chinese2(self, event):
        print("I'm entering lunch_chinese2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/KyYuCb0.jpg'
        info_url = 'https://tenjo.tw/yehjia/'
        map_url = 'https://www.google.com/maps/place/%E8%91%89%E5%AE%B6%E5%B0%8F%E5%8D%B7%E7%B1%B3%E7%B2%89/@22.9910754,120.1947708,17z/data=!4m9!1m2!2m1!1z6JGJ5a625bCP5Y2357Gz57KJ!3m5!1s0x346e7664e96d5667:0x8516e41c5544568d!8m2!3d22.9910733!4d120.1969684!15sChLokYnlrrblsI_ljbfnsbPnsolaGCIW6JGJIOWutiDlsI8g5Y23IOexs-eyiZIBCnJlc3RhdXJhbnQ'
        rec_url = 'https://boylondon.tw/2009-06-14-2320/'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_lunch_chinese3(self, event):
        print("I'm entering lunch_chinese3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/IOhzfIm.jpg'
        info_url = 'https://travel.yam.com/article/115742'
        map_url = 'https://www.google.com/maps/place/%E6%89%8B%E5%B7%A5%E9%B9%BD%E6%B0%B4%E6%84%8F%E9%BA%B5/@22.9958876,120.173675,17z/data=!3m1!4b1!4m5!3m4!1s0x346e760e06725d8f:0xe7eb66b376bd661e!8m2!3d22.9958876!4d120.1758637?hl=zh-TW'
        rec_url = 'https://ifoodie.tw/explore/%E5%8F%B0%E5%8D%97%E5%B8%82/list/%E9%B9%BD%E6%B0%B4%E6%84%8F%E9%BA%B5'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()
    
    def on_enter_lunch_western(self, event):
        print("I'm entering lunch_western")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_lunch_western_type(reply_token, userid)
    
    def on_enter_lunch_western1(self, event):
        print("I'm entering lunch_western1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/SVg4dHY.jpg'
        info_url = 'https://decing.tw/tainan-instock/'
        map_url = 'https://www.google.com/maps/place/%E9%A3%B2%E9%A3%9F%E5%AE%A2+In+Stock/@22.9891091,120.2072086,17z/data=!3m1!4b1!4m5!3m4!1s0x346e7686221dc14d:0xe1e048485b869fa5!8m2!3d22.9891091!4d120.2093973?hl=zh-TW'
        rec_url = 'https://ifoodie.tw/explore/%E5%8F%B0%E5%8D%97%E5%B8%82/list/%E5%8F%B0%E5%8D%97-%E8%A5%BF%E5%BC%8F%E6%96%99%E7%90%86'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_lunch_western2(self, event):
        print("I'm entering lunch_western2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/iFfMxu9.jpg'
        info_url = 'https://www.daisyyohoho.com/tainan-darling-omurice/'
        map_url = 'https://www.google.com/maps/place/%E9%A3%9F%E3%81%B9%E3%82%AA%E3%83%A0%E6%B4%8B%E9%A3%9F%E6%AD%90%E5%A7%86%E5%B0%82%E9%96%80%E5%BA%97/@22.9790902,120.0723661,11z/data=!4m9!1m2!2m1!1z5rSL6aOf5q2Q5aeG!3m5!1s0x346e77cfb7572573:0xa782fa77d4b46f0d!8m2!3d22.9790902!4d120.2124418!15sCgzmtIvpo5_mrZDlp4ZaDyIN5rSL6aOfIOatkOWnhpIBIWphcGFuaXplZF93ZXN0ZXJuX2Zvb2RfcmVzdGF1cmFudA?hl=zh-TW'
        rec_url = 'https://ifoodie.tw/explore/%E5%8F%B0%E5%8D%97%E5%B8%82/list/%E5%8F%B0%E5%8D%97-%E8%A5%BF%E5%BC%8F%E6%96%99%E7%90%86'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_lunch_western3(self, event):
        print("I'm entering lunch_western3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/8Ryra2d.jpg'
        info_url = 'https://hululu.tw/sk/'
        map_url = 'https://www.google.com/maps/place/SK%E5%B0%9A%E6%81%A9%E7%BE%8E%E5%BC%8F%E9%A4%90%E5%BB%B3/@22.995466,120.2258418,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76c00ad0c89d:0xb5f051b493f8c27e!8m2!3d22.995466!4d120.2280305?hl=zh-TW'
        rec_url = 'https://ifoodie.tw/explore/%E5%8F%B0%E5%8D%97%E5%B8%82/list/%E5%8F%B0%E5%8D%97-%E8%A5%BF%E5%BC%8F%E6%96%99%E7%90%86'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()
    
    def on_enter_lunch_other(self, event):
        print("I'm entering lunch_other")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_lunch_other_type(reply_token, userid)
    
    def on_enter_lunch_other1(self, event):
        print("I'm entering lunch_other1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/iLuzkxR.jpg'
        info_url = 'https://hoolee.tw/natural-ramen/'
        map_url = 'https://www.google.com/maps/place/%E3%84%A7%E6%8B%89%E9%9D%A2-%E8%B1%9A%E9%AA%A8%E5%B0%88%E8%B3%A3/@23.0086617,120.2182836,17z/data=!3m1!4b1!4m5!3m4!1s0x346e77989d1e8655:0x81024a287238f3d0!8m2!3d23.0086639!4d120.2205063?hl=zh-TW'
        rec_url = 'https://boylondon.tw/ramen/'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_lunch_other2(self, event):
        print("I'm entering lunch_other2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/xXHC6LN.jpg'
        info_url = 'https://www.mrtainan.com/2019/12/062082068.html'
        map_url = 'https://www.google.com/maps?q=%E6%AB%BB%E4%B9%8B%E5%BA%AD&bih=558&biw=1229&hl=zh-TW&um=1&ie=UTF-8&sa=X&ved=2ahUKEwigm4iU65D1AhXMd94KHY1GC3MQ_AUoAnoECAIQBA'
        rec_url = 'https://ma16zaq2000.pixnet.net/blog/post/352604095-2020%E5%B9%B4%E3%80%90%E5%8F%B0%E5%8D%97%E6%97%A5%E6%9C%AC%E6%96%99%E7%90%86%E6%87%B6%E4%BA%BA%E5%8C%85%E3%80%91%E6%94%B6%E9%8C%8417%E5%AE%B6%E6%97%A5%E5%BC%8F%E5%AE%9A'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_lunch_other3(self, event):
        print("I'm entering lunch_other3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/PfWGSOu.jpg'
        info_url = 'https://masaharuwu.pixnet.net/blog/post/69740270'
        map_url = 'https://www.google.com/maps/place/%E6%AD%90%E5%85%AB%E4%B8%8D%E6%98%AF%E9%98%BF%E5%95%BE%E5%96%9C_%E6%88%90%E5%A4%A7%E5%BA%97/@22.9917774,120.2065244,15z/data=!4m9!1m2!2m1!1z5q2Q54i45LiN5piv6Zi_5ZW-5Zac!3m5!1s0x346e7740a48ce51d:0x7f79fb3e68ebd880!8m2!3d22.9947662!4d120.2214678!15sChXmrZDniLjkuI3mmK_pmL_llb7llpxaHCIa5q2QIOeIuCDkuI3mmK8g6Zi_IOWVviDllpySARJzb29uZGFlX3Jlc3RhdXJhbnQ'
        rec_url = 'https://tainanfoodeat.blogspot.com/2020/01/blog-post_30.html'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_dinner(self, event):
        print("I'm entering dinner")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_dinner_type(reply_token, userid)
    
    def on_enter_dinner_chinese(self, event):
        print("I'm entering dinner_chinese")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_dinner_chinese_type(reply_token, userid)
    
    def on_enter_dinner_chinese1(self, event):
        print("I'm entering dinner_chinese1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/HKrusQ8.jpg'
        info_url = 'https://hululu.tw/goldingot1/'
        map_url = 'https://www.google.com/maps?q=%E9%87%91%E5%85%83%E5%AF%B6%E9%A4%90%E9%A4%A8&source=lmns&bih=558&biw=1229&hl=zh-TW&sa=X&ved=2ahUKEwij2Z7c7pD1AhVI25QKHYIVCKEQ_AUoAXoECAEQAQ'
        rec_url = 'https://supertaste.tvbs.com.tw/pack/321410'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_dinner_chinese2(self, event):
        print("I'm entering dinner_chinese2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/dwEa8Lm.jpg'
        info_url = 'https://eating403240554.pixnet.net/blog/post/297857280-%E6%9D%B1%E5%AF%A7%E8%B7%AF-%E4%B8%83%E6%B5%B7%E9%AD%9A%E7%9A%AE'
        map_url = 'https://www.google.com/maps/place/%E4%B8%83%E6%B5%B7%E9%AD%9A%E7%9A%AE/@22.9847379,120.2196058,15z/data=!4m9!1m2!2m1!1z5LiD5rW36a2a55qu!3m5!1s0x346e7696a35f8e99:0xbbbe72bf0a7fc540!8m2!3d22.991857!4d120.2222776!15sCgzkuIPmtbfprZrnmq5aECIO5LiD5rW3IOmtmiDnmq6SARJzZWFmb29kX3Jlc3RhdXJhbnQ?hl=zh-TW'
        rec_url = 'https://www.mrtainan.com/2020/10/kaiyuanmilkfish.html'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_dinner_chinese3(self, event):
        print("I'm entering dinner_chinese3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/Scluwxy.jpg'
        info_url = 'https://decing.tw/tainan-longlai/'
        map_url = 'https://www.google.com/maps/place/%E9%BE%8D%E4%BE%86%E7%8F%BE%E4%BB%A3%E7%82%92%E9%A4%A8/@22.9765899,120.2235937,17z/data=!3m1!4b1!4m5!3m4!1s0x346e771c3e4c211d:0xa38dd97dc4c94ea!8m2!3d22.9766327!4d120.2257254?hl=zh-TW'
        rec_url = 'https://www.boncity.com/Topic/Restaurant-CTW000025-K29898-Tainan-Chinese-Restaurant.html'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()
    
    def on_enter_dinner_western(self, event):
        print("I'm entering dinner_western")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_dinner_western_type(reply_token, userid)
    
    def on_enter_dinner_western1(self, event):
        print("I'm entering dinner_western1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/if83RMD.jpg'
        info_url = 'https://vhygdih0412.pixnet.net/blog/post/348125284-%5B%E5%8F%B0%E5%8D%97%E7%BE%8E%E9%A3%9F%5D-%E8%83%96%E5%BB%9A%E8%A5%BF%E5%BC%8F%E9%A4%90%E5%BB%B3-liveband-%E9%81%8B%E5%8B%95%E9%A4%90%E9%85%92%E9%A4%A8--'
        map_url = 'https://www.google.com/maps/place/%E8%83%96%E5%BB%9A%E8%A5%BF%E5%BC%8F%E9%9F%B3%E6%A8%82%E9%A4%90%E5%BB%B3/@22.998562,120.2058843,17z/data=!3m1!4b1!4m5!3m4!1s0x346e768b1d725e8f:0x17896e35eb20f329!8m2!3d22.998562!4d120.208073?hl=zh-TW'
        rec_url = 'https://boylondon.tw/2017-05-26-1795/'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_dinner_western2(self, event):
        print("I'm entering dinner_western2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/1j6m3E8.jpg'
        info_url = 'https://ivans120tw.pixnet.net/blog/post/352822232-%E5%8F%B0%E5%8D%97.%E6%9D%B1%E5%8D%80-%E6%9C%A8%E6%A3%89%E9%81%93%E6%B0%91%E6%AD%8C%E8%A5%BF%E9%A4%90%E5%BB%B3'
        map_url = 'https://www.google.com/maps?q=%E5%8F%B0%E5%8D%97%E6%9C%A8%E6%A3%89%E9%81%93%E9%A4%90%E5%BB%B3&um=1&ie=UTF-8&sa=X&ved=2ahUKEwicuan68JD1AhWXMd4KHZmcA78Q_AUoAXoECAIQAw'
        rec_url = 'https://boylondon.tw/%E5%8F%B0%E5%8D%97%E2%80%A7%E6%9C%AA%E5%A4%AE%E6%AD%8C/'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_dinner_western3(self, event):
        print("I'm entering dinner_western3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/32mlVC4.jpg'
        info_url = 'https://boylondon.tw/weiwei/'
        map_url = 'https://www.google.com/maps?q=%E9%A4%B5%E8%83%83&source=lmns&bih=558&biw=1229&hl=zh-TW&sa=X&ved=2ahUKEwjJx-_98ZD1AhXUQfUHHQZnAzEQ_AUoAXoECAEQAQ'
        rec_url = 'https://www.tainanlohas.cc/2021/09/Owner-steak.html'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_breakfast_chinese(self, event):
        print("I'm entering breakfast_chinese")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_breakfast_chinese_type(reply_token, userid)

    def on_enter_chinese_omelet(self, event):
        print("I'm entering chinese_omelet")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_chinese_omelet_type(reply_token, userid)

    def on_enter_beef_soup(self, event):
        print("I'm entering beef_soup")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_beef_soup_type(reply_token, userid)
    
    def on_enter_savory_porridge(self, event):
        print("I'm entering savory_porridge")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_savory_porridge_type(reply_token, userid)
    
    def on_enter_breakfast_western(self, event):
        print("I'm entering breakfast_western")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_breakfast_western_type(reply_token, userid)

    def on_enter_chinese_omelet1(self, event):
        print("I'm entering chinese_omelet1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/mIgbnC7.jpg'
        info_url = 'https://tenjo.tw/agongapo-eggpancake/'
        map_url = 'https://www.google.com/maps/place/%E9%98%BF%E5%85%AC%E9%98%BF%E5%A9%86%E8%9B%8B%E9%A4%85/@22.9994044,120.225466,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76ea7b464111:0x87d8e73fe4e8f48a!8m2!3d22.9994044!4d120.2276547'
        rec_url = 'https://ikachalife.com/854'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_chinese_omelet2(self, event):
        print("I'm entering chinese_omelet2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/Ya438wI.jpg'
        info_url = 'https://jeremyckt2.pixnet.net/blog/post/226133093-%5B%E9%A3%9F%E8%A8%98%5D%5B%E5%8F%B0%E5%8D%97%E5%B8%82%5D-%E5%B0%91%E7%88%BA%E6%89%8B%E4%BD%9C%E8%9B%8B%E9%A4%85-%E5%8B%9D%E5%88%A9%E5%BA%97'
        map_url = 'https://www.google.com/maps/search/%E5%B0%91%E7%88%BA%E8%9B%8B%E9%A4%85/@23.0144364,120.2201731,14z/data=!3m1!4b1'
        rec_url = 'https://ikachalife.com/854'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_chinese_omelet3(self, event):
        print("I'm entering chinese_omelet3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/3Y3PZeb.jpg'
        info_url = 'https://zineblog.com.tw/blog/post/200423'
        map_url = 'https://www.google.com/maps/place/%E5%A5%BD%E6%99%82%E8%BE%B0%E6%89%8B%E5%B7%A5%E8%9B%8B%E9%A4%85/@22.9824274,120.2055295,17z/data=!3m1!4b1!4m5!3m4!1s0x346e77a62d34571d:0xd5f8fc9f93bd6e8!8m2!3d22.982406!4d120.207717?hl=zh-TW'
        rec_url = 'https://ikachalife.com/854'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_beef_soup1(self, event):
        print("I'm entering beef_soup1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/kLNCrHO.jpg'
        info_url = 'https://ketty731.pixnet.net/blog/post/468806600-fresh_beef_soup'
        map_url = 'https://www.google.com/maps/place/%E6%96%B0%E9%AE%AE%E7%89%9B%E8%82%89%E6%B9%AF/@22.9863027,120.1854379,13z/data=!4m9!1m2!2m1!1z5paw6a6u54mb6IKJ5rmv!3m5!1s0x346e769a6efa9065:0x34cee10e53854876!8m2!3d22.9863027!4d120.2204568!15sCg_mlrDprq7niZvogonmua9aEyIR5paw6a6uIOeJm-iCiSDmua-SAQpyZXN0YXVyYW50'
        rec_url = 'https://anikolife.com/tainanbeefsoup/'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_beef_soup2(self, event):
        print("I'm entering beef_soup2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/sdD2I3t.jpg'
        info_url = 'https://anikolife.com/2016-12-12-1357/'
        map_url = 'https://www.google.com/maps/place/%E5%9C%93%E7%92%B0%E7%89%9B%E8%82%89%E6%B9%AF/@22.9911444,120.1914974,17z/data=!3m1!4b1!4m5!3m4!1s0x346e767a9e4e6607:0xb7b2f654e77520d!8m2!3d22.9911425!4d120.1936857?hl=zh-TW'
        rec_url = 'https://anikolife.com/tainanbeefsoup/'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_beef_soup3(self, event):
        print("I'm entering beef_soup3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/OrPuqcF.jpg'
        info_url = 'https://drm88.pixnet.net/blog/post/35702788-%E3%80%90%E5%8F%B0%E5%8D%97%E7%BE%8E%E9%A3%9F%E3%80%91%E8%A5%BF%E7%BE%85%E6%AE%BF%E7%89%9B%E8%82%89%E6%B9%AF%EF%BC%8C%E5%9C%A8%E5%9C%B0%E5%8F%B0%E5%8D%97%E4%BA%BA%E7%9A%84%E6%97%A9'
        map_url = 'https://www.google.com/maps/place/%E8%A5%BF%E7%BE%85%E6%AE%BF%E7%89%9B%E8%82%89%E6%B9%AF/@23.001514,120.2052554,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76f4d0a73ba1:0x74660490b99c2187!8m2!3d23.0014989!4d120.2074398'
        rec_url = 'https://anikolife.com/tainanbeefsoup/'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_savory_porridge1(self, event):
        print("I'm entering savory_porridge1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/wfcY7DN.jpg'
        info_url = 'https://foodieteller.com/yue-jin-rice/'
        map_url = 'https://www.google.com/maps/place/%E6%82%85%E6%B4%A5%E9%B9%B9%E7%B2%A5/@22.9976263,120.19853,17z/data=!3m1!4b1!4m5!3m4!1s0x346e7661419a9cd7:0x1baec53ff7846865!8m2!3d22.9975999!4d120.2007732'
        rec_url = 'https://www.businessweekly.com.tw/focus/blog/3008520'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_savory_porridge2(self, event):
        print("I'm entering savory_porridge2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/p88taKj.jpg'
        info_url = 'https://tenjo.tw/atang-congee/'
        map_url = 'https://www.google.com/maps/place/%E9%98%BF%E5%A0%82%E9%B9%B9%E7%B2%A5/@22.9899117,120.1957646,17z/data=!3m1!4b1!4m5!3m4!1s0x346e767b6d397c75:0x3777ee6a25659259!8m2!3d22.9899688!4d120.1978883'
        rec_url = 'https://www.businessweekly.com.tw/focus/blog/3008520'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_savory_porridge3(self, event):
        print("I'm entering savory_porridge3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/AP9Jew6.jpg'
        info_url = 'https://zineblog.com.tw/blog/post/42810898'
        map_url = 'https://www.google.com/maps/place/%E9%98%BF%E6%86%A8%E9%B9%B9%E7%B2%A5/@23.0015328,120.2041655,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76f55c7ef3d7:0xff66cd9852349479!8m2!3d23.0015328!4d120.2063542?hl=zh-TW'
        rec_url = 'https://www.businessweekly.com.tw/focus/blog/3008520'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_breakfast_western1(self, event):
        print("I'm entering breakfast_western1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/r9L3mKV.jpg'
        info_url = 'https://www.facebook.com/%E5%85%AD%E5%90%8B%E7%9B%A4-%E6%88%90%E5%A4%A7%E5%BA%97-101256752069392/'
        map_url = 'https://www.google.com/maps/place/%E5%85%AD%E5%90%8B%E7%9B%A4-%E6%88%90%E5%A4%A7%E5%BA%97/@22.9940738,120.218851,17z/data=!3m1!4b1!4m5!3m4!1s0x346e7776a4c4049d:0x5a3df25d366e7dc3!8m2!3d22.9940738!4d120.2210397'
        rec_url = 'https://zi.media/@AI-choiced/post/y0xFe3'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_breakfast_western2(self, event):
        print("I'm entering breakfast_western2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/TjQQSGi.jpg'
        info_url = 'https://dingeat.com/hali8hao/'
        map_url = 'https://www.google.com/maps/place/%E5%93%88%E5%88%A98%E8%99%9F%E6%97%A9%E9%A4%90/@22.9929591,120.1973637,17z/data=!3m1!4b1!4m5!3m4!1s0x346e766361101255:0x396aaae8d91064fb!8m2!3d22.9929591!4d120.1995524'
        rec_url = 'https://zi.media/@AI-choiced/post/y0xFe3'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()
