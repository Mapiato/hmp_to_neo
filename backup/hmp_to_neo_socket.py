import csv
import json
import os
import requests
import shutil
import time
from copy import deepcopy


lookup = {
    'TimeStamp': 'TIMESTAMP',
    '': '',
    '0': '',
    '1': '0',
    '2': '0',
    '3': '18040237',
    '4': '18040238',
    '5': '18110236',
    '6': '18110144',
    '7': '18110139',
    '8': '', 
    '9': '',
    '10': '',
    '11': '18040239',
    '12': '18040219',
    '13': '18040215',
    '19': '18040218',
    '20': '18040220',
    '21': '18040231',
    '22': '29084119',
    '27': '18110138',
    '28': '18110135',
    '29': '18110124',
    '30': '18110125'
}
'''
folder setup for testing:
directory = './csv_input/'
storage = './storage/'

'''
directory = 'C:\\Users\\HMP\\AppData\\Local\\VirtualStore\\Program Files (x86)\\HMP 2.58\\'
storage = 'C:\\Users\\HMP\\AppData\\Local\\VirtualStore\\Program Files (x86)\\HMP 2.58\\processed\\'

while True:
    for filename in os.listdir(directory):
        if filename.endswith(".csv") and filename.startswith("Exp"):
            print(os.path.join(directory, filename))
            source = os.path.join(directory, filename)

            with open(source) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                for row in reader:
                    print(row)
                    
        
                    device = {}
                    data = []
        
                    
                    for k in row.keys():
                        if k != 'TimeStamp' or '':
                            device['DEVICE'] = lookup[k]
                            device['VTI'] = row[k]
                            data.append(deepcopy(device))
                    data.pop(-1)                    
                    payload_dict = {'PROTOCOL': 'HMPDataExport', 'TimeStamp': row['TimeStamp'], 'DATA:':  data}                    
                    pl = json.dumps(payload_dict)
                    print(pl)
                    
                    url = "http://172.16.42.1:9995"
                    headers = {'Content-type': 'application/json'}
                    #r = requests.post(url, json=payload_dict, headers=headers)
                    r = requests.post(url, data=str(pl), headers=headers)
                    print(r.status_code)
                    print(r.text)
                    

            processed = shutil.move(source, storage)
            print("File processed and moved to ", storage)
    time.sleep(10)