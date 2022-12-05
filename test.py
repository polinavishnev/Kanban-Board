import os
from app import db
import app
import unittest
import tempfile
from app.kanban_db import Task


class AppTestCase(unittest.TestCase):

    def setUp(self):
        """Sets up a test app and initializes a new database."""
        with app.app.app_context():
            self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
            app.testing = True
            self.app = app.app.test_client()
            db.drop_all()
            db.create_all()

    def tearDown(self):
        """Tears down the test database"""
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    def add(self, task, date):
        """Function to add a new task."""
        return self.app.post('/add', data=dict(
            task=task,
            status='to_do',
            date=date
        ), follow_redirects=True)

    def change_status(self, id, status):
        """Function to change task status."""
        return self.app.get('/task/' + str(id) + '/' + str(status), data=dict(
            id=id,
            status=status
        ), follow_redirects=True)

    def delete_task(self, id):
        """Function to delete task."""
        return self.app.get('/task/' + str(id), data=dict(
            id=id,
        ), follow_redirects=True)

    def test_add_task(self):
        """Test to add tasks."""
        self.add('Finish CS162 assignment!!', '2022-02-02')
        with app.app.app_context():
            task = db.session.query(Task).filter(Task.task == 'Finish CS162 assignment!!').first()
            self.assertEqual(task.task, 'Finish CS162 assignment!!')
            assert task.status == 'to_do'

    def test_move_task(self):
        """Test to change status and delete tasks."""
        self.add('Write unittests!', '2022-02-02')
        with app.app.app_context():
            task = db.session.query(Task).filter(Task.task == 'Finish CS162 assignment!!').first()
            self.change_status(task.id, 'doing')

            task = db.session.query(Task).filter(Task.task == 'Finish CS162 assignment!!').first()
            assert task.status == 'doing'

            self.change_status(task.id, 'done')
            task = db.session.query(Task).filter(Task.task == 'Finish CS162 assignment!!').first()
            assert task.status == 'done'

            self.change_status(task.id, 'to_do')
            task = db.session.query(Task).filter(Task.task == 'Finish CS162 assignment!!').first()
            assert task.status == 'to_do'

            self.delete_task(task.id)
            task = db.session.query(Task).filter(Task.id == task.id).first()
            assert task is None

    def test_validate_task(self):
        """Test to ensure non-existent tasks cannot be moved or deleted."""
        response = self.change_status(1, 'doing')
        assert b'404' in response.data
        response = self.delete_task(1)
        assert b'404' in response.data


if __name__ == '__main__':
    unittest.main()
