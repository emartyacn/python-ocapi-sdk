import json

import requests

from ocapi.lib.conf import Provider

import logging


class RequestData(Provider):

    """Creates and instance of the data we need to authorize our client
    and make requests to ocapi
    """

    AUTH_BASE = 'https://account.demandware.com'
    TOKEN_URL = 'https://account.demandware.com/dw/oauth2/access_token'

    @property
    def creds(self):
        return self.client_id, self.client_secret

    @property
    def client_id(self):
        return self.get_properties('client_id')

    @property
    def client_secret(self):
        return self.get_properties('client_secret')

    @property
    def hostname(self):
        return self.get_properties('hostname')

    @property
    def api_version(self):
        return self.get_properties('api_version')

    def obtain_token(self):
        # TODO: Obtain refresh token
        provider = RequestData()
        auth = (self.client_id, self.client_secret)
        payload = {'grant_type': 'client_credentials'}
        resp = requests.post(
            provider.TOKEN_URL,
            auth=provider.creds,
            data=payload,
        )
        try:
            token = resp.json()['access_token']
            logging.info('Authorization Sucessful')
            return token
        except Exception as e:
            logging.exception('\n\nCAN\'T REACH API!\n\n %s ' %  (json.dumps(resp.json(), indent=2) + '\n'))

    @property
    def headers(self):
        token = self.obtain_token()
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer {0}'.format(token),
            'x-dw-client-id': self.client_id,
        }
        return headers
