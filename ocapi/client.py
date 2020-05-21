import json

import requests
from requests_oauthlib import OAuth2Session

from ocapi.lib.conf import Provider


class ShopAPI(Provider):

    """A module to wrap portions of the OCAPI API using Python

    Refrences:

        https://api-explorer.commercecloud.salesforce.com
        https://documentation.b2c.commercecloud.salesforce.com/DOC1/topic/com.demandware.dochelp/OCAPI/current/shop/Resources/index.html
    """

    AUTH_BASE = 'https://account.demandware.com'
    REDIRECT_URI = 'https://account.demandware.com'
    TOKEN_URL = 'https://account.demandware.com/dw/oauth2/access_token'
    AUTH_PATH = '/dwsso/oauth2/authorize?client_id=%s&redirect_uri=%s&response_type=%s'

    def __init__(self):
        self.SITE = 's/en-US'
        self.API_TYPE = 'dw/shop'
        self.VER = 'v20_4'

    @property
    def creds(self):
        return self.client_id, self.client_secret

    @property
    def client_id(self):
        return self.get_credential('client_id')

    @property
    def client_secret(self):
        return self.get_credential('client_secret')

    @property
    def hostname(self):
        return self.get_credential('hostname')

    @property
    def api_url(self):
        return 'https://{0}/{1}/{2}/{3}'.format(
            self.hostname,
            self.SITE,
            self.API_TYPE,
            self.VER
    )


    def obtain_token(self):
        provider = ShopAPI()
        auth = (self.client_id, self.client_secret)
        payload = {'grant_type': 'client_credentials'}
        resp = requests.post(
            provider.TOKEN_URL,
            auth=provider.creds,
            data=payload,
        )
        try:
            token = resp.json()['access_token']
            success_msg = """
            ************************
            Authorization Successful
            ************************
            """
            print(success_msg)
            return token
        except Exception as e:
            print(e)
            resp.raise_for_status()


    def product_search(self, query):
        """
        https://documentation.b2c.commercecloud.salesforce.com/DOC1/topic/com.demandware.dochelp/OCAPI/current/shop/Resources/ProductSearch.html

        """
        token = self.obtain_token()
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer {0}'.format(token)
        }
        endpoint = '/product_search?q={0}&client_id={1}'.format(query, self.client_id)
        request_url = '{0}{1}'.format(self.api_url, endpoint)
        req = requests.get(
            request_url,
            headers=headers,
            timeout=30,
        ).json()
        print('Response\n')
        print(json.dumps(req, indent=2))