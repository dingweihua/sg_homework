from decrypt import db

class Code(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(64), index = True, unique = True)
    timestamp = db.Column(db.String(64))
    
    def __repr__(self): 
        return '<Code: %r>' % (self.code)