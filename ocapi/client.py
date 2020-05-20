import json

import requests
from requests_oauthlib import OAuth2Session

from ocapi.lib.conf import Provider


class Auth(Provider):

    AUTH_BASE = 'https://account.demandware.com'
    REDIRECT_URI = 'https://account.demandware.com'
    TOKEN_URL = 'https://account.demandware.com/dw/oauth2/access_token'
    AUTH_PATH = '/dwsso/oauth2/authorize?client_id=%s&redirect_uri=%s&response_type=%s'

    @property
    def creds(self):
        return self.client_id, self.client_secret

    @property
    def client_id(self):
        return self.get_credential('client_id')

    @property
    def client_secret(self):
        return self.get_credential('client_secret')

    def auth():
        oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
        auth_url, state = oauth.authorization_url(auth_base)
        #token = oauth.fetch_token(
        #    token_url,
        #    client_secret=client_secret,
        #    include_client_id=True,
        #    authorization_response=resp,
        #)

    def obtain_token(self):
        provider = Auth()
        auth = (self.client_id, self.client_secret)
        payload = {'grant_type': 'client_credentials'}
        resp = requests.post(
            provider.TOKEN_URL,
            auth=provider.creds,
            data=payload,
        ).json()
        token = resp['access_token']
        print('Authorization Successful')
        return token