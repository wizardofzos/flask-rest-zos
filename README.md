# flask01 - A z/OS Python Flask REST API Example


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
       
    
## Adding endpoints to the REST-API

Every endpoint has it's own file in /endpoints. Make sure to add your new endpoints to /endpoints/__init__.py with a line like so:

    from .<name-of-your-resource-endpoint.py> import <ResourceName>

Then in test-app.py add these lines:

    from endpoints import <ResourceName>
    api.add_resource(<ResourceName>, '/<path-to-your-new-endpoint')
    docs.register(<ResourceName>)

And off you go :)

