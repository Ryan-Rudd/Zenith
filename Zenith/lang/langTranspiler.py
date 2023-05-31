def transpile_to_html(node):
    result = ""

    if node.tag_name == "Container":
        result += "<div"

        for attr_name, attr_value in node.attributes.items():
            attr_name = transpile_attribute_name(attr_name)
            result += f' {attr_name}="{attr_value}"'

        result += ">"

        for child_node in node.children:
            result += transpile_to_html(child_node)

        result += "</div>"

    elif node.tag_name == "Header":
        result += "<h1"

        for attr_name, attr_value in node.attributes.items():
            attr_name = transpile_attribute_name(attr_name)
            result += f' {attr_name}="{attr_value}"'

        result += f">{node.content}</h1>"

    elif node.tag_name == "Block":
        result += "<div"

        for attr_name, attr_value in node.attributes.items():
            attr_name = transpile_attribute_name(attr_name)
            result += f' {attr_name}="{attr_value}"'

        result += ">"

        for child_node in node.children:
            result += transpile_to_html(child_node)

        result += "</div>"

    elif node.tag_name == "Button":
        result += "<button"

        for attr_name, attr_value in node.attributes.items():
            attr_name = transpile_attribute_name(attr_name)
            result += f' {attr_name}="{attr_value}"'

        result += f">{node.content}</button>"

    return result


def transpile_attribute_name(attribute_name):
    if attribute_name == "idName":
        return "id"
    return attribute_name
