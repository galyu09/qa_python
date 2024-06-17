# Фикстура для создания экземпляра класса BooksCollector
import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture
def book_list(collector):
    collector = BooksCollector()
    book_list = [
        ('Незнайка', 'Мультфильмы'),
        ('Шерлок Холмс', 'Детективы'),
        ('Гарри Поттер', 'Фантастика'),
        ('Пикник на обочине', 'Фантастика'),
        ('Маленький принц', 'Мультфильмы'),
        ('Тёмная башня', 'Ужасы')
    ]
    for name, genre in book_list:
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector
