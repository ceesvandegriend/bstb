.PHONY: install test lint format build publish all

all: install test lint format build

install:
	@echo "+++ Install +++"
	test -d __pypackages__ || mkdir __pypackages__
	pdm install -d

test:
	@echo "+++ Test +++"
	pdm test

lint:
	@echo "+++ Lint +++"
	pdm lint

format:
	@echo "+++ Format +++"
	pdm format

build:
	@echo "+++ Build +++"
	pdm build

publish:
	@echo "+++ Publish +++"
	pdm publish

clean:
	@echo "+++ Clean +++"
	@rm -rf __pypackages__/
	@rm -rf build/
	@rm -rf dist/
	@rm -rf .pytest_cache/ .coverage
	@find bstb/ tests/ -type d -name __pycache__ -exec rm -rf {} \;
