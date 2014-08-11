# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils import timezone

# Create your models below.
class Node(models.Model):
	"""
	CHOICES = (
		("Pings", "Ping"),
		("Traceroutes", "Traceroute"),
		("Nmaps", "Nmap"),
	)
	"""
	name = models.CharField(max_length=25, unique=True)
	created = models.DateTimeField('Создано:')
	avg_ping = models.CharField(max_length=15)
	hops = models.CharField(max_length=15)
	scan = models.CharField(max_length=15)
	#relatives = models.CharField(max_length=7, choices=CHOICES)

class Ping(models.Model):
	node = models.ForeignKey(Node)
	average = models.CharField(max_length=200)
	date = models.DateTimeField('Дата тестирования')

class Traceroute(models.Model):
	node = models.ForeignKey(Node)
	hop = models.CharField(max_length=100)
	date = models.DateTimeField('Дата тестирования')

class Nmap(models.Model):
	node = models.ForeignKey(Node)
	ports = models.CharField(max_length=100)
	date = models.DateTimeField('Дата тестирования')