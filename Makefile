PYTHON ?= python3

.PHONY: help install audio text prepare train evaluate pipeline

help:
	@echo "Pipeline NLP audio+texte (wav2vec2 + spaCy)"
	@echo ""
	@echo "  install  installe les dependances (requirements.txt)"
	@echo "  audio    analyse audio avec wav2vec2"
	@echo "  text     analyse texte avec spaCy"
	@echo "  prepare  fusion features + split train/dev"
	@echo "  train    entraine le classifieur spaCy textcat"
	@echo "  evaluate evalue le modele sur le jeu de dev"
	@echo "  pipeline execute tout le pipeline"

install:
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m spacy download fr_core_news_md

audio:
	$(PYTHON) -m src.script.audio_analyze

text:
	$(PYTHON) -m src.script.text_analyse

prepare:
	$(PYTHON) -m src.script.prepare

train:
	$(PYTHON) -m src.script.train

evaluate:
	$(PYTHON) -m src.script.evaluate

pipeline: audio text prepare train evaluate
