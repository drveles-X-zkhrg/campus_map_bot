## SQL DB

Для удобочитаемого запроса
```
SELECT 
    s21_peers.s21_nickname AS "Peer Nickname",
    CASE 
        WHEN sessions.online THEN 'Online' 
        ELSE 'Offline' 
    END AS "Status",
    clusters.name AS "Cluster Name",
    sessions."row" AS "Row",
    sessions.place AS "Place",
    sessions.timestamp AS "Timestamp"
FROM 
    sessions
JOIN 
    s21_peers ON sessions.peer_id = s21_peers.id
JOIN 
    clusters ON sessions.cluster_id = clusters.id;
```

### DB structure
s21 peer - заполняется после парсинга 
- id: int
- s21_nickname: char[128]

friend (many_to_many) - заполняется API бота
- tg_id: int
- user: foreign_key(s21_peer)

cluster - заполняется при инициализации бд
- id: int
- name: char[128]

session - заполняется после парсинга 
- id: int 
- user: foreign_key(s21_peer)
- online: bool
- cluster: foreign_key(cluster)
- row: char
- place: int
- timestamp: timestamp

