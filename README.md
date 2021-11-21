#  flask-rest-zos - A z/OS Python Flask REST API Example


Getting this up and runningon your z/OS is a breeze once you have conda installed :)

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

## Running it
    conda activate <env-that-has-python3-in-it>      
    cd ../../flask-rest-zos
    . bin/activate
    # Optional if you want another port than 12345
    export PORT=<port-you-want>
    python3 test-app.py

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

# TODO
Add gunicorn SSL example :)

# Feeling generous?
Send some ETH (or funkty tokens) to: 0x989787Df4b2c2eA8f8dEa6bFf7241916578E0862
