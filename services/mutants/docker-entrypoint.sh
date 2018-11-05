#!/bin/sh
gunicorn -b 0.0.0.0:3000 --reload --log-level debug manage:app
