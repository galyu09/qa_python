import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        books = ['Гордость и предубеждение', 'Что делать, если ваш кот хочет вас убить']
        for book in books:
            collector.add_new_book(book)
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_doubble_adding_returns_once(self, collector):
        collector.add_new_book('Книга')
        collector.add_new_book('Книга') # проверяем, что дважды одна и та же книга не добавится
        assert len(collector.get_books_genre()) == 1

    # Проверка граничных значений в названии книг

    @pytest.mark.parametrize('name,count',
                             [('', 0),
                              ('К', 1),
                              ('КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнига1', 0),
                              ('КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнига', 1),
                              ('Книга', 1)])
    def test_add_new_book(self, name, count, collector):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == count

    def test_add_new_book_returns_empty_genre_list(self, collector):
        collector.add_new_book('Белый клык')
        assert '' in collector.get_book_genre('Белый клык')
        # assert len(collector.get_books_genre()) == 1

    def test_update_book_genre(self, book_list):
        book_list.set_book_genre('Незнайка', 'Ужасы')
        assert book_list.get_book_genre('Незнайка') == 'Ужасы'

    def test_update_book_genre_change_unsupported_genre_returns_last_set_genre(self, book_list):
        book_list.set_book_genre('Гарри Поттер', 'Эротика')
        assert book_list.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_get_books_with_specific_genre(self, book_list):
        assert len(book_list.get_books_with_specific_genre('Фантастика')) == 2

    def test_get_books_for_children_returns_only_children(self, book_list):
        children_books = book_list.get_books_for_children()
        assert len(children_books) == 4

    def test_add_book_in_favorites_returns_favourites(self, book_list):
        book_list.add_book_in_favorites('Незнайка')
        book_list.add_book_in_favorites('Незнайка')  # должна быть добавлена только один раз
        assert len(book_list.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_add_missing_book_not_added(self, book_list):
        book_list.add_book_in_favorites('Книга не из списка')
        assert len(book_list.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_remove_book(self, book_list):
        book_list.add_book_in_favorites('Гарри Поттер')
        book_list.delete_book_from_favorites('Гарри Поттер')
        book_list.delete_book_from_favorites('Гарри Поттер')  # проверяем, что повторно удалить из списка избранных нельзя
        assert 'Гарри Поттер' not in book_list.get_list_of_favorites_books() and len(book_list.get_list_of_favorites_books()) == 0
