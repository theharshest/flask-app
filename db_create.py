from app import db
from models import BlogPost

# create the db and db tables
db.create_all()

# insert
db.session.add(BlogPost("Good", "I'm good."))
db.session.add(BlogPost("Bad", "I'm unwell."))

# commit the changes
db.session.commit()