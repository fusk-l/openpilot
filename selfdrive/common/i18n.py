import gettext
from common.hardware import HARDWARE, ANDROID, PC

supported_language = ['en-US', 'ar-EG']
localedir = '../assets/locales'

if ANDROID:
  
  local = android.getprop(ro.product.locale)
else:
  local = supported_language[0]

i18n = gettext.translation('messages', localedir=localedir, fallback=True, languages=local)

i18n.install()

_ = i18n.gettext
