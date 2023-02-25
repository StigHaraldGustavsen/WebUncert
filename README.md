A web service that receives a JSON paylod of samples and returns a JSON payload the random uncertanity of the samples

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

run locally:
```Bash
poetry install
poetry shell
flask --app webuncert/app run
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