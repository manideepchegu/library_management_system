from flask import Flask, request, jsonify
from library.source_code.api.settings import logger, connection, handle_exceptions
from library.source_code.api import app



# book borrowing
@app.route("/books/update/", methods=["PUT"], endpoint="borrow_book")
@handle_exceptions
def borrow_book():
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    data = request.get_json()
    book_id = data['book_id']
    cur.execute('SELECT is_available FROM books_data WHERE book_id = %s', (book_id,))
    row = cur.fetchone()
    if not row[0]:
        return jsonify({'message': 'Book is not available'}), 400

    # Update the book's availability
    cur.execute('UPDATE books_data SET is_available = false WHERE book_id = %s', (book_id,))
    conn.commit()

    return jsonify({'message': 'Book borrowed successfully'}), 200
