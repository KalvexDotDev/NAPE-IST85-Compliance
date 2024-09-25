import traceback

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
        # put evidence back into a string
        evidence = "".join(evidence)

        # We expect a reference to the standards org within the first 10 lines of a document
        for line in evidence.splitlines()[:20]:
            for auditor in APPROVED_AUDITORS:
                if auditor.lower() in line.lower():
                    return ('pass', f"The certification body check is approved because references to {auditor} were found in the body")
        else:
            return ('fail', f"It is inconclusive if the certification check is approved because no references to {' or '.join(APPROVED_AUDITORS)} were found")
    except Exception as e:
        return ('error', f"An error occurred while evaluating whether the certification body is approved or not. The error is as follows: {traceback.format_exc()}")
