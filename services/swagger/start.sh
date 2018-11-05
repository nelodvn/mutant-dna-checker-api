#!/bin/bash

sed -i -e 's@http://petstore.swagger.io/v2/swagger.json@'"$URL"'@g' /usr/share/nginx/html/index.html

exec nginx -g 'daemon off;'
