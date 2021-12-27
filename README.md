#  flask-rest-zos - A z/OS Python Flask REST API Example


Getting this up and runningon your z/OS is a breeze once you have conda installed :)
You can also just clone this to your x86 Linux environment and it will run there just the same. Make sure if you're adding files that don't match the mapping in '.gitattributes' you add this mapping. That way, you can work/dev on your x86 environment and just pull it on the z/OS side....

Then again, why would you run it outside of z/OS anyway? It's soo easy getting that Learner Edition via IBM no?

## Requirements

- Conda installed
- Python available
- Network connectivity to the outside world    

## Preparing for first run

    conda activate <env-that-has-python3-in-it>
    git clone git@github.com:wizardofzos/flask-rest-zos.git
    cd flask-rest-zos
    python -m venv .
    . bin/activate  
    python3 -m pip install -r requirements.txt

## Running it in devmode
    conda activate <env-that-has-python3-in-it>      
    cd ../../flask-rest-zos
    . bin/activate
    # Optional if you want another port than 12345
    export PORT=<port-you-want>
    python3 testapp.py

Then point your browser to http://<ip_or_dns_of_your_mainframe>:12345/swagger-ui and...

![inaction](https://github.com/wizardofzos/flask-rest-zos/blob/main/inaction.png?raw=true)
       
    
## Adding endpoints to the REST-API

Every endpoint has it's own file in /endpoints. Make sure to add your new endpoints to /endpoints/__init__.py with a line like so:

    from .<name-of-your-resource-endpoint.py> import <ResourceName>

Then in test-app.py add these lines:

    from endpoints import <ResourceName>
    api.add_resource(<ResourceName>, '/<path-to-your-new-endpoint')
    docs.register(<ResourceName>)

And off you go :)

# Running with gunicorn

Running with gunicorn is easy:

    gunicorn --bind 0.0.0.0:5000 wsgi:app

But we'd also like to have it with some SSL-certs...
For this, we just need to create our server cert and key (instructions below, using certbot is highly recommended)

    gunicorn --certfile=/path/to/cert.pem \ 
             --keyfile=key.pem            \
             --bind 0.0.0.0:443           \
             wsgi:app


# Creating your (self-signed) cert

Just execute these commands :)

    openssl req -new > cert.csr
    openssl rsa -in privkey.pem -out key.pem
    openssl x509 -in cert.csr -out cert.pem -req -signkey key.pem -days 3270
    cat key.pem>>cert.pem

 
# Feeling generous?
Send some ETH (or funky tokens) to: 0x989787Df4b2c2eA8f8dEa6bFf7241916578E0862
