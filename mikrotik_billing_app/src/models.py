import datetime
from .main import db # Import db instance from main.py

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True) # Nullable for now
    phone_number = db.Column(db.String(20), unique=True, nullable=True) # Nullable for now
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # Relationships
    user_packages = db.relationship('UserPackage', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class PackageDef(db.Model):
    __tablename__ = 'package_definitions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    price_tzs = db.Column(db.Float, nullable=False)
    duration_days = db.Column(db.Integer, nullable=False) # Duration in days
    data_limit_gb = db.Column(db.Float, nullable=True) # Data limit in GB, nullable for unlimited
    speed_limit_mbps = db.Column(db.Float, nullable=True) # Speed limit in Mbps, nullable for no limit
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    # Relationships
    user_packages = db.relationship('UserPackage', backref='package_def', lazy=True)

    def __repr__(self):
        return f'<PackageDef {self.name}>'

class UserPackage(db.Model):
    __tablename__ = 'user_packages'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    package_def_id = db.Column(db.Integer, db.ForeignKey('package_definitions.id'), nullable=False)
    purchased_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)
    data_consumed_gb = db.Column(db.Float, default=0.0)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f'<UserPackage UserID:{self.user_id} PackageDefID:{self.package_def_id} Active:{self.is_active}>'

    def calculate_expiry(self, package_duration_days):
        self.expires_at = self.purchased_at + datetime.timedelta(days=package_duration_days)
