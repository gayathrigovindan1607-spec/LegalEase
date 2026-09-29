from fastapi import APIRouter

router = APIRouter()

@router.post("/generate")
def generate(data: dict):
    details = data.get("details", "")
    doc_type = data.get("doc_type", "Freelance Work Contract")

    document = f"""
    LegalEase
    Freelance Work Contract

    ## Freelance Work Contract

    {details}

    Agreement made this 15th day of April, 2025

    Between:

    Jane Doe (hereinafter referred to as the "Service Provider"), residing at [Jane Doe's Address], [Jane Doe's City, State, Zip Code]

    And:

    TechNova Inc. (hereinafter referred to as the "Client"), a corporation organized and existing under the laws of [State of Incorporation], with its principal place of business at [TechNova Inc.'s Address], [TechNova Inc.'s City, State, Zip Code]

    1. Scope of Work: {details}

    2. Payment Terms: Client agrees to pay Service Provider as per milestones.

    3. Confidentiality: Both parties agree to maintain confidentiality.

    4. Term: This agreement is valid for 1 year.

    5. Termination: Either party can terminate with 30 days notice.

    9. Severability:
    If any provision of this Agreement is held to be invalid or unenforceable, the remaining provisions shall remain in full force and effect.

    IN WITNESS WHEREOF, the parties have executed this Agreement as of the Effective Date.

    Jane Doe (Service Provider)

    _________
    [Signature]

    TechNova Inc. (Client)

    _________
    [Authorized Representative Signature]
    [Authorized Representative Title]

    Draft by LegalEase AI
    """
    return {"document": document}
    