init:
	pip install virtualenv && virtualenv -p /usr/bin/python3 .venv
	sudo apt install poppler-utils tesseract-ocr
.PHONY: init

activate:
	@echo ""
	@echo "To activate the virtual environment, source the following file using the command:"
	@echo "$$ . .venv/bin/activate"
	@echo ""
.PHONY: activate

deactivate:
	@echo ""
	@echo "To deactivate the virtual environment, write the following command:"
	@echo "(.venv) $$ deactivate"
	@echo ""
.PHONY: deactivate

install:
	@echo ""
	@echo "Prerequiste: virtualenv should be activated. See 'make activate' fore more info."
	@echo "to install the required python modules, write the following command:"
	@echo "(.venv) $$ pip install -r requirements.txt"
	@echo ""
.PHONY: install

freeze:
	@echo ""
	@echo "Prerequiste: virtualenv should be activated. See 'make activate' fore more info."
	@echo "To freeze the current installed python modules, write the following command:"
	@echo "(.venv) $$ pip freeze > requirements.txt"
	@echo ""
.PHONY: freeze

clean:
	rm -rf .venv
.PHONY: clean
