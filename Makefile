init:
	pip install virtualenv && virtualenv -p /usr/bin/python3 .venv
.PHONY: init

start:
	@echo ""
	@echo "To start the virtual environment, source the following file using the command:"
	@echo "$$ . .venv/bin/activate"
	@echo ""
.PHONY: start

stop:
	@echo ""
	@echo "To stop the virtual environment, write the following command:"
	@echo "(.venv) $$ deactivate"
	@echo ""
.PHONY: stop

clean:
	rm -rf .venv
.PHONY: clean
