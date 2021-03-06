from pprint import pprint

import requests
import config.adss


def get_captcha():
    base_url = config.adss.server_ip()
    url = base_url + 'captcha/block_puzzle'
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    r = requests.get(url=url, headers=headers)
    pprint(r.json())
    # cap_id = r.json()['data']['id']
    # cap_val = r.json()['data']['value']
    # return cap_id, cap_val


def login():
    base_url = config.adss.server_ip()
    url = base_url + 'new_login'
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    r = requests.post(url=url, json={
        "picture_id": "",
        "v_code": "",
        "phone": "18801053333",
        "password": "a753c776ff3ed4fefa2af948af87448910153281"
    }, headers=headers)
    ticket = r.json()["data"]["ticket"]
    return ticket


def get_token():
    ticket = login()
    base_url = config.adss.server_ip()
    url = base_url + 'passport'
    json = {
        "ticket": ticket
    }
    headers = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    r = requests.post(url=url, json=json, headers=headers)
    token = r.json()["data"]["token"]
    return token


if __name__ == '__main__':
    get_token()
