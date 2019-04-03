from bottle import Bottle, template

app = Bottle()

@app.route('/')
def index():
    """Home page"""

    info = {'title': 'Welcome Home!',
            'content': 'Hello World'
            }

    return template('simple.tpl', info)

if __name__ == '__main__':
    app.run()
