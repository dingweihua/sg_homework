#! /bin/bash

uwsgi --http :9091 \
	-p 8 \
	-M \
	--buffer-size 65536 \
	--pythonpath . \
	-w run:app \
	--py-auto-reload 1 \
	--log-x-forwarded-for