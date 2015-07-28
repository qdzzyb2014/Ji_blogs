from app import db, models

user = models.User(user_name='qdzzyb',password='wlj199272',email='qdzzyb@163.com')
db.session.add(user)
db.session.commit()