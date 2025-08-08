hello:
	echo "Hello, world!"

up: down
	docker compose up --build -d 

down:
	docker compose down

scrape:
	python src/scrapper.py 