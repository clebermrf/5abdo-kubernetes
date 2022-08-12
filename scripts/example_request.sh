#!/bin/bash

curl -X POST \
    'localhost:8000/v1/predict' \
    -H 'Content-Type: application/json' \
    --data '{
        "model": "sentiments", 
        "version": 1.1,
        "message": "não confio nesse governo"
    }' 
