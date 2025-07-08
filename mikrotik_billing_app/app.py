from src.main import create_app, db # Import db for migration commands
from src.models import User, PackageDef, UserPackage # Import models for migration commands

app = create_app()

# This file can be used as FLASK_APP for flask cli commands
# e.g., export FLASK_APP=app.py
# flask db init
# flask db migrate -m "Initial migration with User, PackageDef, UserPackage models"
# flask db upgrade

if __name__ == '__main__':
    # Note: Running 'flask run' from CLI is preferred over app.run() here
    # when using the application factory pattern and Flask-Migrate.
    # This main block is mostly for direct execution if not using 'flask run'.
    app.run()
