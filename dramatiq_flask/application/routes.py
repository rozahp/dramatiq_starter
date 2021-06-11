from flask import current_app as app

@app.route('/', methods=['GET'])
def index():
    """ index route."""
    return "Yes! This is the index!\n"

