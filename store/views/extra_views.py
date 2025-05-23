import random
from django.http import HttpResponse  # type: ignore


def emoji_view(request):
    emojis = ["😺", "🚀", "🍕", "🎮", "🌈", "🐉", "📚", "🦄"]
    return HttpResponse(
        f"Hello from Django! Here's a random emoji: {random.choice(emojis)}"
    )


def snake_view(request):
    maxi = 20
    maxloops = 20
    text = "Hello, InfoWeb!"

    out = ""

    for l in range(maxloops):
        for i in range(maxi):
            even = l % 2 == 0
            if even:
                out += "<p>" + "&nbsp;" * 2 * i + text + "</p><br>"
            else:
                out += "<p>" + "&nbsp;" * 2 * (maxi - i) + text + "</p><br>"

    css = "<style>* {  margin: 0; padding: 0; }p { margin: -6px 0; }</style>"

    return HttpResponse(css + out)


def about_view(request):
    quotes = [
        "The best way to predict the future is to invent it.",
        "In the middle of difficulty lies opportunity.",
        "Life is short. Code fast.",
        "Keep calm and debug.",
        "Computers are fast; programmers keep it slow.",
    ]

    html_content = f"""
    <html>
        <head>
            <title>About This Site</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #f0f0f0;
                    padding: 40px;
                }}
                .container {{
                    background-color: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                    max-width: 600px;
                    margin: auto;
                }}
                h1 {{
                    color: #333;
                }}
                p {{
                    font-size: 1.1em;
                    color: #666;
                }}
                .quote {{
                    margin-top: 20px;
                    font-style: italic;
                    color: #555;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>About This Site</h1>
                <p>This is a random Django demo created just for fun.</p>
                <p>It features emojis, quotes, and whatever else you can imagine.</p>
                <div class="quote">💬 Quote of the Day:<br><strong>"{random.choice(quotes)}"</strong></div>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html_content)
