from flask import Flask

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
from library.source_code.api.library_management.admin_apis import add_to_library, add_magazines, borrow_magazines,borrow_magazines, borrowing_book, delete_book, return_magazines, return_book
from library.source_code.api.library_management.functional_apis import books_available, particular_book
