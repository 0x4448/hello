define HELP
make build: build the image
make test: test the image
endef

export HELP

help:
	@echo "$$HELP"

build:
	docker build --tag 0x4448/hello:dev .

test:
	@tests/run.sh