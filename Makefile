define HELP
make build: build the image
make test: test the image
endef

export HELP

help:
	@echo "$$HELP"

build:
	docker build --tag 0x4448/hello:dev .

rm:
	docker ps --filter name=hello -aq | xargs docker rm -f

run:
	docker run -d -p 8000:8000 --name hello 0x4448/hello:dev

test:
	@tests/run.sh
