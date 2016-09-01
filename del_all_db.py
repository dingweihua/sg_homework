from decrypt import db, models

codes = models.Code.query.all()

for code in codes: 
    db.session.delete(code)

db.session.commit()