
class ZENITH_COMPONENT_CONSTRUCTOR:
    def __init__(self) -> None:
        self.CALLABLE_NAME = str
        self.ZENITH_COMPONENT_BASE = None
        self.ZENITH_COMPONENT_TYPE = None
        self.PROPERTIES = {
        }

class ZENITH:
    def COMPONENT(func, *args, **kwargs):
        print("Attempting to initalize component rules...")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Code to be executed after the original function
        print("Initalized component rules.")