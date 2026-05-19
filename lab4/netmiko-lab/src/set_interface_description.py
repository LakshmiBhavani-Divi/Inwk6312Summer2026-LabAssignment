from netmiko import Netmiko 

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
    }
]

config = [
    "interface GigabitEthernet3",
    "description Configured via Netmiko"
]

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_config_set(config)
    print(output)
    net_connect.disconnect()
