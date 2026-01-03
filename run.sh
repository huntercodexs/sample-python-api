#!/bin/bash

echo "Application is starting"
uvicorn app.main:app --reload

