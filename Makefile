.DEFAULT_GOAL=ls

ls: ## list available commands
	@grep '^[^#[:space:]].*:' Makefile

format: ## format the code using black
	@black .
	@isort .

install: ## Install Python dependencies
	@pip install -r requirements.txt

run: ## Run the main.py script with input and output parameters
	@python main.py $(path_in) $(path_out)

test: ## Run tests using pytest
	@pytest
