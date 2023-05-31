def transpile_to_html(node):
    transpile_functions = {
        "Container": transpile_container,
        "Header": transpile_header,
        "Block": transpile_block,
        "Button": transpile_button
    }

    if node.tag_name in transpile_functions:
        transpile_func = transpile_functions[node.tag_name]
        return transpile_func(node)
    
    # Default transpilation for unknown tags
    return transpile_unknown(node)


def transpile_container(node):
    result = "<div"

    for attr_name, attr_value in node.attributes.items():
        result += f' {attr_name}="{attr_value}"'

    result += ">"

    for child_node in node.children:
        result += transpile_to_html(child_node)

    result += "</div>"
    return result


def transpile_header(node):
    result = "<h1"

    for attr_name, attr_value in node.attributes.items():
        result += f' {attr_name}="{attr_value}"'

    result += f">{node.content}</h1>"
    return result


def transpile_block(node):
    result = "<div"

    for attr_name, attr_value in node.attributes.items():
        result += f' {attr_name}="{attr_value}"'

    result += ">"

    for child_node in node.children:
        result += transpile_to_html(child_node)

    result += "</div>"
    return result


def transpile_button(node):
    result = "<button"

    for attr_name, attr_value in node.attributes.items():
        result += f' {attr_name}="{attr_value}"'

    result += f">{node.content}</button>"
    return result


def transpile_unknown(node):
    # Default transpilation for unknown tags
    result = f"<{node.tag_name}"

    for attr_name, attr_value in node.attributes.items():
        result += f' {attr_name}="{attr_value}"'

    result += f">{node.content}</{node.tag_name}>"
    return result
