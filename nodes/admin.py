from django.contrib import admin
from nodes.models import Node, Ping, Traceroute, Nmap

# Register your models here.

admin.site.register(Node)