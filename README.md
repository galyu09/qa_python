# qa_python

**Список юнит-тестов для приложения BooksCollector**

### add_new_book

`test_add_new_book_add_two_books` - проверка на возможность добавить 2 книги 

`test_add_new_book_doubble_adding_returns_once` - негативная проверка на повторное добавление одной и той же книги

`test_add_new_book_add_incorrect_name_not_added` - негативная проверка на добавление книг с некорректыми названиями (за границами допустимого кол-ва символов)

`test_add_new_book_returns_empty_genre_list` - проверка, что новая книга добавляется с пустым жанром

### set_book_genre

`test_update_book_genre` - проверка на возможность изменить жанр книги 

`test_update_book_genre_change_unsupported_genre_returns_last_set_genre` - негативная проверка на то, что нельзя присвоить жанр, не входящий в список разрешенных

### get_books_with_specific_genre

`test_get_book_with_specific_genre` - тест на возможность выборки книг по жанрам

### get_books_for_children

`test_get_books_for_children_returns_only_children` - тест на вывод списка книг, доступных детям (книги с неразрешенными детям жанрами в список не попадают)

### add_book_in_favorites

`test_add_book_in_favorites_returns_favourite` - тест на добавление книги в список избранных 

`test_add_book_in_favorites_add_missing_book_not_added` - негативная проверка на невозможность добавить одну и ту же книгу в избранное дважды

### delete_book_from_favorites

`test_delete_book_from_favorites_remove_book` - тест на удаление книги из списка избранных (там же проверяем, что повторно удалить из списка избранных нельзя)