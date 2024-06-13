# Parser service

In parser container

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