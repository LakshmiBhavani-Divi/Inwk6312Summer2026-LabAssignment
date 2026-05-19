from netmiko import ConnectHandler 

devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
    }
]

for device in devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show interface description")
    net_connect.disconnect()

    print("="*50)
    print(output)
