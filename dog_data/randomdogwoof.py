#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 00:59:23 2019

@author: bhargav
"""

import requests

for i in range(5):
    API_URL = 'https://random.dog/woof.json'
    #API_KEY = 'i0cgsdYL3hpeOGkoGmA2TxzJ8LbbU1HpbkZo8B3kFG2bRKjx3V'
    #headers = {'UserAPI-Key': API_KEY}
    response = requests.get('{}'.format(API_URL))
    data = response.json()
    print(data['url'])
    fileurl = data['url']
    import wget
    file_name = wget.download(fileurl)