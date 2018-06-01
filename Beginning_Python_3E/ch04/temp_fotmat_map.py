template = '''<html>
            <head><title>{title}</title></head>
            <body>
            <h1>{title}</h1>
            <p>{text}</p>
            </body>
            </html>'''

data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}

print(template.format_map(data))
