import mysql.connector

# Database connection details (replace with your own)
hostname = "localhost"
username = "root"
password = ""
database = "bookstore"

def connect_to_database():
  """Establishes a connection to the MySQL database."""
  try:
    connection = mysql.connector.connect(
        host=hostname, user=username, password=password, database=database
    )
    return connection
  except mysql.connector.Error as err:
    print("Error connecting to database:", err)
    return None

def read_books():
  """Reads all book data from the database and returns a list of dictionaries."""
  connection = connect_to_database()
  if connection is None:
    return []
  try:
    cursor = connection.cursor()
    cursor.execute("SELECT book_id, book_name, book_author FROM books")
    books = [dict(zip(["book_id", "book_name", "book_author"], row)) for row in cursor]
    connection.commit()
    return books
  except mysql.connector.Error as err:
    print("Error reading data:", err)
    return []
  finally:
    connection.close()

def write_book(book_id, book_name, book_author):
  """Writes a new book record to the database."""
  connection = connect_to_database()
  if connection is None:
    return
  try:
    cursor = connection.cursor()
    sql = "INSERT INTO books (book_id, book_name, book_author) VALUES (%s, %s, %s)"
    cursor.execute(sql, (book_id, book_name, book_author))
    connection.commit()
    print("Book added successfully!")
  except mysql.connector.Error as err:
    print("Error writing data:", err)
  finally:
    connection.close()

# usage
books = read_books()
print("Existing books:")
for book in books:
  print(f"ID: {book['book_id']}, Name: {book['book_name']}, Author: {book['book_author']}")

# Add a new book (replace with your desired values)
new_book_id = int(input("Enter book ID: "))
new_book_name = input("Enter book name: ")
new_book_author = input("Enter book author: ")
write_book(new_book_id, new_book_name, new_book_author)

# Read books again to see the update
books = read_books()
print("\nBooks after adding a new record:")
for book in books:
  print(f"ID: {book['book_id']}, Name: {book['book_name']}, Author: {book['book_author']}")
