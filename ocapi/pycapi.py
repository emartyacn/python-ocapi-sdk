import json

import requests

from ocapi.lib.conf import Provider

import logging


class PyCAPI(Provider):

    """Creates and instance of the data we need to authorize our client
    and make requests to ocapi
    """

    AUTH_BASE = 'https://account.demandware.com'
    TOKEN_URL = 'https://account.demandware.com/dw/oauth2/access_token'

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.host = kwargs['hostname']
            self.client = kwargs['client']
            self.secret = kwargs['secret']
            self.version = kwargs['api_version']

    @property
    def creds(self):
        return self.client_id, self.client_secret

    @creds.setter
    def creds(self, val):
        if val == None:
            return self.client, self.secret

    @property
    def client_id(self):
        return self.get_properties('client_id')

    @client_id.setter
    def client_id(self, val):
        if val == None:
            return self.client

    @property
    def client_secret(self):
        return self.get_properties('client_secret')

    @client_secret.setter
    def client_secret(self, val):
        if val == None:
            return self.secret

    @property
    def hostname(self):
        return self.get_properties('hostname')

    @hostname.setter
    def hostname(self, val):
        if val == None:
            return self.host

    @property
    def api_version(self):
        return self.get_properties('api_version')

    @api_version.setter
    def api_version(self, val):
        if val == None:
            return self.version

    def obtain_token(self):
        # TODO: Obtain refresh token
        provider = PyCAPI()
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
