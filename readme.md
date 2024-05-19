# Friends Bot

## TO DO

## DOCs

### DB structure
s21 peer 
- id: int
- s21_nickname: char[128]

friend (many_to_many) 
- tg_id: int
- user: foreign_key(s21_peer)

cluster
- id: int
- name: char[128]

session
- id: int 
- user: foreign_key(s21_peer)
- online: bool
- cluster: foreign_key(cluster)
- row: char
- place: int
- timestamp: timestamp


## Idea

- Мне кажется проще всего в качестве доп функционала можно прикрутить уведомления - когда кто-то появился в кампусе, но это уже реально сталкеринг. Ну или платно.