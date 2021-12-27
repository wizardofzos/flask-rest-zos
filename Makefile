d:
	python testapp.py

s:
	gunicorn --certfile=cert.pem --keyfile=key.pem --bind 0.0.0.0:5443 wsgi:app
