import gettext
import re
from common.hardware import HARDWARE, ANDROID, PC

supported_language = ['en-US', 'ar-EG']
localedir = '../assets/locales'

if ANDROID:

  local = android.getprop(ro.product.locale)
else:
  local = supported_language[0]

i18n = gettext.translation('messages', localedir=localedir, fallback=True, languages=local)

i18n.install()

convert_to_symbol = False
symbol_map = {'ar_EG':{'0':'٠','1':'١','2':'٢','3':'٣','4':'٤','5':'٥','6':'٦','7':'٧','8':'٨','9':'٩'},}
def symble_lookup(re_match):
  return symbol_map[local][re_match.group(0)]
def numtosym(text):
  if convert_num and local in symbol_map:
    return re.sub("\d", symble_lookup, text)
  else:
    return num

def _(message):
  return numtosym(i18n.gettext(message))
