// #include <libintl.h>
// #include <locale.h>
#include "gettext.h"

setlocale (LC_ALL, "");
// setlocale (LC_CTYPE, "");
// setlocale (LC_MESSAGES, "");
bindtextdomain (PACKAGE, LOCALEDIR);
textdomain (PACKAGE);

#define _(STRING) gettext(STRING)
