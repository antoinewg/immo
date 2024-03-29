import enum


def choices(enumeration):
    """
    Convert an Enum to a Django-style "choices" iterator.
    """
    return [(member.name, member.value) for member in enumeration]


class ESTATE_TYPE(enum.Enum):
    appartment = "Appartement"
    appartment_viager = "Appartement en viager"
    maison_villa = "Maison/Villa"
    maison_villa_viager = "Maison/Villa en viager"
    projet_construction = "Projet de construction"
