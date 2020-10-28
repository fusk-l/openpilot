import gettext
import re
from common.params import Params
from common.hardware import HARDWARE, ANDROID, PC

supported_language = ['en-US', 'ar-EG']
localedir = '../assets/locales'

if ANDROID:
  local = Params().get('AndroidLocal').decode('utf8')
else:
  local = supported_language[0]

i18n = gettext.translation('messages', localedir=localedir, fallback=True, languages=local)

i18n.install()

number_to_symbol = False
symbol_map = {'ar_EG':['٠','١','٢','٣','٤','٥','٦','٧','٨','٩',],}
def symble_lookup(re_match):
  return symbol_map[local][int(re_match.group(0))]
def numtosym(text):
  if number_to_symbol and local in symbol_map:
    return re.sub("\d", symble_lookup, text)
  else:
    return num

def _(message):
  return numtosym(i18n.gettext(message))
