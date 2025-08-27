install:
	 pip install -r requirements.txt

test:
	 pytest -q

format:
	 python -m black .

lint:
	 python -m pylint --disable=R,C *.py

clean:
	 rm -rf __pycache__ .pytest_cache
