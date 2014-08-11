# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.forms.models import modelformset_factory
from nodes.models import Node, Ping, Traceroute, Nmap
import datetime
import xmlrpclib
import re

# Create your views below.
def index(request):
	return HttpResponse("Привет мир! :)")

def add_form(request):
	#formset = formseting(request, Node)
	message = "Какой адрес вы хотите протестировать? Введите его в форму выше! "
	return render_to_response("add_form.html", {"message": message, })


def add(request):
	destination = "127.0.0.1"
	message = "Какой адрес вы хотите протестировать? Введите его в форму выше! "
	proxy = xmlrpclib.ServerProxy('http://localhost:8080')
	if 'node' in request.GET:
		destination = request.GET['node']
		if correct(destination):
			if not exist(destination, Node):
				nodes = Node.objects.create(name = destination,
											created = datetime.date.today(),
											avg_ping = "Current average ping time",
											hops = "Number of hops",
											scan = "Scanned for: seconds",
											)
				nodes.avg_ping = ping(destination, proxy, nodes)
				nodes.hops = traceroute(destination, proxy, nodes)
				nodes.scan = nmap(destination, proxy, nodes)
				nodes.save()
			else:
				nodes = Node.objects.get(name = destination)
				nodes.avg_ping = ping(destination, proxy, nodes)
				nodes.hops = traceroute(destination, proxy, nodes)
				nodes.scan = nmap(destination, proxy, nodes)
				nodes.save()
			message = "Узел %r успешно протестирован!" % str(destination)
		else: message = "Ошибка в адресе. Введите правильный URL или IP, например 127.0.0.1 или yandex.ru"
	else: message = "Добро пожаловать на страницу тестирования!"

	Nodes = Node.objects.all()
	database = Ping.objects.all()
	return render_to_response("add_form.html", {"message": message,
												"Nodes": Nodes,
												"database": database,
												})

def choose_db(request):
	dbField = Ping
	Nodes = Node.objects.all()
	database = Ping.objects.all().filter(node_id = 1)
	message = "Something"
	if 'dbFields' in request.GET:
		dbField = request.GET['dbFields']
		if 'filter' in request.GET:
			node = request.GET['filter']
			if node != "all":
				id_filter = Node.objects.get(name = node)
				if dbField == "Ping":
					database = Ping.objects.all().filter(node_id = id_filter.id)
				elif dbField == "Traceroute":
					database = Traceroute.objects.all().filter(node_id = id_filter.id)
				elif dbField == "Nmap":
					database = Nmap.objects.all().filter(node_id = id_filter.id)

				message = "Показана таблица %r по узлу %r" % (str(dbField), str(node))

			else:
				if 'dbFields' in request.GET:
					dbField = request.GET['dbFields']
				if dbField == "Ping":
					database = Ping.objects.all()
				elif dbField == "Traceroute":
					database = Traceroute.objects.all()
				elif dbField == "Nmap":
					database = Nmap.objects.all()

				message = "Показана таблица %r по всем узлам" % str(dbField)


	return render_to_response("add_form.html", {"Nodes": Nodes,
												"database": database,
												"dbField": dbField,
												"message": message,
												})
"""
def table(request):
	Nodes = Node.objects.all()
	Pings = Ping.objects.all()
	Nmaps = Nmap.objects.all()
	Traceroutes = Traceroute.objects.all()
	return render_to_response("table.html", {"Nodes": Nodes,
												"Pings": Pings,
												"Nmaps": Nmaps,
												"Traceroutes": Traceroutes,
												})
"""
def correct(destination):
	correct = re.search("(\d+.\d+.\d+.\d+)|(\w+\\.com|\\.ru)", destination)
	return correct

def exist(destination,db):
	exist = False
	bd = db.objects.all()
	for element in bd:
		if element.name == destination:
			exist = True
			break
	return exist

def ping(destination, proxy, nodes):
	ping = Ping.objects.create(node = nodes, average = proxy.ping(destination), date = datetime.datetime.today())
	curr_ping = ping.average
	return curr_ping

def traceroute(destination, proxy, nodes):
	traceroute = Traceroute.objects.create(node = nodes, hop = proxy.traceroute(destination), date = datetime.datetime.today())
	found = re.search("(\d+)  (\d+.\d+.\d+.\d+)  (\d+.\d+) ms  (\d+.\d+) ms  (\d+.\d+) ms$", traceroute.hop)
	if found: result = found.group(1)
	else: result = "Недоступен"
	return result

def nmap(destination, proxy, nodes):
	nmap = Nmap.objects.create(node = nodes, ports = proxy.nmap(destination), date = datetime.datetime.today())
	found = re.search("Nmap done: (\d+) IP address \((\d+) host up\) scanned in (\d+.\d+) seconds", nmap.ports)
	if found: result = found.group(3)
	else: result = "Недоступен"
	return result




