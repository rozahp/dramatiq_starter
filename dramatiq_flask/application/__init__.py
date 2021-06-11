from flask import Flask
import os
import atexit
import logging
import dramatiq_dashboard

def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # logger
    logging.basicConfig(level=app.config["LOGGING_LEVEL"])

    # dramatiq_dashboard
    from .tasks import dramatiq
    dashboard_middleware = dramatiq_dashboard.make_wsgi_middleware(app.config['DASHBOARD_PREFIX'])
    app.wsgi_app = dashboard_middleware(app.wsgi_app)

    # atexit
    def interupt(Observer):
        app.logger.debug("Interupt entered")
        Observer.stop()
        Observer.join()

    with app.app_context():

        # Include our Routes
        from . import routes

        # watcher process
        from . import watcher
        if not app.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
            pass
        else:
            Observer = watcher.startObserver(app.config["WATCHER_PATH"])
            atexit.register(interupt, Observer)
        return app
