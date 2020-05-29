import random

import requests


def get_product(links):
    resp = requests.get(random.choice(links)).json()
    product_link = '{0}/{1}/{2}/{3}.html'.format(
        resp['c_primaryCategory'],
        resp['primary_category_id'],
        resp['name'].replace(' ', '-').lower(),
        resp['id'])
    return product_link