#
# 3FCG 
# 3FactorCodeGenerator
#

# > How to use?
# Just import this file to your project and then call function genCode(key) or function valCode(code, key) from class tfcg
# In args include your key

# > How it works?
# By gmt time, gmt date and secret key that formatting and hashing by md5 and then returning 6 first symbols in uppercase

import hashlib
import time

class tfcg:
    def genCode(key):
        gmt = time.gmtime(time.time())
        strToFormat = f"___{key}__{gmt.tm_hour}_{str(gmt.tm_min)[0]}__{gmt.tm_mday}_{gmt.tm_mon}_{gmt.tm_year}___"
        md5Hash = hashlib.md5(strToFormat.encode()).hexdigest()
        return md5Hash[:6].upper()

    def valCode(code, key):
        gmt = time.gmtime(time.time())
        strToFormat = f"___{key}__{gmt.tm_hour}_{str(gmt.tm_min)[0]}__{gmt.tm_mday}_{gmt.tm_mon}_{gmt.tm_year}___"
        md5Hash = hashlib.md5(strToFormat.encode()).hexdigest()
        return code == md5Hash[:6].upper()
