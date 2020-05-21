import requests

from ocapi.lib.conf import Provider


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
        return self.get_credential('client_id')

    @property
    def client_secret(self):
        return self.get_credential('client_secret')

    @property
    def hostname(self):
        return self.get_credential('hostname')

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
            success_msg = """
            ************************
            Authorization Successful
            ************************
            """
            print(success_msg)
            return token
        except Exception as e:
            # TODO: Use logging
            print(e)
            resp.raise_for_status()

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