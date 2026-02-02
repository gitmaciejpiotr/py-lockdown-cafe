from app.errors import NotWearingMaskError, VaccineError
from app.cafe import Cafe


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str | None:
    masks_to_buy = 0
    not_vaccinated = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            not_vaccinated += 1
        except NotWearingMaskError:
            masks_to_buy += 1

    if not_vaccinated > 0:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
