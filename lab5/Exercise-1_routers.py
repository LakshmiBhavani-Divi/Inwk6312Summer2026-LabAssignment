import yaml
import requests
from requests.auth import HTTPBasicAuth
import json

USER = "student"
PASS = "Meilab123"

with open("Exercise-1_routers.yaml") as f:
    data = yaml.safe_load(f)

for router in data["routers"]:
    host = router["host"]
    base_url = f"http://{host}/restconf/api/running/interfaces/interface/"

    for intf in router["interfaces"]:
        url = base_url + intf["name"]

        payload = {
            "ietf-interfaces:interface": {
                "name": intf["name"],
                "type": "iana-if-type:ethernetCsmacd",
                "enabled": True,
                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": intf["ip"],
                            "netmask": "255.255.255.0"
                        }
                    ]
                }
            }
        }

        headers = {
            'Content-Type': 'application/vnd.yang.data+json'
        }

        response = requests.put(url,
            auth=HTTPBasicAuth(USER, PASS),
            headers=headers,
            data=json.dumps(payload)
        )

        print(host, intf["name"], response.status_code)
