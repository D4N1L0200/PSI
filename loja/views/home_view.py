from django.http import HttpResponse  # type: ignore


def home_view(request) -> HttpResponse:
    links: list[str] = [
        "<a href='/produto/'>Listar produtos</a>",
        "<a href='/extra/emoji/'>Emoji</a>",
        "<a href='/extra/snake/'>Snake</a>",
        "<a href='/extra/about/'>About</a>",
    ]

    html: str = """<h1>Hello, InfoWeb!</h1>
    <ul>
    """
    for link in links:
        html += f"<li>{link}</li>"

    html += "</ul>"

    return HttpResponse(html)
