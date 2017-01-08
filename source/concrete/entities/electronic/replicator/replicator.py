from controller import controller
from model import model
from view import view

class Replicator(controller.Controller, model.Model, view.View):
    def __init__(self, parent = None, logistics = None):
        controller.Controller.__init__(self)
        model.Model.__init__(self, parent, logistics)
        view.View.__init__(self)
        pass
