from sqlalchemy import select, inspect

from library.adapters.orm import metadata


def test_database_populate_inspect_table_names(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    assert inspector.get_table_names() == ['authors', 'book_authors', 'books', 'publishers', 'reviews',
                                           'user_reading_list', 'users']


def test_database_populate_select_all_books(database_engine):
    inspector = inspect(database_engine)
    name_of_books_table = inspector.get_table_names()[2]

    with database_engine.connect() as connection:
        select_statement = select([metadata.tables[name_of_books_table]])
        result = connection.execute(select_statement)

        all_books = []
        for row in result:
            all_books.append(row['id'])

        assert all_books == [707611, 2168737, 2250580, 11827783, 12349663, 12349665, 13340336, 13571772, 17405342,
                             18711343, 18955715, 23272155, 25742454, 27036536, 27036537, 27036538, 27036539, 30128855,
                             30735315, 35452242]


def test_database_populate_select_all_users(database_engine):
    inspector = inspect(database_engine)
    name_of_users_table = inspector.get_table_names()[6]

    with database_engine.connect() as connection:
        select_statement = select([metadata.tables[name_of_users_table]])
        result = connection.execute(select_statement)

        all_users = []
        for row in result:
            all_users.append(row['user_name'])

        assert all_users == ['test1', 'test2', 'test3']


def test_database_populate_select_all_publishers(database_engine):
    inspector = inspect(database_engine)
    name_of_publishers_table = inspector.get_table_names()[3]

    with database_engine.connect() as connection:
        select_statement = select([metadata.tables[name_of_publishers_table]])
        result = connection.execute(select_statement)

        all_publishers = []
        for row in result:
            all_publishers.append(row['name'])

        assert all_publishers == ['N/A', 'Dargaud', 'Hachette Partworks Ltd.', 'N/A', 'DC Comics', 'Go! Comi',
                                  'Avatar Press', 'Avatar Press', 'Avatar Press', 'Avatar Press', 'N/A',
                                  'Dynamite Entertainment', 'VIZ Media', 'VIZ Media', 'N/A', 'Hakusensha',
                                  'Planeta DeAgostini', 'Shi Bao Wen Hua Chu Ban Qi Ye Gu Fen You Xian Gong Si',
                                  'Marvel', 'N/A']


def test_database_populate_select_all_reviews(database_engine):
    inspector = inspect(database_engine)
    name_of_reviews_table = inspector.get_table_names()[4]

    with database_engine.connect() as connection:
        select_statement = select([metadata.tables[name_of_reviews_table]])
        result = connection.execute(select_statement)

        all_reviews = []
        for row in result:
            all_reviews.append(row['reviewed_book'])

        assert all_reviews == [27036539, 27036536, 27036537, 27036539, 27036539, 27036539, 25742454, 25742454, 25742454,
                             13571772, 13571772, 707611, 27036536, 18711343, 11827783]


def test_database_populate_select_all_authors(database_engine):
    inspector = inspect(database_engine)
    name_of_authors_table = inspector.get_table_names()[0]

    with database_engine.connect() as connection:
        select_statement = select([metadata.tables[name_of_authors_table]])
        result = connection.execute(select_statement)

        all_authors = []
        for row in result:
            all_authors.append(row['id'])

        assert all_authors == [14965, 24594, 24781, 37450, 61231, 79136, 81563, 89537, 93069, 131836, 169661, 294649,
                               311098, 791996, 853385, 1015982, 1251983, 3188368, 3274315, 4346284, 4391289, 4980321,
                               5808419, 6384773, 6869276, 7359735, 7507599, 8224446, 8551671, 14155472, 16209952]