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

# usage
books = read_books()
print("Listing books:")
for book in books:
  print(f"ID: {book['book_id']}, Name: {book['book_name']}, Author: {book['book_author']}")
