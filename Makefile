.PHONY: dist check release

dist:
	python3 scripts/build_dist.py

check:
	python3 scripts/ci_validate.py
	python3 scripts/build_dist.py --check

release: dist
	chmod +x scripts/pack_release.sh
	./scripts/pack_release.sh
