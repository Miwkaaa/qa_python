import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize("book_name", [
        "Ромео и Джульетта",
        "Мастер и Маргарита",
        "Король Лев"
    ])
    def test_add_new_book(self, collection, book_name):
        collection.add_new_book(book_name)
        assert book_name in collection.get_books_genre()
        assert collection.get_book_genre(book_name) == ''

    def test_set_book_genre(self, collection):
        book = "Книга"
        collection.add_new_book(book)
        collection.set_book_genre(book, "Фантастика")
        assert collection.get_book_genre(book) == "Фантастика"

    def test_get_book_genre_returns_empty_for_new_book(self, collection):
        book = "Книга"
        collection.add_new_book(book)
        assert collection.get_book_genre(book) == ''

    def test_get_book_genre_returns_correct_genre_from_dict(self, collection):
        book = "Книга"
        genre = "Детективы"
        # Проставляем жанр напрямую, без использования set_book_genre
        collection.books_genre[book] = genre
        assert collection.get_book_genre(book) == genre

    def test_set_genre_for_nonexistent_book_does_nothing(self, collection):
        collection.set_book_genre("Неизвестная книга", "Фантастика")
        assert collection.get_book_genre("Неизвестная книга") is None

    def test_get_books_with_specific_genre(self, collection_five_books):
        result = collection_five_books.get_books_with_specific_genre("Ужасы")
        assert "Чужой" in result

    def test_get_books_genre_returns_dict(self, collection):
        collection.add_new_book("1984")
        genres = collection.get_books_genre()
        assert isinstance(genres, dict)
        assert "1984" in genres

    def test_get_books_for_children_excludes_age_rated(self, collection_five_books):
        kids_books = collection_five_books.get_books_for_children()
        expected = {'Властелин колец', 'Король лев', 'Сон в летнюю ночь'}
        assert set(kids_books) == expected

    def test_add_book_in_favorites(self, collection):
        book = "Хоббит"
        collection.add_new_book(book)
        collection.add_book_in_favorites(book)
        assert book in collection.get_list_of_favorites_books()

    def test_add_book_in_favorites_for_nonexistent_book_does_nothing(self, collection):
        collection.add_book_in_favorites("Неизвестная книга")
        assert collection.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites(self, collection):
        book = "1984"
        collection.add_new_book(book)
        collection.add_book_in_favorites(book)
        collection.delete_book_from_favorites(book)
        assert book not in collection.get_list_of_favorites_books()

    def test_delete_nonexistent_book_from_favorites_does_nothing(self, collection):
        book = "1984"
        collection.add_new_book(book)
        collection.add_book_in_favorites(book)
        collection.delete_book_from_favorites("Неизвестная книга")
        assert book in collection.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_returns_correct_list(self, collection):
        book1 = "Хоббит"
        book2 = "1984"
        collection.add_new_book(book1)
        collection.add_new_book(book2)
        collection.add_book_in_favorites(book1)
        collection.add_book_in_favorites(book2)
        favorites = collection.get_list_of_favorites_books()
        assert isinstance(favorites, list)
        assert set(favorites) == {book1, book2}