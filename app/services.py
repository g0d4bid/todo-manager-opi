from datetime import datetime
from app.models import db, TaskModel

class TaskRepository:

    @staticmethod
    def get_all():
        return TaskModel.query.order_by(TaskModel.due_date.asc()).all()

    @staticmethod
    def get_by_id(task_id):
        return TaskModel.query.get_or_404(task_id)

    @staticmethod
    def save(task):
        db.session.add(task)
        db.session.commit()

    @staticmethod
    def delete(task):
        db.session.delete(task)
        db.session.commit()


class TaskFactory:

    @staticmethod
    def create_task(title, description, priority, due_date, category):

        if not title or not title.strip():
            raise ValueError("Название задачи является обязательным полем и не может быть пустым.")

        priority = priority if priority else 'Medium'
        category = category if category.strip() else 'General'

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