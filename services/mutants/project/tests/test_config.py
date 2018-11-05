import os
import unittest

from flask import current_app
from flask_testing import TestCase

from project import create_app

app = create_app()


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')
        self.assertFalse(current_app is None)
        self.assertTrue(app.config['DEBUG_TB_ENABLED'])
        self.assertEqual(app.config['MONGO_URI'], os.environ.get('MONGO_URI'))


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertFalse(app.config['DEBUG_TB_ENABLED'])
        self.assertEqual(app.config['MONGO_URI'], os.environ.get('MONGO_URI_TEST'))


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['SECRET_KEY'] == '-6hu0sr=qd*t4*&osv*d=4wjg3n#*0pkl#=(!va$8%#m6+0ekm')
        self.assertFalse(app.config['TESTING'])
        self.assertFalse(app.config['DEBUG_TB_ENABLED'])
        self.assertEqual(app.config['MONGO_URI'], os.environ.get('MONGO_URI'))


if __name__ == '__main__':
    unittest.main()
