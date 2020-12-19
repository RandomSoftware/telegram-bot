.PHONY: shell run

shell:
	pipenv install
	pipenv shell

run:
	pipenv run python src/server.py