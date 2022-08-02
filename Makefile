clean:
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	find . -name __pycache__ -delete
	rm -f .coverage


test:
	pytest tests/


coverage: clean
	coverage run -m pytest tests/ && coverage report -m


mypy: clean
	mypy app/
