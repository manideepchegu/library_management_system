
from flask import Flask, request, jsonify
from library.source_code.api.settings import logger, connection, handle_exceptions
from library.source_code.api import app

@app.route("/books/<int:book_id>", methods=["GET"], endpoint="particular_book")
@handle_exceptions
def particular_book(book_id):
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    cur.execute('SELECT title, author, published_date, is_available FROM books_data WHERE book_id = %s',(book_id,))
    rows = cur.fetchone()
    if not rows:
        return jsonify({"message": f"No rows found "})
    data_list = []
    title, author, published_date, is_available = rows
    data = {

        'title': title,
        'author': author,
        'published_date': published_date,
        'is_available': is_available
    }
    data_list.append(data)
    logger(__name__).warning("close the database connection")

    return jsonify({"message": book_id,  "details": data_list})
