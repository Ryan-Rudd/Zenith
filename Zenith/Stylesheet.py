from .Builder import Builder
class RecognizedStylesheetAttributes(object):
    def __init__(self) -> None:
        self.css_attributes = [
            'align-content',
            'align-items',
            'align-self',
            'all',
            'animation',
            'animation-delay',
            'animation-direction',
            'animation-duration',
            'animation-fill-mode',
            'animation-iteration-count',
            'animation-name',
            'animation-play-state',
            'animation-timing-function',
            'backface-visibility',
            'background',
            'background-attachment',
            'background-blur',
            'background-clip',
            'background-color',
            'background-image',
            'background-origin',
            'background-position',
            'background-repeat',
            'background-size',
            'block-size',
            'border',
            'border-block-end',
            'border-block-end-color',
            'border-block-end-style',
            'border-block-end-width',
            'border-block-start',
            'border-block-start-color',
            'border-block-start-style',
            'border-block-start-width',
            'border-bottom',
            'border-bottom-color',
            'border-bottom-left-radius',
            'border-bottom-right-radius',
            'border-bottom-style',
            'border-bottom-width',
            'border-collapse',
            'border-color',
            'border-image',
            'border-image-outset',
            'border-image-repeat',
            'border-image-slice',
            'border-image-source',
            'border-image-width',
            'border-inline-end',
            'border-inline-end-color',
            'border-inline-end-style',
            'border-inline-end-width',
            'border-inline-start',
            'border-inline-start-color',
            'border-inline-start-style',
            'border-inline-start-width',
            'border-left',
            'border-left-color',
            'border-left-style',
            'border-left-width',
            'border-radius',
            'border-right',
            'border-right-color',
            'border-right-style',
            'border-right-width',
            'border-spacing',
            'border-style',
            'border-top',
            'border-top-color',
            'border-top-left-radius',
            'border-top-right-radius',
            'border-top-style',
            'border-top-width',
            'border-width',
            'bottom',
            'box-decoration-break',
            'box-shadow',
            'box-sizing',
            'break-after',
            'break-before',
            'break-inside',
            'caption-side',
            'caret-color',
            'clear',
            'clip',
            'clip-path',
            'color',
            'column-count',
            'column-fill',
            'column-gap',
            'column-rule',
            'column-rule-color',
            'column-rule-style',
            'column-rule-width',
            'column-span',
            'column-width',
            'columns',
            'content',
            'counter-increment',
            'counter-reset',
            'cursor',
            'direction',
            'display',
            'empty-cells',
            'filter',
            'flex',
            'flex-basis',
            'flex-direction',
            'flex-flow',
            'flex-grow',
            'flex-shrink',
            'flex-wrap',
            'float',
            'font',
            'font-family',
            'font-feature-settings',
            'font-kerning',
            'font-language-override',
            'font-size',
            'font-size-adjust',
            'font-stretch',
            'font-style',
            'font-synthesis',
            'font-variant',
            'font-variant-alternates',
            'font-variant-caps',
            'font-variant-east-asian',
            'font-variant-ligatures',
            'font-variant-numeric',
            'font-variant-position',
            'font-weight',
            'gap',
            'grid',
            'grid-area',
            'grid-auto-columns',
            'grid-auto-flow',
            'grid-auto-rows',
            'grid-column',
            'grid-column-end',
            'grid-column-gap',
            'grid-column-start',
            'grid-gap',
            'grid-row',
            'grid-row-end',
            'grid-row-gap',
            'grid-row-start',
            'grid-template',
            'grid-template-areas',
            'grid-template-columns',
            'grid-template-rows',
            'hanging-punctuation',
            'height',
            'hyphens',
            'image-orientation',
            'image-rendering',
            'image-resolution',
            'ime-mode',
            'initial-letters',
            'inline-size',
            'inset',
            'inset-block',
            'inset-block-end',
            'inset-block-start',
            'inset-inline',
            'inset-inline-end',
            'inset-inline-start',
            'isolation',
            'justify-content',
            'justify-items',
            'justify-self',
            'left',
            'letter-spacing',
            'line-break',
            'line-height',
            'list-style',
            'list-style-image',
            'list-style-position',
            'list-style-type',
            'margin',
            'margin-block-end',
            'margin-block-start',
            'margin-bottom',
            'margin-inline-end',
            'margin-inline-start',
            'margin-left',
            'margin-right',
            'margin-top',
            'mask',
            'mask-border',
            'mask-border-mode',
            'mask-border-outset',
            'mask-border-repeat',
            'mask-border-slice',
            'mask-border-source',
            'mask-border-width',
            'mask-clip',
            'mask-composite',
            'mask-image',
            'mask-mode',
            'mask-origin',
            'mask-position',
            'mask-repeat',
            'mask-size',
            'mask-type',
            'max-block-size',
            'max-height',
            'max-inline-size',
            'max-width',
            'min-block-size',
            'min-height',
            'min-inline-size',
            'min-width',
            'mix-blend-mode',
            'object-fit',
            'object-position',
            'offset',
            'offset-anchor',
            'offset-block',
            'offset-block-end',
            'offset-block-start',
            'offset-distance',
            'offset-inline',
            'offset-inline-end',
            'offset-inline-start',
            'offset-path',
            'offset-position',
            'offset-rotate',
            'opacity',
            'order',
            'orphans',
            'outline',
            'outline-color',
            'outline-offset',
            'outline-style',
            'outline-width',
            'overflow',
            'overflow-anchor',
            'overflow-block',
            'overflow-inline',
            'overflow-wrap',
            'overflow-x',
            'overflow-y',
            'overscroll-behavior',
            'overscroll-behavior-block',
            'overscroll-behavior-inline',
            'overscroll-behavior-x',
            'overscroll-behavior-y',
            'padding',
            'padding-block-end',
            'padding-block-start',
            'padding-bottom',
            'padding-inline-end',
            'padding-inline-start',
            'padding-left',
            'padding-right',
            'padding-top',
            'page',
            'page-break-after',
            'page-break-before',
            'page-break-inside',
            'paint-order',
            'perspective',
            'perspective-origin',
            'place-content',
            'place-items',
            'place-self',
            'pointer-events',
            'position',
            'quotes',
            'resize',
            'right',
            'rotate',
            'row-gap',
            'ruby-align',
            'ruby-merge',
            'ruby-position',
            'scale',
            'scroll-behavior',
            'scroll-margin',
            'scroll-margin-block',
            'scroll-margin-block-end',
            'scroll-margin-block-start',
            'scroll-margin-bottom',
            'scroll-margin-inline',
            'scroll-margin-inline-end',
            'scroll-margin-inline-start',
            'scroll-margin-left',
            'scroll-margin-right',
            'scroll-margin-top',
            'scroll-padding',
            'scroll-padding-block',
            'scroll-padding-block-end',
            'scroll-padding-block-start',
            'scroll-padding-bottom',
            'scroll-padding-inline',
            'scroll-padding-inline-end',
            'scroll-padding-inline-start',
            'scroll-padding-left',
            'scroll-padding-right',
            'scroll-padding-top',
            'scroll-snap-align',
            'scroll-snap-stop',
            'scroll-snap-type',
            'scrollbar-color',
            'scrollbar-gutter',
            'scrollbar-width',
            'shape-image-threshold',
            'shape-margin',
            'shape-outside',
            'tab-size',
            'table-layout',
            'text-align',
            'text-align-all',
            'text-align-last',
            'text-combine-upright',
            'text-decoration',
            'text-decoration-color',
            'text-decoration-line',
            'text-decoration-skip',
            'text-decoration-style',
            'text-emphasis',
            'text-emphasis-color',
            'text-emphasis-position',
            'text-emphasis-style',
            'text-indent',
            'text-justify',
            'text-orientation',
            'text-overflow',
            'text-rendering',
            'text-shadow',
            'text-size-adjust',
            'text-transform',
            'text-underline-position',
            'top',
            'touch-action',
            'transform',
            'transform-box',
            'transform-origin',
            'transform-style',
            'transition',
            'transition-delay',
            'transition-duration',
            'transition-property',
            'transition-timing-function',
            'translate',
            'unicode-bidi',
            'user-select',
            'vertical-align',
            'visibility',
            'white-space',
            'widows',
            'width',
            'will-change',
            'word-break',
            'word-spacing',
            'writing-mode',
            'z-index'
        ]
            
class Style:
    def __init__(self):
        self.STYLE_DICTIONARY = dict()

    def formatSelector(self, selector):
        TYPE_OF_SELECTOR = ["class", "id"]
        formatted_selector = {}
        for selector_type in TYPE_OF_SELECTOR:
            if selector.startswith(selector_type + "."):
                formatted_selector['type'] = selector_type
                formatted_selector['name'] = selector[len(selector_type) + 1:]
                break
        return formatted_selector

    def apply(self, BUILDER: Builder, BUILDER_ROUTE: str):
        STYLE_TAG = "style"
        CSS_SELECTORS = []
        CSS_CONVERTED = ""

        for SELECTOR in self.STYLE_DICTIONARY:
            formatted_selector = self.formatSelector(SELECTOR)
            CSS_SELECTORS.append({"selector": formatted_selector, "attributes": self.STYLE_DICTIONARY[SELECTOR]})

        for selector_data in CSS_SELECTORS:
            selector = selector_data['selector']
            attributes = selector_data['attributes']
            SELECTOR_TYPE = selector['type']
            SELECTOR_NAME = selector['name']
            SELECTOR_TYPE_VAL_TRANS = ""
            if SELECTOR_TYPE == "class":
                SELECTOR_TYPE_VAL_TRANS = "."
            if SELECTOR_TYPE == "id":
                SELECTOR_TYPE_VAL_TRANS = "#"

            CSS_CONVERTED += f"{SELECTOR_TYPE_VAL_TRANS}{SELECTOR_NAME}" + "{"
            for attribute, value in attributes.items():
                CSS_CONVERTED += f"{attribute}: {value};"
            CSS_CONVERTED += "} "

        return CSS_CONVERTED


class Stylesheet:
    def new(style: dict, **kwargs) -> Style:
        styleAttributes = RecognizedStylesheetAttributes().css_attributes
        stylesheet = {}
        for selector, attributes in style.items():
            for attribute, value in attributes.items():
                if attribute not in styleAttributes:
                    print(f"Unrecognized Style Attribute \"{attribute}\" in @Stylesheet")
                    exit(1)
                else:
                    if selector not in stylesheet:
                        stylesheet[selector] = {}
                    stylesheet[selector][attribute] = value
        stylesheet_object = Style()
        stylesheet_object.STYLE_DICTIONARY = stylesheet
        return stylesheet_object