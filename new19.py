from netmiko import ConnectHandler

iosv_12_s2 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.10.22',
    'username': 'cisco',
    'password': 'cisco',
}

iosv_12_s3 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.10.23',
    'username': 'cisco',
    'password': 'cisco',
}

all_devices = [iosv_12_s2, iosv_12_s3]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    config_commands =  ['int loop 20', 'ip address 6.6.6.6 255.255.255.0', 'router ospf 100', 'network 0.0.0.0 0.0.0.0 area 0']
    output = net_connect.send_config_set(config_commands)
    print output