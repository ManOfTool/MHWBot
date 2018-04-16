from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Tw7ffpyN4FG/vehyKAUyViwanhCD0GWEYwgWGpemLQZt/FmyxhiBvjzx99TopUiHJc/vac0UOHx7+4jRHevn9u/VA68w0UVFoxt3iU45HI8HgDW5DJsG0cAgn+58BjiCSPNXkh+NuoKchckiElLBSQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('91df27ee5a241496ff870c23b3ef34d1')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text

    if msg == '飛龍種':
        message = TextSendMessage(text='雄火龍\n雌火龍\n蒼火龍\n櫻火龍\n角龍\n黑角龍\n風飄龍\n浮空龍')
    elif msg == '牙龍種':
        message = TextSendMessage(text='大凶豺龍\n大凶顎龍\n岩賊龍\n飛雷龍\n慘爪龍')
    elif msg == '鳥龍種':
        message = TextSendMessage(text='搔鳥\n眩鳥\n毒妖鳥')
    elif msg == '獸龍種':
        message = TextSendMessage(text='土砂龍\n爆鎚龍\n骨鎚龍\n蠻顎龍\n恐暴龍')
    elif msg == '魚龍種':
        message = TextSendMessage(text='泥魚龍\n熔岩龍')
    elif msg == '古龍種':
        message = TextSendMessage(text='麒麟\n鋼龍\n炎王龍\n屍套龍\n滅盡龍\n熔山龍')
    elif msg == '角龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518400220/diablos.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518400220/diablos.jpg')
    elif msg == '黑角龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401005/black_diablos.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401005/black_diablos.jpg')
    elif msg == '雄火龍' or msg == '火龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401017/male_fire.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401017/male_fire.jpg')
    elif msg == '雌火龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401016/female_fire.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401016/female_fire.jpg')
    elif msg == '蒼火龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401005/blue_fire.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401005/blue_fire.jpg')
    elif msg == '櫻火龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401019/sakura_fire.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401019/sakura_fire.jpg')
    elif msg == '風飄龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401016/ice_bird.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401016/ice_bird.jpg')
    elif msg == '浮空龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401015/floating_marshmalow.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401015/floating_marshmalow.jpg')
    elif msg == '爆鱗龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401005/bomber.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401005/bomber.jpg')
    elif msg == '大凶豺龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518402759/big_lizard.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518402759/big_lizard.jpg')
    elif msg == '大凶顎龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518402759/black_lizard.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518402759/black_lizard.jpg')
    elif msg == '岩賊龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518402838/blue_lizard.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518402838/blue_lizard.jpg')
    elif msg == '飛雷龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401019/pikachu.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401019/pikachu.jpg')
    elif msg == '慘爪龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401019/red_dog.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401019/red_dog.jpg')
    elif msg == '搔鳥':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401016/holding_rock.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401016/holding_rock.jpg')
    elif msg == '眩鳥':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401018/light.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401018/light.jpg')
    elif msg == '毒妖鳥':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401020/poison_bird.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401020/poison_bird.jpg')
    elif msg == '土砂龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518402759/muddy.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518402759/muddy.jpg')
    elif msg == '爆鎚龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401005/big_chin.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401005/big_chin.jpg')
    elif msg == '骨鎚龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401005/bone_chin.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401005/bone_chin.jpg')
    elif msg == '蠻顎龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401019/rousing_nose.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401019/rousing_nose.jpg')
    elif msg == '泥魚龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401017/mud_fish.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401017/mud_fish.jpg')
    elif msg == '熔岩龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401017/lava_fish.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401017/lava_fish.jpg')
    elif msg == '麒麟':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401016/kirin.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401016/kirin.jpg')
    elif msg == '鋼龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518403112/windy_steel.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518403112/windy_steel.jpg')
    elif msg == '炎王龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401017/flame.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401017/flame.jpg')
    elif msg == '屍套龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518403015/walking_dead.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518403015/walking_dead.jpg')
    elif msg == '滅盡龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401005/destroyer.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401005/destroyer.jpg')
    elif msg == '熔山龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401018/lava_mountain.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401018/lava_mountain.jpg')
    elif msg == '冥燈龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401016/lantern.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1518401016/lantern.jpg')
    elif msg == '恐暴龍':
        message = ImageSendMessage(original_content_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1521723041/cucumber.jpg', preview_image_url = 'https://res.cloudinary.com/hxrp4uqty/image/upload/v1521723041/cucumber.jpg')

    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
