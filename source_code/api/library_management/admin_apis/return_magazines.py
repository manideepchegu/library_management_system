from flask import Flask, request, jsonify
from library.source_code.api.settings import logger, connection, handle_exceptions
from library.source_code.api import app


@app.route("/magazines/return/", methods=["PUT"], endpoint="return_magazine")
@handle_exceptions
def return_magazine():
    cur, conn = connection()
    logger(__name__).warning("starting the database connection")
    data = request.get_json()
    magazine_id = data['magazine_id']
    cur.execute('SELECT is_available FROM magazine_data WHERE magazine_id = %s', (magazine_id,))
    row = cur.fetchone()
    if  row[0]:
        return jsonify({'message': 'magazine is not available'}), 400

    # Update the book's availability
    cur.execute('UPDATE magazine_data SET is_available = true WHERE magazine_id = %s', (magazine_id,))
    conn.commit()

    return jsonify({'message': 'magazine returned successfully'}), 200