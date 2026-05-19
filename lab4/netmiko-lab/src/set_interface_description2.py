from netmiko import Netmiko 

device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
}

net_connect = Netmiko(**device)

output = net_connect.send_config_from_file("changes.txt")
print(output)

net_connect.disconnect()
