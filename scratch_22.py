< !DOCTYPE
html >
< html
lang = "ru" >
< head >
< meta
charset = "UTF-8" >
< title > Менеджер
задач(ОПИ
Лаб
2) < / title >
< link
rel = "stylesheet"
href = "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css" >
< / head >
< body


class ="bg-light" >

< div


class ="container mt-5" >

< h1


class ="mb-4 text-center" > Менеджер задач < / h1 >

< div


class ="card card-body mb-4 shadow-sm" >

< h5 > Создать
новую
задачу < / h5 >
< form
action = "/add"
method = "POST"


class ="row g-3" >

< div


class ="col-md-4" >

< input
type = "text"
name = "title"


class ="form-control" placeholder="Название задачи" required >

< / div >
< div


class ="col-md-4" >

< input
type = "text"
name = "description"


class ="form-control" placeholder="Описание (необязательно)" >

< / div >
< div


class ="col-md-4" >

< input
type = "text"
name = "category"


class ="form-control" placeholder="Категория (например: Учеба)" >

< / div >
< div


class ="col-md-4" >

< select
name = "priority"


class ="form-select" >

< option
value = "Low" > Низкий
приоритет < / option >
< option
value = "Medium"
selected > Средний
приоритет < / option >
< option
value = "High" > Высокий
приоритет < / option >
< / select >
< / div >
< div


class ="col-md-4" >

< input
type = "date"
name = "due_date"


class ="form-control" >

< / div >
< div


class ="col-md-4 d-grid" >

< button
type = "submit"


class ="btn btn-primary" > Добавить задачу < / button >

< / div >
< / form >
< / div >

< div


class ="card card-body shadow-sm" >

< h5 > Текущие
задачи < / h5 >
< table


class ="table table-hover mt-3" >

< thead >
< tr >
< th > Статус < / th >
< th > Название < / th >
< th > Описание < / th >
< th > Категория < / th >
< th > Приоритет < / th >
< th > Дедлайн < / th >
< th > Действия < / th >
< / tr >
< / thead >
< tbody >
{ %
for task in tasks %}
< tr


class ="{% if task.is_completed %}table-success text-muted{% endif %}" >

< td >
{ % if task.is_completed %}
< span


class ="badge bg-success" > Выполнено < / span >


{ % else %}
< span


class ="badge bg-warning text-dark" > Активна < / span >


{ % endif %}
< / td >
< td > { % if task.is_completed %} < del > {{task.title}} < / del > { % else %}{{task.title}}
{ % endif %} < / td >
< td > {{task.description}} < / td >
< td > < span


class ="badge bg-secondary" > {{task.category}} < / span > < / td >

< td >
< span


class ="badge {% if task.priority == 'High' %}bg-danger{% elif task.priority == 'Medium' %}bg-primary{% else %}bg-info{% endif %}" >


{{task.priority}}
< / span >
< / td >
< td > {{task.due_date if task.due_date else 'Нет срока'}} < / td >
< td >
{ % if not task.is_completed %}
< a
href = "/complete/{{ task.id }}"


class ="btn btn-sm btn-success" > Выполнить < / a >


{ % endif %}
< a
href = "/delete/{{ task.id }}"


class ="btn btn-sm btn-danger" > Удалить < / a >

< / td >
< / tr >
{ % endfor %}
< / tbody >
< / table >
< / div >
< / div >
< / body >
< / html >