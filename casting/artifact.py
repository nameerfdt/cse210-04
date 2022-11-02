from casting.actor import Actor

class Artifact(Actor):
    """An item of interest inheriting attributes and methods from parent.
    
    The responsibility of an Artifact is to provide a message about itself.
    
    Attributes:
        _message (string): A brief descriptoin
    """

    def __init__(self):
        """Constructs a new Artifact invoking the part constructor"""
        super().__init__()
        self._message = ""

    def get_message(self):
        """Gets the artifacts message
        
        Returns:
            string: the message
        """
        return self._message

    def set_message(self, message):
        """Updates the artifacts message.
        
        Args:
            message (str): the message
        """
        self._message = message