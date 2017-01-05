import uuid
from datetime import datetime, timedelta

class Model:
    uuid    = None
    created = None
    parent  = None

    def __init__(self, parent = None):
        self.parent = parent
        self.uuid = uuid.uuid4()
        self.created = datetime.now()
        pass

    def created_delta(self):
        return (datetime.now() - self.created).total_seconds()
