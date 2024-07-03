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

def read_book(book_id=None, book_name=None, book_author=None):
  """Reads book data based on provided criteria and returns a dictionary."""
  connection = connect_to_database()
  if connection is None:
    return None
  try:
    cursor = connection.cursor()
    where_clause = []
    params = []
    if book_id:
      where_clause.append("book_id = %s")
      params.append(book_id)
    if book_name:
      where_clause.append("book_name = %s")
      params.append(book_name)
    if book_author:
      where_clause.append("book_author = %s")
      params.append(book_author)
    query = f"SELECT book_id, book_name, book_author FROM books WHERE {' AND '.join(where_clause)}"
    cursor.execute(query, params)
    #print(query)
    #print(params)
    book = dict(zip(["book_id", "book_name", "book_author"], cursor.fetchone()))
    connection.commit()
    return book
  except mysql.connector.Error as err:
    print("Error reading data:", err)
    return None
  finally:
    connection.close()

def update_book(book_id, new_book_name=None, new_book_author=None):
  """Updates a book record based on ID and optionally changes name or author."""
  connection = connect_to_database()
  if connection is None:
    return
  try:
    cursor = connection.cursor()
    set_clause = []
    params = []
    
    if new_book_name:
      set_clause.append("book_name = %s")
      params.append(new_book_name)
    if new_book_author:
      set_clause.append("book_author = %s")
      params.append(new_book_author)
    params.append(book_id)
    query = f"UPDATE books SET {' , '.join(set_clause)} WHERE book_id = %s"
    #print(query)
    #print(params)
    cursor.execute(query, params)
    
    connection.commit()
    print(f"Book with ID {book_id} updated successfully!")
  except mysql.connector.Error as err:
    print("Error updating data:", err)
  finally:
    connection.close()

def delete_book(book_id=None, book_name=None, book_author=None):
  """Deletes a book record based on provided criteria."""
  connection = connect_to_database()
  if connection is None:
    return
  try:
    cursor = connection.cursor()
    where_clause = []
    params = []
    if book_id:
      where_clause.append("book_id = %s")
      params.append(book_id)
    if book_name:
      where_clause.append("book_name = %s")
      params.append(book_name)
    if book_author:
      where_clause.append("book_author = %s")
      params.append(book_author)
    query = f"DELETE FROM books WHERE {' AND '.join(where_clause)}"
    cursor.execute(query, params)
    connection.commit()
    deleted_count = cursor.rowcount
    print(f"{deleted_count} book(s) deleted successfully!")
  except mysql.connector.Error as err:
    print("Error deleting data:", err)
  finally:
    connection.close()

# Example usage
# Get user input for modification or deletion
choice = input("Enter (u) to update, (d) to delete, or (r) to read a book: ")
if choice.lower() == 'u':
  # Update a book
  book_id = int(input("Enter book ID to update: "))
  new_name = input("Enter new book name (leave blank to keep existing): ")
  new_author = input("Enter new book author (leave blank to keep existing): ")
  update_book(book_id, new_name, new_author)
elif choice.lower() == 'd':
  # Delete a book
  delete_choice = input("Delete by (i)d, (n)ame, or (a)uthor? ")
  if delete_choice.lower() == 'i':
    book_id = int(input("Enter book ID to delete: "))
    delete_book(book_id=book_id)
  elif delete_choice.lower() == 'n':
    book_name = input("Enter book name to delete: ")
    delete_book(book_name=book_name)
  elif delete_choice.lower() == 'a':
    book_author = input("Enter book author to delete: ")
    delete_book(book_author=book_author)
  else:
    print("Invalid deletion criteria. Please try again.")
elif choice.lower() == 'r':
  # Read a book
  read_choice = input("Read by (i)d, (n)ame, or (a)uthor? ")
  if read_choice.lower() == 'i':
    book_id = int(input("Enter book ID to read: "))
    book = read_book(book_id=book_id)
  elif read_choice.lower() == 'n':
    book_name = input("Enter book name to read: ")
    book = read_book(book_name=book_name)
  elif read_choice.lower() == 'a':
    book_author = input("Enter book author to read: ")
    book = read_book(book_author=book_author)
  else:
    print("Invalid read criteria. Please try again.")
  if book:
    print(f"\nBook details:")
    print(f"ID: {book['book_id']}, Name: {book['book_name']}, Author: {book['book_author']}")
  else:
    print("Book not found.")
else:
  print("Invalid choice. Please try again.")
