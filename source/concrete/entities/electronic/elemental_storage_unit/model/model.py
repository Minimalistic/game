from source.abstract.entities.inanimate.model import model
from source.concrete.entities.electronic.elemental_storage_tank.elemental_storage_tank import ElementalStorageTank
from source.library.science.chemistry.element import elements

class Model(model.Model):
    name  = "Elemental Storage Unit"
    tanks = dict()
    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.add_tank(elements.Aluminum)
        self.add_tank(elements.Carbon)
        self.add_tank(elements.Hydrogen)
        self.add_tank(elements.Iron)
        self.add_tank(elements.Oxygen)
        self.add_tank(elements.Silicon)
        self.add_tank(elements.Calcium)
        self.add_tank(elements.Titanium)
        pass

    def add_tank(self,element):
        self.tanks[element.name] = ElementalStorageTank(self, element, 100)

    def store_element(self, element_name, kg):
        self.tanks[element_name].add_element(kg)
        pass

    def check_storage(self, element_masses):
        have_enough = True
        print("\033[92m"+"Checking Storage To See If There Are Enough Elements To Build."+"\033[0m")

        for element_name in element_masses.keys():
            if self.tanks[element_name].stored < element_masses[element_name]:
                short_by = element_masses[element_name] - self.tanks[element_name].stored
                # You need 1.5 kg more Aluminum to build that.
                print("\033[91m"+"You need "+str(short_by)+" kg more "+element_name+" to build that."+"\033[0m")
                have_enough = False
        return have_enough

    def take_elements(self, element_masses):
        for element_name in element_masses:
            self.tanks[element_name].remove_kg(element_masses[element_name])
