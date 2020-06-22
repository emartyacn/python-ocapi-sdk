# Python module for OCAPI (under development)

## How to use

### Prequisites

- [OCAPI settings](https://github.com/SalesforceCommerceCloud/ocapi-settings) must be added to the instance under test.
- pip install requirements.txt
- [docs](https://documentation.b2c.commercecloud.salesforce.com/DOC1/topic/com.demandware.dochelp/OCAPI/current/shop/Resources/index.htm)

### Authentication with OCAPI can happen one of two ways

1. You can create a file named `.pycapi` at the root of the repo using the following format (Not tested on Windows).

```shell
[default]
client_id = <CLIENT_ID>
client_secret = <CLIENT_SECRET>
hostname = <INSTANCE_URI>
api_version = v20_4
```

2. Manualy supply credenials through an API instance.

```python
from ocapi.client import ShopAPI

api = ShopAPI(hostname='dev-us.pandora.net', client_id='<CLIENT_ID>', client_secret='<CLIENT_SECRET>', api_version='
   ...: v20_4')

api.product_search(site_id='en-US', query='rings')
```

### **Note: The above uses a very limited portion of the search endpoint [docs](https://documentation.b2c.commercecloud.salesforce.com/DOC1/topic/com.demandware.dochelp/OCAPI/current/shop/Resources/ProductSearch.html). In order to fully utilize the search API, the product_search method will need to be improved.**


### Output should be:

```shell
[{'_type': 'product_search_hit',
  'hit_type': 'master',
  'link': 'https://dev-us.pandora.net/s/en-US/dw/shop/v20_4/products/188882C01?q=rings&client_id=cea04f38-4d79-4a1d-b3cb-171b771dccce',
  'product_id': '188882C01',
  'product_name': 'Wrapped Open Infinity Ring',
  'product_type': {'_type': 'product_type', 'master': True},
  'represented_product': {'_type': 'product_ref',
   'id': '188882C01-48',
   'link': 'https://dev-us.pandora.net/s/en-US/dw/shop/v20_4/products/188882C01-48?q=rings&client_id=cea04f38-4d79-4a1d-b3cb-171b771dccce'}},
...
```

### From here we can parse and compile a product URL...

---
All code authored by: Erik Marty