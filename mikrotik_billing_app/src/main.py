import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize SQLAlchemy instance
db = SQLAlchemy()
# Initialize Migrate instance
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configuration
    database_dir = os.environ.get('DATABASE_DIR', '/app/data')
    if not os.path.exists(database_dir):
        os.makedirs(database_dir)

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(database_dir, 'billing.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    # Initialize Flask-Migrate
    # Models need to be imported for migrate to detect them
    from . import models
    migrate.init_app(app, db)


    @app.route('/')
    def hello_world():
        return 'Hello, MikroTik Billing App! Database configured with Migrations.'

    # Import models for access elsewhere if needed, already imported for Migrate
    # from . import models

    return app

if __name__ == '__main__':
    # This part is mainly for running the Flask development server directly.
    # Migrations should ideally be handled by 'flask db' commands.
    app = create_app()

    # The db.create_all() call is generally not needed when using Flask-Migrate,
    # as migrations handle table creation. However, for initial simple non-containerized
    # execution or testing, it might be useful. For container deployment,
    # 'flask db upgrade' should be the way to set up the DB.
    # For now, I'll leave it commented out to encourage migration usage.
    # with app.app_context():
    #     db.create_all()

    app.run(host='0.0.0.0', port=8080)
