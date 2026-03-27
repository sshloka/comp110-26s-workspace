rsvp_list: list[str] = ["Enrico", "Yun"]


def add_rsvp(rsvped: list[str], friend: str) -> None:
    rsvped.append(friend)


def has_rsvped(rsvped: list[str], friend: str) -> bool:
    i: int = 0
    while i < len(rsvped):
        if rsvped[i] == friend:
            return True
        i = i + 1
    return False


def not_yet_rsvped(rsvped: list[str], invited: list[str]) -> list[str]:
    yet_to_rsvp: list[str] = []
    i: int = 0
    while i < len(invited):
        guest: str = invited[i]
        if not has_rsvped(rsvped, guest):
            yet_to_rsvp.append(guest)
        i = i + 1
    return yet_to_rsvp
