# Parser service

In parser container

## TO DO


- AUTH 2.0
How to authenticate your application

1. To get an access token (JWT) you need to make a POST request to the Access Token URL (https://auth.sberclass.ru/auth/realms/EduPowerKeycloak/protocol/openid-connect/token). In the request body parameters you need to specify the values for parameters - "username" (=$login), "password" (=$password), "grant_type" (="password") and "client_id" (="s21-open-api")
2. In case of successful authentication, the response will include an access token and a refresh token
3. Use the access token to send requests to the API. Place it in the Authorization header (Bearer $token) to authenticate your application
- Take all campuses `/v1/campuses`
- Take all clusters of KZN `7c293c9c-f28c-4b10-be29-560e4b000a34` 
	-  Take all clusters for all MSK timezon campuses, MSK, KZN, Белгород, Великий Новгород, Ярославль
``` 
clusters = {
    "Kazan": {
        "34734": "et",
        "34735": "ev",
        "34736": "ge",
        "34737": "pr",
          "34738": "si",
          "34739": "un",
          "34740": "va",
    },
    "Moscow": {
        "34715": "at",
        "36799": "du",
        "34717": "ga", 
        "34718": "il",
        "34719": "mi",
        "34720": "oa",
        "34721": "ox",
        "34723": "su",
        "34724": "vo",
    },
}
```

- Take all peers online 
```
curl -X 'GET' \
  'https://edu-api.21-school.ru/services/21-school/api/v1/clusters/34734/map?limit=101&offset=0' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer token...'
  ```
## Endpoints

`update_peers()` sends to api data:

```
data_to_send =
{
	"peers": { 
		"s21_peer_nick": {
			"status": "val"
			"cluster": "val",
			"row": "val",
			"col": "val",
			"time": "MSK timestamp",
		},
		"s21_peer_nick1": {
			"status": "val"
			"cluster": "val",
			"row": "val",
			"col": "val",
			"time": "MSK timestamp",
		},
		.
		.	
		.
	}
}
```