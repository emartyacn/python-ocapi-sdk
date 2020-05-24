import json

import requests
from requests_oauthlib import OAuth2Session

from ocapi.request_data import RequestData
from ocapi.lib.conf import Provider

import logging


class ShopAPI(Provider):

    """A module to wrap portions of the OCAPI API using Python

    References:

        https://github.com/ashishkumar-tudip/python-demandware-sdk
        https://api-explorer.commercecloud.salesforce.com
        https://documentation.b2c.commercecloud.salesforce.com/DOC1/topic/com.demandware.dochelp/OCAPI/current/shop/Resources/index.html
    """

    def __init__(self):
        self.data = RequestData()
        self.API_TYPE = 'dw/shop'
        self.headers = self.data.headers
        self.client_id = self.data.client_id
        self.VER = self.data.api_version


    def api_url(self, site_id='-'):
        return 'https://{0}/s/{1}/{2}/{3}'.format(
            self.data.hostname,
            site_id,
            self.API_TYPE,
            self.VER
    )


    def product_search(self, site_id, query):
        """
        https://documentation.b2c.commercecloud.salesforce.com/DOC1/topic/com.demandware.dochelp/OCAPI/current/shop/Resources/ProductSearch.html

        """
        api_url = self.api_url(site_id)
        endpoint = '/product_search?q={0}&client_id={1}'.format(query, self.client_id)
        request_url = '{0}{1}'.format(api_url, endpoint)
        res = requests.get(
            request_url,
            headers=self.headers,
            timeout=30,
        )
        logging.debug(json.dumps(res.json(), indent=2))
        try:
            hits = res.json()['hits']
            logging.info(json.dumps(hits, indent=2))
            return json.dumps(hits)
        except Exception as e:
            logging.exception('\n\n')


    def auth(self):
        # WIP
        endpoint = '/customers/auth?client_id={0}'.format(self.client_id)
        request_url = '{0}{1}'.format(self.api_url, endpoint)
        payload = {'type': 'credentials'}
        req = requests.post(
            request_url,
            headers=self.headers,
            auth=self.data.creds,
            json=payload,
        )


    def customer(self):
        # WIP
        endpoint = '/customers?client_id={0}'.format(self.client_id)
        request_url = '{0}{1}'.format(self.api_url, endpoint)
        payload = {
            "password":"abcd1234$$",
                "customer": {
                "login": "ocapi.qa",
                "email":"ocapiguya001@mailinator.com",
                "last_name":"Ocapi"
            }
        }
        req = requests.post(
            request_url,
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        logging.info(json.dumps(req.json(), indent=2))
        print(json.dumps(req.json(), indent=2))