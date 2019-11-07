#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 01:39:07 2019

@author: bhargav
"""

import requests

for i in range(2):
    API_URL = 'http://shibe.online/api/shibes?count=100&urls=true'
    #API_KEY = 'i0cgsdYL3hpeOGkoGmA2TxzJ8LbbU1HpbkZo8B3kFG2bRKjx3V'
    #headers = {'UserAPI-Key': API_KEY}
    response = requests.get('{}'.format(API_URL))
    data = response.json()
    fileurl = data['url']
    import wget
    file_name = wget.download(fileurl)