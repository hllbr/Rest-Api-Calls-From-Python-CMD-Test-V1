>>>>python
>>>>import requests
>>>>url = 'https://jsonplaceholder.typicode.com/photos'
>>>>response = requests.get(url)
>>>>print(response.json())
>>>>jsonPayload = {'albumId':1,'title':'test','url':'nothing.com','thumbnailUrl':'nothing.com'}
>>>>response = requests.post(url,json= jsonPayload)
>>>>response.json()
>>>>url = 'https://jsonplaceholder.typicode.com/photos/100'
>>>>response = requests.put(url,json =jsonPayload)
>>>>response.json()
>>>>response = requests.delete(url)
>>>>response.json()
