import json
import random

import requests

from ocapi.client import ShopAPI


class Helpers(ShopAPI):


    def get_product(site_id='-', query=None):
        shop = ShopAPI()
        links = [link['link'] for link in shop.product_search(site_id, query)]
        resp = requests.get(random.choice(links)).json()
        product_link = 'https://{0}/{1}/{2}/{3}/{4}.html'.format(
            shop.hostname,
            resp['c_primaryCategory'],
            resp['primary_category_id'],
            resp['name'].replace(' ', '-').lower(),
            resp['id'])
        return product_link