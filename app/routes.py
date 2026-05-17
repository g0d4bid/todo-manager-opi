from flask import Blueprint, render_template, request, redirect, url_for
from app.services import TaskRepository, TaskFactory

bp = Blueprint('tasks', __name__)

@bp.route('/')
def index():
    tasks = TaskRepository.get_all()
    return render_template('index.html', tasks=tasks)

@bp.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    priority = request.form.get('priority')
    due_date = request.form.get('due_date')
    category = request.form.get('category')

    try:
        new_task = TaskFactory.create_task(title, description, priority, due_date, category)
        TaskRepository.save(new_task)
    except ValueError as e:
        print(f"Ошибка валидации: {e}")

    return redirect(url_for('tasks.index'))

@bp.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = TaskRepository.get_by_id(task_id)
    task.is_completed = True
    TaskRepository.save(task)
    return redirect(url_for('tasks.index'))

@bp.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = TaskRepository.get_by_id(task_id)
    TaskRepository.delete(task)
    return redirect(url_for('tasks.index'))