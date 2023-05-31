from ZenithDecorator import *
@ZENITH.COMPONENT
class MATERIAL_SLIDER(ZENITH_COMPONENT_CONSTRUCTOR):
    def __init__(self) -> None:
        self.CALLABLE_NAME = "MATERIAL_SLIDER"
        self.ZENITH_COMPONENT_BASE = "Input"
        self.ZENITH_COMPONENT_TYPE = "Slider"
        self.PROPERTIES = {"width": 200}