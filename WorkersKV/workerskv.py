import json
import requests

from WorkersKV.configs import read_token

BASE_URL = 'https://api.cloudflare.com/client/v4'
HEADERS = {"Content-Type": "application/json"}


class WorkersKV(object):
    def __init__(self, account, namespace):
        self.token = read_token()
        self.headers = HEADERS
        self.headers["Authorization"] = "Bearer " + self.token
        self.base_url = (
            BASE_URL + "/accounts/" + str(account) + "/storage/kv/namespaces/" + str(namespace)
        )

    def list_keys(self):
        response = requests.get(
            self.base_url + "/keys",
            headers=self.headers
        )
        return response

    
    def get(self, key):
        response = requests.get(
            self.base_url + "/values/" + key,
            headers=self.headers
        )
        return response

    
    def put(self, key, value):
        response = requests.put(
            self.base_url + "/values/" + key,
            headers=self.headers,
            data=value
        )
        return response


    def bulk_put(self, key):
        # WIP
        return None


    def delete(self, key):
        response = requests.delete(
            self.base_url + "/values/" + key,
            headers=self.headers
        )
        return response
    
    def bulk_delete(self, key):
        # WIP
        return None