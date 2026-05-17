import os
from flask import Flask
from app.models import db
from app.routes import bp

def create_app():
    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'tasks.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(bp)

    with app.app_context():
        db.create_all()

    return app


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TaskModel(db.Model):

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    priority = db.Column(db.String(20), default='Medium', nullable=False)
    due_date = db.Column(db.String(20), nullable=True)
    category = db.Column(db.String(50), default='General', nullable=False)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)

    from datetime import datetime
    from app.models import db, TaskModel

    class TaskRepository:
        """Реализация паттерна Repository для изоляции операций с базой данных."""

        @staticmethod
        def get_all():
            """Возвращает все задачи, отсортированные по дате дедлайна."""
            return TaskModel.query.order_by(TaskModel.due_date.asc()).all()

        @staticmethod
        def get_by_id(task_id):
            """Ищет задачу по её уникальному идентификатору (ID)."""
            return TaskModel.query.get_or_404(task_id)

        @staticmethod
        def save(task):
            """Сохраняет или обновляет объект задачи в базе данных."""
            db.session.add(task)
            db.session.commit()

        @staticmethod
        def delete(task):
            """Удаляет задачу из базы данных."""
            db.session.delete(task)
            db.session.commit()

    class TaskFactory:
        """Реализация паттерна Factory для создания объектов с предварительной валидацией."""

        @staticmethod
        def create_task(title, description, priority, due_date, category):
            """
            Фабричный метод создания задачи.
            Включает бизнес-правила проверки корректности входных данных.
            """
            if not title or not title.strip():
                raise ValueError("Название задачи является обязательным полем и не может быть пустым.")

            # Установка значений по умолчанию, если поля не заполнены
            priority = priority if priority else 'Medium'
            category = category if category.strip() else 'General'

            # Валидация корректности формата даты (если передана)
            if due_date:
                try:
                    datetime.strptime(due_date, "%Y-%m-%d")
                except ValueError:
                    raise ValueError("Некорректный формат даты. Ожидается YYYY-MM-DD.")

            return TaskModel(
                title=title.strip(),
                description=description.strip() if description else "",
                priority=priority,
                due_date=due_date,
                category=category.strip()
            )

        from flask import Blueprint, render_template, request, redirect, url_for, flash
        from app.services import TaskRepository, TaskFactory

        bp = Blueprint('tasks', __name__)

        @bp.route('/')
        def index():
            """Отображение главной страницы со списком всех задач."""
            tasks = TaskRepository.get_all()
            return render_template('index.html', tasks=tasks)

        @bp.route('/add', methods=['POST'])
        def add_task():
            """Обработчик POST-запроса на добавление новой задачи."""
            title = request.form.get('title')
            description = request.form.get('description')
            priority = request.form.get('priority')
            due_date = request.form.get('due_date')
            category = request.form.get('category')

            try:
                # Использование фабрики для порождения объекта
                new_task = TaskFactory.create_task(title, description, priority, due_date, category)
                # Сохранение через репозиторий
                TaskRepository.save(new_task)
            except ValueError as e:
                # В реальном приложении здесь используется flash(str(e)) для вывода ошибки пользователю
                print(f"Ошибка валидации: {e}")

            return redirect(url_for('tasks.index'))

        @bp.route('/complete/<int:task_id>')
        def complete_task(task_id):
            """Смена статуса задачи на 'Выполнено'."""
            task = TaskRepository.get_by_id(task_id)
            task.is_completed = True
            TaskRepository.save(task)
            return redirect(url_for('tasks.index'))

        @bp.route('/delete/<int:task_id>')
        def delete_task(task_id):
            """Удаление задачи из системы."""
            task = TaskRepository.get_by_id(task_id)
            TaskRepository.delete(task)
            return redirect(url_for('tasks.index'))