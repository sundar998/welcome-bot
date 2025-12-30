def bold(text: str) -> str:
    return f"<b>{text}</b>"

def italic(text: str) -> str:
    return f"<i>{text}</i>"

def code(text: str) -> str:
    return f"<code>{text}</code>"

def link(text: str, url: str) -> str:
    return f'<a href="{url}">{text}</a>'
