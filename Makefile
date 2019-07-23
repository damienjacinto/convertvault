SHELL:=/bin/bash
APP?=convertvault
CONTAINER_IMAGE?=jacintod/convertvault
RELEASE?=1.0.0
PORT?=8080

.PHONY: help run container test

help:
	@ echo
	@ echo '  Usage:'
	@ echo ''
	@ echo '    make <target>'
	@ echo ''
	@ echo '  Targets:'
	@ echo ''
	@ echo '    env         Bascule virtualenv env'
	@ echo '    run         Run app on port: $(PORT) - check $$(PORT)'
	@ echo '    container   Build the docker image'
	@ echo '    drun        Run docker image on binded port: $(PORT) - check $$(PORT)'
	@ echo '    test        lancement des tests'
	@ echo ''
	
venv: venv/bin/active

venv/bin/active: requirements.txt
	test -d venv || virtualenv venv && \
    pip3 install -r requirements.txt && \
	. venv/bin/activate
	
run: 
	PORT=$(PORT) DEBUG=0 python3 convertvault.py

container:
	docker stop $(CONTAINER_IMAGE):$(RELEASE) || true && \
	docker build -t $(CONTAINER_IMAGE):$(RELEASE) .

drun: container
	docker run --name ${APP} -p ${PORT}:8080 --rm \
		$(CONTAINER_IMAGE):$(RELEASE)

test:
	python3 test.py -v