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
	-  Take all clusters for all campuses ?
```
{
  "clusters": [
    {
      "id": 34734,
      "name": "Eternity",
      "capacity": 80,
      "availableCapacity": 80,
      "floor": 2
    },
    {
      "id": 34735,
      "name": "Evolution",
      "capacity": 99,
      "availableCapacity": 99,
      "floor": 2
    },
    {
      "id": 34736,
      "name": "Genom",
      "capacity": 80,
      "availableCapacity": 54,
      "floor": 3
    },
    {
      "id": 34737,
      "name": "Progress",
      "capacity": 81,
      "availableCapacity": 67,
      "floor": 3
    },
    {
      "id": 34738,
      "name": "Singularity",
      "capacity": 81,
      "availableCapacity": 81,
      "floor": 2
    },
    {
      "id": 34739,
      "name": "Universe",
      "capacity": 99,
      "availableCapacity": 74,
      "floor": 3
    },
    {
      "id": 34740,
      "name": "Vault",
      "capacity": 49,
      "availableCapacity": 38,
      "floor": 3
    }
  ]
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