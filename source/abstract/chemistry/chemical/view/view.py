class View:
    def __init__(self):
        pass

    def pretty_print(self, i=0):
        print(("\t"*i) + self.name)
        for element in self.elements:
            element.pretty_print(i+1)
