A web service that receives a JSON paylod of samples and returns a JSON payload the random uncertanity of the samples

# run locally:

make sure you have poetry installed if not
```Bash
pip install poetry
```
if you want the .venv file to be in the project directory:
```Bash
poetry config virtualenvs.in-project true
```

install the python modules, enter the .venv and run the application
```Bash
poetry install
poetry shell
flask --app webuncert/app run
```
# Build and run it as a docker container

create a docker container and run it, and mapping it to port 1000 on the dockerhost machine.
```bash
docker build -t docker_user/conatinername:0.0.1.RELEACE .
docker container run -d -p 1000:5000 docker_user/conatinername:0.0.1.RELEACE
```

# how to use the webservice

input HTTP body:
```JSON
{"samples": [1000.1, 999.9, 1000.0, 998.9, 1000.0, 1000.8, 1002.7]}
```
returns:
```JSON
{
    "confidence_intervall": 0.95,
    "dof": 6,
    "mean": 1000.342857142857,
    "n": 7,
    "repetability": 0.0037986975893979894,
    "samples": [
        1000.1,
        999.9,
        1000.0,
        998.9,
        1000.0,
        1000.8,
        1002.7
    ],
    "standard_deviaton": 0.0014048437830613866,
    "uncertanity_fraction": 0.0012999715833845495,
    "uncertanity_in_unit": 1.300417287927424,
    "uncertanity_prcent": 0.12999715833845493,
    "uncertanity_from_repetatbilty": true,
}
```


valid JSON raw input:
```JSON
 {
    "samples": [1000.1, 999.9, 1000.0, 998.9, 1000.0, 1000.8, 1002.7],
    "stdev": "bool",
    "confidence_interval": "0.0-1.0 or 1-100%",
    "coverage_factor": "float", 
 }
```
Note:
if both confidence_interval and coverage factor is sent in the body, then coverage factor base uncert will be returned.


