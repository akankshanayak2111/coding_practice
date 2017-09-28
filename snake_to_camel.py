def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name."""

    words = variable_name.split("_")

    for i in range(1, len(words)):
    	words[i] = words[i].capitalize()

  	return "".join(words)
