from django.forms.models import modelformset_factory
from nodes.models import Node, Ping, Traceroute, Nmap

NodeFormSet = modelformset_factory(Node)
formset = NodeFormSet()

print(formset)