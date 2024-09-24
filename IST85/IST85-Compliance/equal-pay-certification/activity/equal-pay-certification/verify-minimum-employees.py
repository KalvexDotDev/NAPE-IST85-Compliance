import json

MIN_REQUIRED_EMPLOYEES = 25
def evaluate(evidence):
    try:
        j = json.loads(evidence)
        if len(j['results'])>= MIN_REQUIRED_EMPLOYEES:
            return ('pass', "The minimum number of employees are present in the employee data")
        else:
            return ('fail',  "The minimum number of employees are NOT present in the employee data")
    except json.decoder.JSONDecodeError as jde:
        return ('inconclusive', f"The data supplied as not in a valid format {jde}")
    except KeyError as ke:
        return ('inconclusive', f"The data supplied as not in a valid format {ke}")
    except Exception as e:
        return ('error', "An unexpected error occured during evaluation of the minimum employee count: {e}")
        
