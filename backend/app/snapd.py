from operator import mul
from urllib import response
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
from .helpers import SnapdAdapter

class SnapdClient():
    def __init__(self):
        self.session = requests.Session()
        self.session.mount("http://snapd/", SnapdAdapter())
    
    def snap_system_info(self):
        response = self.session.get("http://snapd/v2/system-info")
        return response.json()

    def refresh(self):
        response = self.session.post("http://snapd/v2/snaps", json={"action": "refresh"})
        return response.json()

    def revert(self, snap):
        response = self.session.post("http://snapd/v2/snaps/"+snap, json={"action": "revert"})
        return response.json()
    

    def side_load_snap(self, snap, path):

        multipart_form_data = {
            'devmode': True,
            'filename': path
        }

        snap_file = {
            'snap': (open(snap, 'rb'))
        }

        response = self.session.post("http://snapd/v2/snaps", files=snap_file, data=multipart_form_data)
        return response.json()



