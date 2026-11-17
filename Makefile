.PHONY: localbuild validate serve

PYTHON ?= python3

localbuild:
	zensical build --clean

validate:
	$(PYTHON) scripts/validate_zensical_nav.py

serve:
	zensical serve
