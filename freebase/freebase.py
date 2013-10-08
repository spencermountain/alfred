
# Created by spencer owen
# https://github.com/spudstud/alfred-bitcoin-workflow

# User can change which number(s) are returned by editing currentValue

import json
import urllib2
from xml.etree.ElementTree import Element, SubElement, Comment,  tostring

# Api v2 url for rates
url="http://data.mtgox.com/api/2/BTCUSD/money/ticker"
jsonURL=urllib2.urlopen(url)
jsonObject=json.load(jsonURL)
currentValue="yeaaaah"

items = Element('items')

item = SubElement(items, 'item')
item.set('uid', 'mtgoxprice')
item.set('arg', str(currentValue)) # arg allows you to pass a string to other displays (notification center)
item.set('valid', 'yes')

title = SubElement(item, 'title')
title.text = "MtGox Current Rate"

subtitle = SubElement(item, 'subtitle')
subtitle.text = str(currentValue)

icon = SubElement(item, 'icon')
icon.text = "MtGox.png"

print tostring(items)
