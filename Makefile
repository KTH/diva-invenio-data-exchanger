.DEFAULT_GOAL=ls

ls: # list available commands
	@grep '^[^#[:space:]].*:' Makefile
format: # format the code using black
	@black . && isort .
install: # Install py dependencies
	@pip install -r requirements.txt
run: # Install py dependencies
	@python main.py $(input) $(output)