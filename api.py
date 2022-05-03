import logging

import requests

logger = logging.getLogger("api")


class BaseAPI(object):

    def make_patch(self, url: str, data: dict = {}, headers: dict = {}) -> requests.Response:
        response = requests.patch(url, data, headers=headers)
        logger.info(f"request: {url}, data: {data}, headers: {headers}")
        return response

    def make_post(self, url: str, data: dict = {}, headers: dict = {}) -> requests.Response:
        response = requests.post(url, data, headers=headers)
        logger.info(f"request: {url}, data: {data}, headers: {headers}")
        return response

    def make_get(self, url: str, params: dict = {}, headers: dict = {}) -> requests.Response:
        response = requests.get(url, params=params, headers=headers)
        logger.info(f"request: {url}, params: {params}, headers: {headers}")
        return response
