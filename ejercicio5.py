#-*- coding:utf-8 -*-

from lxml import etree
doc = etree.parse('comercios.xml')
comercios = doc.getroot()

datos=[]

cadena=raw_input("Dime una cadena: ")
longitud=len(cadena)
for com in comercios:
	contacto=com.find("CONTACTO").text
	if cadena == contacto[:longitud]:
	
		nombre=com.find("NOM_COMERCIAL").text
		print nombre
