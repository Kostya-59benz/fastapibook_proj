from model.explorer import Explorer

# fiction data
_explorers = [
    Explorer(name="Claude Hande", country="FR", description="Scarce during full moons"),
    Explorer(name="Noah Weiser", country="DE", description="Myopic machete man"),
]


def get_all() -> list[Explorer]:

    return _explorers


def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None


# Приведенные ниже варианты пока не функциональны,
# поэтому они просто делают вид, что работают,
# не изменяя реальный фиктивный список
def create(explorer: Explorer) -> Explorer:
    """Create explorer"""
    return explorer


def modify(explorer: Explorer) -> Explorer:
    """Partial change entry of explorer"""
    return explorer



def replace(explorer: Explorer) -> Explorer:
    """Complete change entry of explorer"""
    return explorer


def delete(name: str) -> bool:
    """Delete an entry of creature; return None if it exist"""
    return None
