import unittest
from app import create_app
from app.models import db, TaskModel
from app.services import TaskFactory, TaskRepository

class TodoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_task_factory_valid_creation(self):

        title = "Защитить лабу"
        category = "Учеба"
        priority = "Высокий"

        task = TaskFactory.create_task(title=title, description="CI/CD", priority=priority, due_date="2026-05-20",
                                       category=category)

        self.assertEqual(task.title, title)
        self.assertEqual(task.category, category)
        self.assertEqual(task.priority, priority)
        self.assertFalse(task.is_completed)

    def test_task_factory_invalid_title(self):

        with self.assertRaises(ValueError):
            TaskFactory.create_task(title="", description="Сбой", priority="Низкий", due_date="2026-05-20",
                                    category="Ошибки")

    def test_repository_save_and_get(self):
        task = TaskFactory.create_task(title="Тестовая задача", description="...", priority="Средний",
                                       due_date="2026-05-20", category="Тест")

        TaskRepository.save(task)
        saved_tasks = TaskRepository.get_all()

        self.assertEqual(len(saved_tasks), 1)
        self.assertEqual(saved_tasks[0].title, "Тестовая задача")


    def test_index_page_status_code(self):

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_functional_add_task_via_form(self):

        response = self.client.post('/add', data={
            'title': 'Интеграционный тест',
            'description': 'Проверка формы',
            'priority': 'Низкий',
            'due_date': '2026-05-20',
            'category': 'Работа'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'\xd0\x98\xd0\xbd\xd1\x82\xd0\xb5\xd0\xb3\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x82\xd0\xb5\xd1\x81\xd1\x82',
            response.data)


if __name__ == '__main__':
    unittest.main()