PYTHON ?= python3

.PHONY: help install prepare train evaluate pipeline

help:
	@echo "Pipeline NLP : HEALTHY vs SICK (spaCy textcat)"
	@echo ""
	@echo "  install   installe les dependances"
	@echo "  prepare   corpus JSON -> prepared.json (train/dev)"
	@echo "  train     entraine le classifieur spaCy textcat"
	@echo "  evaluate  evalue le modele sur le dev set"
	@echo "  pipeline  execute prepare + train + evaluate"

install:
	$(PYTHON) -m pip install -r requirements.txt

prepare:
	$(PYTHON) -m src.script.prepare

train:
	$(PYTHON) -m src.script.train

evaluate:
	$(PYTHON) -m src.script.evaluate

pipeline: prepare train evaluate
