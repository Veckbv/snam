from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import Comics

app = create_app('default')
manage = Manager(app)
migrate = Migrate(app, db)



manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()