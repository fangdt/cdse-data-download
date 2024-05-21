# -*- coding: utf-8 -*-

import requests


# 获取CDSE的Access token
def get_access_token(username: str, password: str) -> str:
    data = {
        "client_id": "cdse-public",
        "username": username,
        "password": password,
        "grant_type": "password",
    }
    req = requests.post(
        "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token",
        data=data,
    )
    req.raise_for_status()
    return req.json()["access_token"]


# 获取产品响应
def download_response(data_id, token):
    url = f"https://download.dataspace.copernicus.eu/odata/v1/Products({data_id})/$value"
    headers = {"Authorization": f"Bearer {token}"}
    session = requests.Session()
    session.headers.update(headers)
    response = session.get(url, headers=headers, stream=True)
    return response
