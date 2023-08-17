import sqlite3

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Год: {self.year}")

def create_table():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            year INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def add_book(title, author, year):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Books (title, author, year) VALUES (?, ?, ?)', (title, author, year))
    
    conn.commit()
    conn.close()

def view_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Books')
    books = cursor.fetchall()

    for book in books:
        id, title, author, year = book
        print(f"ID: {id}, Название: {title}, Автор: {author}, Год: {year}")

    conn.close()

def update_book(id, author=None, year=None):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    update_query = 'UPDATE Books SET '
    params = []

    if author:
        update_query += 'author = ?, '
        params.append(author)
    if year:
        update_query += 'year = ?, '
        params.append(year)

    update_query = update_query.rstrip(', ') + ' WHERE id = ?'
    params.append(id)

    cursor.execute(update_query, tuple(params))
    
    conn.commit()
    conn.close()

def delete_book(title):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Books WHERE title = ?', (title,))
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()

    add_book('Война и мир', 'Лев Толстой', 1869)
    add_book('1984', 'Джордж Оруэлл', 1949)

    view_books()

    update_book(1, author='Лев Толстой (Исправлено)')

    delete_book('1984')

    view_books()

    book = Book('Гарри Поттер и философский камень', 'Дж. К. Роулинг', 1997)
    book.display_info()