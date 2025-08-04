import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_one_book_has_no_genre(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert collector.books_genre['Что делать, если ваш кот хочет вас убить'] == ''

    def test_set_book_genre_one_book_genre_is_added(self, collector):
        collector.add_new_book('Практикум')
        collector.set_book_genre('Практикум', 'Ужасы')
        assert collector.books_genre['Практикум'] == 'Ужасы'

    def test_get_book_genre_one_book_got_genre(self, collector):
        collector.add_new_book('Практикум')
        collector.set_book_genre('Практикум', 'Ужасы')
        assert collector.get_book_genre('Практикум') == 'Ужасы'

    def test_get_books_with_specific_genre_two_horror_book(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.add_new_book('Практикум')
        collector.set_book_genre('Практикум', 'Фантастика')
        collector.add_new_book('Каникулы')
        collector.set_book_genre('Каникулы', 'Фантастика')
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == ['Практикум', 'Каникулы']

    def test_get_books_genre_of_three_books(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Комедии')
        collector.add_new_book('Практикум')
        collector.set_book_genre('Практикум', 'Ужасы')
        collector.add_new_book('Каникулы')
        collector.set_book_genre('Каникулы', 'Фантастика')
        assert collector.get_books_genre() == {
            'Что делать, если ваш кот хочет вас убить': 'Комедии',
            'Практикум': 'Ужасы',
            'Каникулы': 'Фантастика'
        }

    def test_get_books_for_children_two_books_got_one_book_mult(self, collector):
        collector.add_new_book('Король лев')
        collector.set_book_genre('Король лев', 'Мультфильмы')
        collector.add_new_book('Практикум')
        collector.set_book_genre('Практикум', 'Ужасы')
        assert collector.get_books_for_children() == ['Король лев']

    def test_add_book_in_favorites_one_book_added_to_favorite(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Каникулы')
        collector.add_book_in_favorites('Каникулы')
        assert 'Каникулы' in collector.favorites

    def test_get_list_of_favorites_books_got_list(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Практикум')
        collector.add_new_book('Каникулы')
        collector.add_book_in_favorites('Практикум')
        collector.add_book_in_favorites('Каникулы')
        assert sorted(collector.get_list_of_favorites_books()) == sorted(['Практикум', 'Каникулы'])

    def test_delete_book_from_favorites_was_deleted_one_book(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Практикум')
        collector.add_book_in_favorites('Практикум')
        collector.delete_book_from_favorites('Практикум')
        assert len(collector.favorites) == 0