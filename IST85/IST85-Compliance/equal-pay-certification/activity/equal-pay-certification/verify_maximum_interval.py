import re
from datetime import datetime
import traceback

YEARS_DESKTOP_COMPUTING_EXISTED = r'\b(197[5-9]|19[8-9]\d|20\d{2})\b'

def evaluate(evidence):
    try:
        years = re.findall(YEARS_DESKTOP_COMPUTING_EXISTED, evidence)
        if years is None or not years:
            return ('inconclusive', f"It is inconclusive if any years were found in the document")

        current_year = datetime.now().year
        is_less_than_three_years = [int(year) >= current_year - 3 for year in years]

        if all(is_less_than_three_years):
            return ('pass', "The Maximum interval check is approved because all years found in the document are within 3 years from this one")
        else:
            return ('fail', "Years beyond 3 years from now were found in the document.")
    except Exception as e:
        return ('error', f"An error occurred while evaluating whether the duration since last audit was less than required. The error is as follows: {traceback.format_exc()}")