import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'kbufktutyl'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'kartoev.ali@gmail.com'
	MAIL_PASSWORD = 'Veckbv3888870'
	SNAM_MAIL_SENDER = 'Snam Admin <snam@example.com>'
	SNAM_ADMIN = os.environ.get('SNAM_ADMIN') or 'kartoev.ali@gmail.com'
	


class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'postgresql://ali:rfhnjtd3888870@localhost/dev_snam'

class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'postgresql://ali:rfhnjtd3888870@localhost/test_snam'
	WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'postgresql://ali:rfhnjtd3888870@localhost/prod_snam'


config = {
	'development' : DevelopmentConfig,
	'testing' : TestingConfig,
	'production' : ProductionConfig,

	'default' : DevelopmentConfig
}
