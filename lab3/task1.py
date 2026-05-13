Task 1 – Rendering a Jinja Template File in Python
from jinja2 import Environment, FileSystemLoader

# Load template
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template.j2")

# Create class
class NetworkInterface(object):
    def __init__(self, name, description, vlan, uplink=False):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink

# Create object
interface_obj = NetworkInterface("GigabitEthernet0/1", "Server Port", 10)

# Render template
print(template.render(interface=interface_obj))
