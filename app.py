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
        message = TextSendMessage(text='土砂龍\n爆錘龍\n骨錘龍\n蠻顎龍')
    elif msg == '魚龍種':
        message = TextSendMessage(text='泥魚龍\n熔岩龍')
    elif msg == '古龍種':
        message = TextSendMessage(text='麒麟\n鋼龍\n炎王龍\n屍套龍\n滅盡龍\n熔山龍')
    elif msg == '角龍':
        message = ImageSendMessage(original_content_url = 'https://forum.gamer.com.tw/C.php?bsn=5786&snA=137187', preview_image_url = 'https://forum.gamer.com.tw/C.php?bsn=5786&snA=137187')
    else:
        message = TextSendMessage(text=msg)

    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
