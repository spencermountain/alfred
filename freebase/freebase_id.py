import cStringIO
import urllib2
import json
import re

q= '{query}'
# q= "type river"
q= q.strip()

t= "/common/topic"
reg="^type "
if re.search(reg, q):
  t='/type/type'
  q= re.sub(reg,'', q)

reg="^person "
if re.search(reg, q):
  t='/people/person'
  q= re.sub(reg,'', q)

reg="^location "
if re.search(reg, q):
  t='/location/location'
  q= re.sub(reg,'', q)

reg="^property "
if re.search(reg, q):
  t='/type/property'
  q= re.sub(reg,'', q)

key= "AIzaSyD5GmnQC7oW9GJIWPGsJUojspMMuPusAxI" #please don't abuse my key ;)
URL= "https://www.googleapis.com/freebase/v1/search?query=" + q + "&limit=1&type=" + t + "&key=" + key
data_string= urllib2.urlopen(URL).read()
result = json.loads(data_string)
if t == '/type/type' or t == "/type/property":
  print result['result'][0]['id']
else:
  print result['result'][0]['mid']