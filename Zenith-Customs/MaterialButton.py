from ZenithDecorator import *
@ZENITH.COMPONENT
class MATERIAL_SLIDER(ZENITH_COMPONENT_CONSTRUCTOR):
    def __init__(self) -> None:
        self.CALLABLE_NAME = "MATERIAL_BUTTON"
        self.ZENITH_COMPONENT_BASE = "Button"
        self.PROPERTIES = {"width": 200}