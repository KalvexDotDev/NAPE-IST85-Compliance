import json
import traceback

MIN_REQUIRED_EMPLOYEES = 25
def evaluate(evidence):
    try:
        if len(evidence['results'])>= MIN_REQUIRED_EMPLOYEES and type(evidence['results']) is list:
            return ('pass', "The minimum number of employees are present in the employee data")
        else:
            return ('fail',  "The minimum number of employees are NOT present in the employee data")
    except KeyError as ke:
        return ('inconclusive', f"The data supplied as not in a valid format {ke}")
    except Exception as e:
        return ('error', f"An unexpected error occured during evaluation of the minimum employee count: {traceback.format_exc()}")