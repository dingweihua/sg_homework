# -*- coding: utf-8 -*-

import os
import unittest

from decrypt import app, db
from decrypt.models import Code

class modelsTestCase(unittest.TestCase):
	def setUp(self):
		app.config['Testing'] = True
		basedir = os.path.abspath(os.path.dirname('__file__'))
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
		self.app = app.test_client()
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_code_normal_case(self):
		"""test adding/querying data"""
		# save a code
		code = Code(code='ATestCode', timestamp='2016-09-05 11:02:00')
		db.session.add(code)
		db.session.commit()

		# query the stored code
		code = Code.query.filter_by(code='ATestCode').first()
		self.assertEqual(code.code, 'ATestCode')
		self.assertEqual(code.timestamp, '2016-09-05 11:02:00')

	def test_code_unique_attr(self):
		"""test duplicate code case"""
		code = Code(code='ATestCode', timestamp='2016-09-05 11:07:00')
		db.session.add(code)
		db.session.commit()
		code = Code(code='ATestCode', timestamp='2016-09-05 11:08:00')
		with self.assertRaisesRegexp(Exception, 'UNIQUE constraint failed'):
			db.session.add(code)
			db.session.commit()

if __name__ == '__main__':
	unittest.main()