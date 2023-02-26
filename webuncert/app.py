from flask import Flask, jsonify, request

from meter_proving.meter_proving import calculate_uncertanity

app = Flask(__name__)

@app.route("/")
def GetUncert():
    from_repetability = True
    #print(request.json)
    x = request.json['samples']
    if 'stdev' in request.json:
        from_repetability = not request.json['stdev']

    if 'confidence_interval' in request.json:
        confidence_interval = request.json['confidence_interval']
        if confidence_interval> 1.0: #guess the input is in prcent and not in a fraction
            confidence_interval = confidence_interval/100
    
    if 'coverage_factor' in request.json:
        coverage_factor = request.json['coverage_factor']
    
    
    if 'confidence_interval' in request.json and not 'coverage_factor' in request.json:
        uncert = calculate_uncertanity(x,repetability=from_repetability,confidence_intervall=confidence_interval)
    elif 'coverage_factor' in request.json:
        uncert = calculate_uncertanity(x,repetability=from_repetability,coverage_factor=coverage_factor)
    else: 
        uncert = calculate_uncertanity(x,repetability=from_repetability)
    
    uncert['samples'] = x #addint samples to the dict
    uncert['uncertanity_from_repetatbilty'] = from_repetability
    
    return jsonify(uncert)