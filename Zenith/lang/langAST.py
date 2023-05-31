class ASTNode:
    def __init__(self, tag_name):
        self.tag_name = tag_name
        self.attributes = {}
        self.content = ""
        self.children = []  # Add the 'children' attribute as an empty list

    def set_attribute(self, attr_name, attr_value):
        self.attributes[attr_name] = attr_value

    def set_content(self, content):
        self.content = content

    def add_child(self, child_node):
        self.children.append(child_node)



def build_ast(tokens):
    stack = []
    root = None

    for token in tokens:
        if token.startswith("<") and not token.startswith("</"):
            # Handle open tags
            tag_parts = token[1:-1].split()
            tag_name = tag_parts.pop(0)
            node = ASTNode(tag_name)

            # Handle attributes
            for part in tag_parts:
                if "=" in part:
                    attr_name, attr_value = part.split("=")
                    attr_value = attr_value.strip('"')
                    node.set_attribute(attr_name, attr_value)
                else:
                    attr_name = part
                    node.set_attribute(attr_name, "")

            if stack:
                parent_node = stack[-1]
                parent_node.add_child(node)
            else:
                root = node

            stack.append(node)
        elif token.startswith("</"):
            # Handle close tags
            stack.pop()
        else:
            # Handle text content
            node = stack[-1]
            node.set_content(token)

    return root


def print_ast(node, indent=""):
    print(f"{indent}<{node.tag_name}>")

    for attr_name, attr_value in node.attributes.items():
        print(f"{indent}  - {attr_name}: {attr_value}")

    if node.content:
        print(f"{indent}  - content: {node.content}")

    for child_node in node.children:
        print_ast(child_node, indent + "  ")

    print(f"{indent}</{node.tag_name}>")
