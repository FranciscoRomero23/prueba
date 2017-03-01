#-*- coding:utf-8 -*-

from lxml import etree
doc = etree.parse('comercios.xml')
comercios = doc.getroot()

datos=[]

comercio=raw_input("Dime el nombre del comercio: ")

for com in comercios:
	nombre=com.find("NOM_COMERCIAL").text
	if nombre == comercio:
		nombre=com.find("NOM_COMERCIAL").text
		telefono=com.find("TFNO").text
		fax=com.find("FAX").text
		email=com.find("EMAIL").text
		web=com.find("WEB").text

		print "Nombre:",nombre
		print "Telefono:",telefono
		print "Fax:",fax
		print "Email:",email
		print "Web:",web
