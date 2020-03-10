import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat(".ages/json").st_size != 0:
    