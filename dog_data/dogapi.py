import requests

for i in range(500000):
    API_URL = 'https://dog.ceo/api/breeds/image/random'
    #API_KEY = 'i0cgsdYL3hpeOGkoGmA2TxzJ8LbbU1HpbkZo8B3kFG2bRKjx3V'
    #headers = {'UserAPI-Key': API_KEY}
    response = requests.get('{}'.format(API_URL))
    data = response.json()
    print(str(i) + " " + data['status'] + "-" + data['message'])
    if(data['status'] == "success"):
        fileurl = data['message']
        urlsplit = fileurl.split('/')
        breed = urlsplit[4]
        fname = urlsplit[5]
        newfilename = "images/"+breed+"---"+fname
#        print(breed+"---"+fname)
#        print(newfilename)
        import wget
        file_name = wget.download(fileurl)
        import os
        os.rename(fname, newfilename)