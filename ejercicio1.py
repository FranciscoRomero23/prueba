#-*- coding:utf-8 -*-

from lxml import etree
doc = etree.parse('comercios.xml')
comercios = doc.getroot()

print "1. Lista los comercios con pagina web."

web=0
for com in comercios:
	if com.find("WEB").text != "NO DISPONIBLE":
		web = web +1
print "Hay",web,"comercios con página web."

