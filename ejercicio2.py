#-*- coding:utf-8 -*-

from lxml import etree
doc = etree.parse('comercios.xml')
comercios = doc.getroot()

print "2. Contar la cantidad de comercios por zona."

zonas=[]
cantzona=[]

for com in comercios:
	zona=com.find("ZONA").text
	if zona not in zonas:
		zonas.append(zona)
		cantzona.append(0)

cuenta=len(zonas)

for com in comercios:
	zona=com.find("ZONA").text
	for num in xrange(1,cuenta+1):
		if zona == zonas[num-1]:
			cantzona[num-1]=cantzona[num-1]+1

for num in xrange(1,cuenta+1):
	print zonas[num-1],cantzona[num-1]
