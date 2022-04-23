from ..a_pack.change_a import change_a
from ..b_pack.change_b import change_b

def change_a_and_b(sa: str, sb: str) -> None:
    change_a(sa)
    change_b(sb)
    return