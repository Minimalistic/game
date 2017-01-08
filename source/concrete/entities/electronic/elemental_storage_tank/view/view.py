from source.abstract.entities.inanimate.view import view
from source.library.action import action

from animation_config import percent_000, percent_020, percent_040, percent_060, percent_080, percent_100

from ..model import model

class View(view.View):
    height  = 64
    width   = 32

    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(percent_000.data)
        pass

    def on_render(self):
        p = self.get_stored_percent()
        if p < .19:
            if self.capacity_state != model.CapacityState.PERCENT_000:
                self.capacity_state = model.CapacityState.PERCENT_000
                self.animation = action.Action(percent_000.data)
        if p >= .20 and p <= .39:
            if self.capacity_state != model.CapacityState.PERCENT_020:
                self.capacity_state = model.CapacityState.PERCENT_020
                self.animation = action.Action(percent_020.data)
        if p >= .40 and p <= .59:
            if self.capacity_state != model.CapacityState.PERCENT_040:
                self.capacity_state = model.CapacityState.PERCENT_040
                self.animation = action.Action(percent_040.data)
        if p >= .60 and p <= .79:
            if self.capacity_state != model.CapacityState.PERCENT_060:
                self.capacity_state = model.CapacityState.PERCENT_060
                self.animation = action.Action(percent_060.data)
        if p >= .80 and p <= .99:
            if self.capacity_state != model.CapacityState.PERCENT_080:
                self.capacity_state = model.CapacityState.PERCENT_080
                self.animation = action.Action(percent_080.data)
        if p >= 1.0:
            if self.capacity_state != model.CapacityState.PERCENT_100:
                self.capacity_state = model.CapacityState.PERCENT_100
                self.animation = action.Action(percent_100.data)
        self.animation.on_render(self)
        pass

    def pretty_print(self, i=0):
        print(("\t"*i)+self.element.name+" "+str(self.stored)+"/"+str(self.capacity))
