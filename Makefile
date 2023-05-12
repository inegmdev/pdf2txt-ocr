init:
	@echo ""
	@echo "▶ Start initializing and installing prerequistes ..."
	@echo ""
	pip install virtualenv && virtualenv -p /usr/bin/python3 .venv
	sudo apt update && sudo apt install -y poppler-utils tesseract-ocr
	@echo ""
	@echo "✅ [SUCCESS] Start initializing and installing prerequistes."
	@echo ""
	@$(MAKE) help
.PHONY: init

clean:
	rm -rf .venv
.PHONY: clean

help:
	@echo ""
	@echo " 1) Activate/deactivate Virtualenv"
	@echo "$$ source ./activate"
	@echo "and"
	@echo "$$ source ./deactivate"
	@echo ""
	@echo ""
	@echo " 2) Install Python Modules"
	@echo "Prerequiste: virtualenv should be activated."
	@echo "(.venv) $$ ./install"
	@echo ""
	@echo ""
	@echo " 3) Freeze Python Modules (Development Only)"
	@echo "Prerequiste: virtualenv should be activated."
	@echo "(.venv) $$ ./freeze"
	@echo ""
.PHONY: help
