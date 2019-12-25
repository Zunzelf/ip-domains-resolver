from securitytrails import securitytrails
from tqdm import tqdm
from os import system as sys, path
import shutil 
import json


def get_domains(url, key):
    s = securitytrails(api_key=key) 
    res_req = json.loads(s.get_subdomain(url))

    sub_domains = res_req["subdomains"]
    res = []
    for sub in sub_domains:
        res.append("%s.%s"%(sub, url))
    return res
