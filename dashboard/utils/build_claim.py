# ==========================================================
# Build Complete Claim Dictionary
# ==========================================================

def build_claim(

    vehicle_data,
    policy_data,
    driver_data,
    claim_data

):

    complete_claim = {}

    complete_claim.update(

        vehicle_data

    )

    complete_claim.update(

        policy_data

    )

    complete_claim.update(

        driver_data

    )

    complete_claim.update(

        claim_data

    )

    return complete_claim