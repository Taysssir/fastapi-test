#!/bin/sh
SLEEP_TIME="1"
echo "Hi, I'm sleeping for ${SLEEP_TIME} seconds Waiting for postgress database end starting process"
sleep ${SLEEP_TIME}

uvicorn api.main:app --reload --host 0.0.0.0 --port 5000