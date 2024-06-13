import pytest
from main import BooksCollector


class TestBooksCollector:

    # Фикстура для создания экземпляра класса BooksCollector
    @pytest.fixture
    def collector(self):
        collector = BooksCollector()
        return collector


    def test_adding_books(self, collector):
        name1 = 'Белый клык'
        name2 = 'Как украсть миллион'
        collector.add_new_book(name1)
        collector.add_new_book(name2)
        # Проверяем, что книга была добавлена с пустым жанром
        assert '' in collector.get_book_genre(name1)
        assert [name1, name2] == list(collector.get_books_genre().keys())
        assert len(collector.get_books_genre()) == 2

    def test_update_book_genre(self, collector):
        name = 'Одиночество в сети'
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Фантастика')
        assert collector.get_book_genre(name) == 'Фантастика'
        collector.set_book_genre(name, 'Мультфильмы')
        assert collector.get_book_genre(name) == 'Мультфильмы'
        collector.set_book_genre(name, 'Эротика')
        assert collector.get_book_genre(name) == 'Мультфильмы'

    def test_get_book_with_specific_genre(self, collector):
        name1 = 'Специфичная книга_детектив'
        name2 = 'Спец_книга_комедия'
        name3 = 'спец_книга_ужасы'
        collector.add_new_book(name1)
        collector.add_new_book(name2)
        collector.add_new_book(name3)
        collector.set_book_genre(name1, 'Детективы')
        collector.set_book_genre(name2, 'Комедия')
        collector.set_book_genre(name3, 'Детективы')
        assert len(collector.get_books_with_specific_genre('Детективы')) == 2

    @pytest.mark.parametrize("book_list, expected_children_count", [
        ([
             ('Незнайка', 'Мультфильмы'),
             ('Шерлок Холмс', 'Детективы'),
             ('Гарри Поттер', 'Фантастика'),
             ('Пикник на обочине', 'Фантастика'),
             ('Маленький принц', 'Мультфильмы'),
             ('Тёмная башня', 'Ужасы')
         ], 4)
    ])
    def test_get_books_for_children_returns_only_children(self, book_list, expected_children_count, collector):
        for name, genre in book_list:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        children_books = collector.get_books_for_children()
        assert len(children_books) == expected_children_count
        for name, genre in book_list:
            if genre not in collector.genre_age_rating:
                assert name in children_books
            else:
                assert name not in children_books

    def test_add_book_in_favorites_returns_vavourite(self, collector):
        name = 'I like this book'
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name) # должна быть добавлена только один раз
        assert len(collector.get_list_of_favorites_books()) == 1
        assert name in collector.get_list_of_favorites_books()

        # assert name in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_remove_book(self, collector):
        name = 'book I dislike'
        name1 = 'I like this book'
        collector.add_new_book(name)
        collector.add_new_book(name1)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name1)
        collector.delete_book_from_favorites(name)
        collector.delete_book_from_favorites(name) # проверяем, что повторно удалить из списка избранных нельзя
        assert len(collector.get_list_of_favorites_books()) == 1
        assert name not in collector.get_list_of_favorites_books()
        assert name1 in collector.get_list_of_favorites_books()

