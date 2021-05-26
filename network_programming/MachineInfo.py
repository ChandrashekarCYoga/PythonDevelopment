#!/usr/bin/env python
# Python Network Programming Cookbook,

# This program is optimized for Python 2.7.12
#   and Python 3.5.2.
# It may run on any other version with/without
# modifications.

import socket
from binascii import hexlify


def print_machine_info():
  host_name = socket.gethostname()
  ip_address = socket.gethostbyname(host_name)
  print(f"Host name: {host_name}")
  print(f"IP address: {ip_address}")


def get_remote_machine_info(remote_host):
  # remote_host = 'www.yogicways.in'
  try:
    print(f'IP address of {remote_host} : {socket.gethostbyname(remote_host)}')
  except socket.error as err_msg:
    print(f'{remote_host} : {err_msg}')

def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print ("IP Address: %s => Packed: %s, Unpacked: %s" %(ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr))

def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25]:
        print ("Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname)))
    
    print ("Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp')))

if __name__ == '__main__':
    print_machine_info()
    get_remote_machine_info('www.yogicways.in')
    get_remote_machine_info('www.google.com')
    convert_ip4_address()
    find_service_name()
    
