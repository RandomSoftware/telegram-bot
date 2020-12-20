.PHONY: shell run test

shell:
	pipenv install
	pipenv shell

run:
	pipenv run python src/server.py

test:
	pipenv run python -m unittest discover -s tests