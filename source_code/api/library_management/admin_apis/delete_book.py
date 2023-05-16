from flask import Flask, request, jsonify
from library.source_code.api.settings import logger, connection, handle_exceptions
from library.source_code.api import app



@app.route("/books/delete/<int:book_id>",methods=["DELETE"],endpoint="delete_book")
def delete_book(book_id):
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    cur.execute('DELETE FROM books_data WHERE book_id=%s', (book_id,))
    logger(__name__).warning("close the database connection")
    conn.commit()
    if cur.rowcount > 0:
        return jsonify({"message": "book deleted successfully"})
    else:
        return jsonify({"message": "book_id  not found"})

