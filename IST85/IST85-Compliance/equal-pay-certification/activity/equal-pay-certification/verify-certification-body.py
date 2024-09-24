APPROVED_AUDITORS = [
    "BST",
    "Super Standards",
    "Deloitte",
    "KPMG",
    "PWC",
    "CROWE"
]

def evaluate(evidence):
    try:
        for line in evidence:
            for auditor in APPROVED_AUDITORS:
                if auditor in line:
                    return ('pass', f"The certification body check is approved because references to {auditor} were found in the body")
        else:
            return ('inconclusive', f"It is inconclusive if the certification check is approved because no references to {" ".join(APPROVED_AUDITORS)} was found.")
    except Exception as e:
        return ('error', f"An error occurred while evaluating whether the 'mgt_approved' field is true or false. The error is as follows: {str(e)}")
