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
	'古龍種': '麒麟\n鋼龍\n炎王龍\n炎妃龍\n屍套龍\n滅盡龍\n熔山龍\n爛輝龍\n貝希摩斯'
}

monsters = {
	'角龍': 'mhw/DIABLOS',
	'黑角龍': 'mhw/BDIABLOS',
	'雄火龍': 'mhw/RATHALOS',
	'蒼火龍': 'mhw/ARATHALOS',
	'雌火龍': 'mhw/RATHIAN',
	'櫻火龍': 'mhw/PRATHIAN',
	'風漂龍': 'mhw/LEGIANA',
	'浮空龍': 'mhw/PAOLUMU',
	'爆鱗龍': 'mhw/BAZELGEUSE',
	'大凶豺龍': 'mhw/GJAGRAS',
	'大凶顎龍': 'mhw/GGIRROS',
	'岩賊龍': 'mhw/DODOGAMA',
	'飛雷龍': 'mhw/TKADACHI',
	'慘爪龍': 'mhw/ODOGARON',
	'搔鳥': 'mhw/KYK',
	'眩鳥': 'mhw/TTYK',
	'毒妖鳥': 'mhw/mhw/PUKEI',
	'土砂龍': 'mhw/BARROTH',
	'蠻顎龍': 'mhw/ANJANATH',
	'暴錘龍': 'mhw/URAGAAN',
	'骨錘龍': 'mhw/RADOBAAN',
	'泥魚龍': 'mhw/JYURATODUS',
	'熔岩龍': 'mhw/LAASIOTH',
	'麒麟': 'mhw/KIRIN',
	'鋼龍': 'mhw/KDAORA',
	'炎王龍': 'mhw/TEOSTRA',
	'炎妃龍': 'mhw/LUNASTRA',
	'屍套龍': 'mhw/VAALHAZAK',
	'滅盡龍': 'mhw/NERGIGANTE',
	'熔山龍': 'mhw/ZMAGDAROS',
	'冥燈龍': 'mhw/XENOJIIVA',
	'恐暴龍': 'mhw/DEVILJHO',
	'絢輝龍': 'mhw/KULVETAROTH',
	'貝希摩斯': 'mhw/BEHEMOTH',
	'鹿首精': 'mhw/LESHY',
	'古代鹿首精': 'mhw/KERNUN'
}