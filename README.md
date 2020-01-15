# WorkersKV

A Cloudflare Workers KV API Wrapper made with Python.

## Cloudflare Authentification
This library only supports API token authentification.
Create a file "~/.cloudflare/cloudflare.cfg" with the API token

```shell
cat ~/.cloudflare/cloudflare.cfg
[CloudFlare]
token = 00000000000000000000000000000000
```

## Example
````python
from WorkersKV import WorkersKV

workers = WorkersKV(
    account="XXXX",
    namespace="XXXXX"
)

keys = workers.list_keys()
print(keys.json())

>{
    'messages': [],
    'errors': [],
    'success': True,
    'result_info': {'cursor': '', 'count': 3},
    'result': [
        {'name': 'Adam'},
        {'name': 'John'},
    ]}
}


value = workers.get("Adam")
print(value.content)

> b'18'

value = workers.put("David", "24")
value = workers.get("David")
print(value.content)

> b'24'
```