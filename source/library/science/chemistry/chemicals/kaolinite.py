from source.library.science.chemistry.element import elements
from source.abstract.chemistry.chemical import chemical


# Al2Si2O5(OH)4 in mineralogy or Al2O3-2SiO2-2H2O in ceramics
class Kaolinite(chemical.Chemical):
    name = "Kaolinite"
    molar_mass = 258.18
    density = 2.68  # 2.16 - 2.68
    formula = "Al2Si2O5(OH)4"

    def __init__(self):
        chemical.Chemical.__init__(self)
        self.elements = [
            elements.Aluminum(),
            elements.Aluminum(),
            elements.Silicon(),
            elements.Silicon(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Oxygen(),
            elements.Hydrogen(),
            elements.Hydrogen(),
            elements.Hydrogen(),
            elements.Hydrogen(),
        ]
        pass

