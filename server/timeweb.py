import requests
from config import TIMEWEB_TOKEN, TIMEWEB_SERVER_ID
import json


class Timeweb:
    def __init__(self):
        self.base_url = 'https://api.timeweb.cloud/api/v1'
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + TIMEWEB_TOKEN
        })

    def get_server(self):
        url = self.base_url+'/servers/'+str(TIMEWEB_SERVER_ID)
        response = self.session.get(url)
        server_data = json.loads(response.text).get('server')
        
        data = {
            'status': server_data.get('status'),
            'cpu': server_data.get('cpu'),
            'cpu_frequency': server_data.get('cpu_frequency'),
            'ram': server_data.get('ram'),
            'disk': {
                'size': server_data.get('disks')[0].get('size'),
                'used': server_data.get('disks')[0].get('used'),
            }
        }
        return data
    
    
if __name__ == '__main__':
    timeweb = Timeweb()
    print(timeweb.get_server())