install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*whl

lint:
	poetry run flake8 lessons_codes

run-pytest:
	poetry run pytest
run-pytest-collect:
	poetry run pytest --collect-only
run-pytest-cov:
	poetry run pytest --cov

run_2_4:
	poetry run python -m lessons_codes.tests.test_ch2_4
