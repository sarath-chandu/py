from netmiko import ConnectHandler

iosv_12 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.10.22',
    'username': 'cisco',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_12)
#net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
print output

config_commands = ['int loop 10', 'ip address 5.5.5.5 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print output