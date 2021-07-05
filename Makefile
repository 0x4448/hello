define HELP
make build: build the image
make pytest: run unit tests
make rm: delete container
make run: run container
endef

export HELP

help:
	@echo "$$HELP"

build:
	docker build --tag 0x4448/hello:dev .

functest:
	tests/functest.sh

pytest:
	coverage run -m pytest
	coverage report -m

rm:
	docker ps --filter name=hello -aq | xargs docker rm -f

run:
	docker run -d -p 8000:8000 --name hello 0x4448/hello:dev
