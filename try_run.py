from decrypt import db, models

codes = models.Code.query.all()
#import pdb; pdb.set_trace()

code = models.Code(code = 'dfakdfDHUFQE', timestamp = '2015-06-29-11:27:27')
db.session.add(code)
code = models.Code(code = 'dafdeur', timestamp = '2015-06-29-11:28:27')
db.session.add(code)
db.session.commit()