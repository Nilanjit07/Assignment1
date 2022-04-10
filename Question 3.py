hacker_legends = ['LulzSec', 'Gary McKinnon', 'Adrian Lamo', 'Jonathan James', 'Kevin Poulsen']

hacker_legends.append('Anonymous')
print(hacker_legends)

networking = ['packet', 'LAN', 'WAN', 'port', 'firewall', 'VPN']

networking.insert(3, 'SSH')
print(networking)

ip_addy = [255.224, 192.168,  1331904083.25, 5102018, 10.255, 172.31]

ip_addy.remove(5102018)
print(ip_addy)

cyber_traits = ['detailed oriented', 'methodically', 'lazy', 'persistent', 'curious', 'instinctive']

cyber_traits.pop(2)
print(cyber_traits)

sec_co = ['IBM', 'Raytheon', 'Mimecast', 'Cisco']
new_co= ['Checkp Point Software', 'Palo Alto Networks', 'Symantec', 'Trend Micro']

sec_co.extend(new_co)
print(sec_co)

dns_list = [98.105, 98.1115, 99.105, 98.111, 98.105, 98.106, 98.501]

print(dns_list.count(98.105))


mr_robot = ['bigger', 'something', 'represents', 'it', 'mistake', 'a', 'just', 'never', 'is', 'bug', 'a']

mr_robot.reverse()
print(mr_robot)

ssh_list = [1331903959.94555, 1331901011.84795, 1331903492.37203, 1331901032.03789, 1331903508.24007, 1331903476.8]

ssh_list.sort()
print(ssh_list)

ssh_list.sort(reverse=True)
print(ssh_list)

network_list = [39104, 38694, 38702, 38787, 39860]
print(max(network_list))

network_list = [39104, 38694, 38702, 38787, 39860]
print(min(network_list))
