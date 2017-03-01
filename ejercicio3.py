#-*- coding:utf-8 -*-

from lxml import etree
doc = etree.parse('comercios.xml')
comercios = doc.getroot()

nombres=[]

zonapedida=raw_input("Dime la zona que debo buscar: ")

for com in comercios:
	zona=com.find("ZONA").text
	if zona == zonapedida:
		nombres.append(com.find("NOM_COMERCIAL").text)

for nom in nombres:
	print nom
