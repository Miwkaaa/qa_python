import pytest
from main import BooksCollector


@pytest.fixture
def collection():
    return BooksCollector()


def pytest_make_parametrize_id(val):
    return repr(val)


@pytest.fixture
def collection_five_books(collection):
    collection.books_genre = {
        'Властелин колец': 'Фантастика',
        'Король лев': 'Мультфильмы',
        'Чужой': 'Ужасы',
        'Сон в летнюю ночь': 'Комедии',
        'Молчание ягнят': 'Детективы',
    }
    return collection