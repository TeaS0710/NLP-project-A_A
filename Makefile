PYTHON ?= python3

.PHONY: help extract prepare train evaluate pipeline asr audio text

help:
	@echo "Targets disponibles:"
	@echo "  make extract"
	@echo "  make prepare"
	@echo "  make train"
	@echo "  make evaluate"
	@echo "  make pipeline"
	@echo "  make asr"
	@echo "  make audio"
	@echo "  make text"

extract:
	$(PYTHON) -m src.script.extract

prepare:
	$(PYTHON) -m src.script.prepare

train:
	$(PYTHON) -m src.script.train

evaluate:
	$(PYTHON) -m src.script.evaluate

pipeline: extract prepare train evaluate

asr:
	$(PYTHON) -m src.script.asr

audio:
	$(PYTHON) -m src.script.audio_analyze

text:
	$(PYTHON) -m src.script.text_analyse
