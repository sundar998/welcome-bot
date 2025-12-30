def parse_buttons(text: str):
    """
    Parses button text format into a list of dictionaries
    Example format:
    Button title - t.me/LinkExample
    Button title - popup: Popup text
    """
    buttons = []
    for line in text.split("\n"):
        if " - " in line:
            title, value = line.split(" - ", 1)
            buttons.append({"text": title.strip(), "value": value.strip()})
    return buttons
