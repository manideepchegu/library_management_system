from flask import Flask, request, jsonify
from library.source_code.api.settings import logger, connection, handle_exceptions
from library.source_code.api import app



@app.route("/books/add", methods=["POST"], endpoint="add_to_library")
@handle_exceptions
def add_to_library():
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    if "title" and "author" and "published_date" and "is_available" not in request.json:
        raise Exception("details missing")
    data = request.get_json()
    title = data['title'],
    author = data['author'],
    published_date = data['published_date'],
    is_available = data['is_available']
    cur.execute(
        'INSERT INTO books_data (title, author, published_date, is_available) VALUES (%s, %s, %s, %s)', (title, author, published_date, is_available))
    conn.commit()
    logger(__name__).warning("closing the database connection")
    return jsonify({'message': 'Book added successfully'}), 201