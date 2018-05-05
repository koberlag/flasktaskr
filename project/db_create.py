# project/db_create.py

from views import db
from models import Task
from datetime import date, datetime


# create the database and the db table
db.create_all()
datetime
# insert data
db.session.add(Task("Finish this tutorial", date(2010, 9, 22), 10, datetime.utcnow(), 1, 1))
db.session.add(Task("Finish Real Python", date(2010, 10, 3), 10, datetime.utcnow(), 1, 1))

# commit the changes
db.session.commit()