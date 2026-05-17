from app import create_app

print("--- Инициализация приложения Flask ---")
app = create_app()

if __name__ == '__main__':
    print("--- Запуск локального сервера разработки ---")
    app.run(debug=True, port=5000)