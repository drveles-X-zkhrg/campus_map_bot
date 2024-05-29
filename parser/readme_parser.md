# Parser

Это отдельный микросервис, поднимается в своем контейнере.

## Отправляемые данные
```
data_to_return =
{
	"peers": { 
		"s21_peer_nick": {
			"status": "val"
			"cluster": "val",
			"row": "val",
			"col": "val",
			"time": "val",
		},
		"s21_peer_nick1": {
			"status": "val"
			"cluster": "val",
			"row": "val",
			"col": "val",
			"time": "val",
		},
		.
		.	
		.
	}
}
```
## DOCs

Вебдрайвер должен лежать в `.venv/`

вебдрайвер для линукс 
https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/linux64/chrome-linux64.zip

<!-- - Крона или системцтл для автозапуска парсера. -->
crontab 
*/1 * * * * cd /home/jenniffr/friends_bot/ && . /home/jenniffr/friends_bot/venv/bin/activate && /home/jenniffr/friends_bot/venv/bin/python3 /home/jenniffr/friends_bot/main.py >> /home/jenniffr/friends_bot/cron.log

scp jenniffr@87.242.85.185:/home/jenniffr/friends_bot/cron.log ./

## Parser ожидаемые проблемы.

1. Не хватило ресурсов и программа не выполнилась за минуту.
2. Не ответил сайт
3. Не удалось залогиниться
4. Не удалось загрузить карту кампуса
5. Не удалось развернуть этажи
6. Не удалось загрузить класстер 
7. Не удалось распрасить данные класстера.
8. Все класстеры пусты.




на псевдокоде нужно чтобы создаешь поток
создаешь лок для потока
в потоке пушишь на ручку
снимаешь лок
