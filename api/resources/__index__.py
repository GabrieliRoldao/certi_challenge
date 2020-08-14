from api.resources.number_resource import number_resource


def init_resources(app):
    app.register_blueprint(number_resource)
