#!/bin/sh
gunicorn -b 0.0.0.0:3000 manage:app
