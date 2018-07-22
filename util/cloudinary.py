import cloudinary
import cloudinary.api
from util.config import CLOUD_NAME, API_KEY, API_SECRET

cloudinary.config(
	cloud_name = CLOUD_NAME,
	api_key = API_KEY,
	api_secret = API_SECRET
)

catagory = {
	'飛龍種': '雄火龍\n雌火龍\n蒼火龍\n櫻火龍\n角龍\n黑角龍\n風飄龍\n浮空龍',
	'牙龍種': '大凶豺龍\n大凶顎龍\n岩賊龍\n飛雷龍\n慘爪龍',
	'鳥龍種': '搔鳥\n眩鳥\n毒妖鳥',
	'獸龍種': '土砂龍\n爆鎚龍\n骨鎚龍\n蠻顎龍\n恐暴龍',
	'魚龍種': '泥魚龍\n熔岩龍',
	'古龍種': '麒麟\n鋼龍\n炎王龍\n炎妃龍\n屍套龍\n滅盡龍\n熔山龍\n爛輝龍'
}

monsters = {
	'角龍': 'DIABLOS',
	'黑角龍': 'BDIABLOS',
	'雄火龍': 'RATHALOS',
	'蒼火龍': 'ARATHALOS',
	'雌火龍': 'RATHIAN',
	'櫻火龍': 'PRATHIAN',
	'風漂龍': 'LEGIANA',
	'浮空龍': 'PAOLUMU',
	'爆鱗龍': 'BAZELGEUSE',
	'大凶豺龍': 'GJAGRAS',
	'大凶顎龍': 'GGIRROS',
	'岩賊龍': 'DODOGAMA',
	'飛雷龍': 'TKADACHI',
	'慘爪龍': 'ODOGARON',
	'搔鳥': 'KYK',
	'眩鳥': 'TTYK',
	'毒妖鳥': 'PUKEI',
	'土砂龍': 'BARROTH',
	'蠻顎龍': 'ANJANATH',
	'暴錘龍': 'URAGAAN',
	'骨錘龍': 'RADOBAAN',
	'泥魚龍': 'JYURATODUS',
	'熔岩龍': 'LAASIOTH',
	'麒麟': 'KIRIN',
	'鋼龍': 'KDAORA',
	'炎王龍': 'TEOSTRA',
	'炎妃龍': 'LUNASTRA',
	'屍套龍': 'VAALHAZAK',
	'滅盡龍': 'NERGIGANTE',
	'熔山龍': 'ZMAGDAROS',
	'冥燈龍': 'XENOJIIVA',
	'恐暴龍': 'DEVILJHO',
	'絢輝龍': 'KULVETAROTH'
}