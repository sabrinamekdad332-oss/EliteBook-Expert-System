from experta import Fact

class Issue(Fact):
    """The core problem reported by the user."""
    pass

class Symptom(Fact):
    """Specific behavior observed on the HP EliteBook."""
    pass

class HardwareStatus(Fact):
    """State of specific components like Battery, Screen, or Keyboard."""
    pass