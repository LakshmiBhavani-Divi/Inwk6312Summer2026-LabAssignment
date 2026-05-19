import yaml 
from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko

hosts = yaml.load(open('hosts.yml'), Loader=yaml.SafeLoader)
interfaces = yaml.load(open('interfaces.yml'), Loader=yaml.SafeLoader)

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('interfaces_config_template.j2')

config = template.render(data=interfaces)

for host in hosts["hosts"]:
    net_connect = Netmiko(
        host=host["name"],
        username=host["username"],
        password=host["password"],
        device_type=host["type"]
    )
    print(f"Logged into {host['name']} successfully")
    output = net_connect.send_config_set(config.split("\n"))
    print(output)
    print(f"Pushed config into {host['name']} successfully")
    net_connect.disconnect()
print("Done!")
