import os
# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = '7\xd5D@\xcb\x1f#\x88?\xa4T\x03\xa9*\xf8\xfa\xd4j\xa9\xd8\xee{v\xed'

# define the full path for the databse
DATABASE_PATH = os.path.join(basedir, DATABASE)