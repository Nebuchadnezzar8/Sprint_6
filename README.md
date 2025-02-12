# Sprint_6

## Описание проекта
Автотесты для сервиса заказа самокатов

## Структура проекта
- **helpers/**: Содержит вспомогательные модули.
  - `data.py`: Тестовые данные.
  - `generator.py`: Генерация данных для тестов.
  - `urls.py`: Хранение URL-адресов, используемых в тестах.
- **locators/**: Содержит локаторы элементов веб-страниц.
  - `main_page_locators.py`: Локаторы для главной страницы.
  - `order_page_locators.py`: Локаторы для страницы заказа.
- **pages/**: Реализация Page Object Model.
  - `base_page.py`: Базовый класс для страниц.
  - `main_page.py`: Класс для главной страницы.
  - `order_page.py`: Класс для страницы заказа.
- **tests/**: Содержит тесты.
  - `test_main_page.py`: Тесты для главной страницы.
  - `test_order_page.py`: Тесты для страницы заказа.
- **конфигурационные файлы**:
  - `.gitignore`: Исключение файлов из контроля версий.
  - `conftest.py`: Фикстуры и общие настройки для тестов.
  - `pytest.ini`: Настройки для Pytest.
  - `requirements.txt`: Список зависимостей.

## Требования
- Python 3.x  
- Selenium WebDriver  
- Pytest  
- Allure  

## Установка
1. Клонируйте репозиторий:  
   ```bash
   git clone https://github.com/Nebuchadnezzar8/Sprint_6.git

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt

## Запуск тестов:
    pytest


## Сформировать отчет в Allure:
   ```bash
   allure serve allure_results
