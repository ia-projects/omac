import unittest
import configparser
from core.models.base import Engine
from core.models.tasks import Task

class TestUM(unittest.TestCase):
    def setUp(self):
        # TODO : create test setup
        # config = configparser.ConfigParser()
        # config.read('omac.conf')
        # engine = config.get('test', 'engine')
        # path = config.get('test', 'path')
        # self.engine = Engine(engine, path, reset_db=True)
        pass

    def test_task_unique_subject(self):
        # TODO : test unique subject of tasks
        # task_1 = Task('Create tests')
        # session = self.engine.session()
        # session.add(task_1)
        #
        # task_2 = Task('Create test')
        # with self.failureException()
        pass

