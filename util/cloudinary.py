import cloudinary
import cloudinary.api
from util.config import CLOUD_NAME, API_KEY, API_SECRET

cloudinary.config(
	cloud_name = CLOUD_NAME,
	api_key = API_KEY,
	api_secret = API_SECRET
)

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