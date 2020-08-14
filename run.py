from flask import Flask
from api.resources.__index__ import init_resources

# Run the application
if __name__ == '__main__':
    app = Flask(__name__)
    init_resources(app)
    app.run(host='0.0.0.0', debug=True)