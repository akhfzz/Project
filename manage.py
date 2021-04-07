from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
from Prosses.__init__ import app, engine, dbs, db

# app.config.from_object(os.environ['APP_SETTING'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()