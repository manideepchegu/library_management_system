
from flask import Flask, jsonify
from library.source_code.api.settings import logger, connection, handle_exceptions
from library.source_code.api import app



# books available in the library
@app.route("/books/all", methods=["GET"], endpoint="all_books")
@handle_exceptions
def all_books():
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    cur.execute('SELECT *  FROM books_data')
    rows = cur.fetchall()
    print(rows)
    if not rows:
        return jsonify({"message": f"No rows found "})
    data_list = []
    for row in rows:
        book_id,title, author, published_date, is_available = row
        data = {
            'book_id' : book_id,
            'title' : title,
            'author' : author,
            'published_date' : published_date,
            'is_available' : is_available
        }
        data_list.append(data)
        logger(__name__).warning("close the database connection")
    print(data_list)
    return jsonify({"message":"all books", "details":data_list})

