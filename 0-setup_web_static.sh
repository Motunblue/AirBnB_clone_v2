#!/usr/bin/env bash
#Install nginx if not already installed

if ! command -v "nginx" &> /dev/null; then
    apt-get -y update
    apt-get -y install nginx
fi

if [ ! -d "/data/web_static/releases/test/" ]; then
    mkdir -p "/data/web_static/releases/test/"
fi
if [ ! -d "/data/web_static/shared/" ]; then
    mkdir -p "/data/web_static/shared/"
fi
if [ ! -d "/data/web_static/releases/" ]; then
    mkdir -p "/data/web_static/releases/"
fi
cat <<EOF > /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    This is a test page
  </body>
</html>
EOF

if ls "/data/web_static/current" &> /dev/null; then
    rm -f /data/web_static/current
fi
ln -sf "/data/web_static/releases/test/" "/data/web_static/current"

sudo chown -R "ubuntu:ubuntu" "/data/"

sed -i '/server_name _;/r /dev/stdin' /etc/nginx/sites-available/default <<EOF

    	location /hbnb_static {
		 alias /data/web_static/current/;
		 autoindex off;
	}
EOF

service nginx restart
