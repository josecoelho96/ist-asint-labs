from bottle import Bottle, run, post, get, template, request, debug

app = Bottle()


# Create a static page to link to the previous options
@app.route('/')
def homepage():
    temp = """
    <ul>
    <li><a href="/books">List of books</a></li>
    <li><a href="/authors">List of authors</a></li>
    <li><a href="/createbook">Create a book</a></li>
    <li><a href="/forms/search">[FORM] Search book by author</a></li>
    <li><a href="/forms/create">[FORM] Create a new book</a></li>
    </ul>
    """
    return temp


# List of books
# Single books(using HTTP query ?bookid=1111)
@app.route('/books')
def list_books():
    if len(request.query) == 0:
        return "List all books<br>You can search by a single book with ?bookid=book_id"
    if "bookid" in request.query.keys():
        return "List book with id %s" % request.query["bookid"]
    else:
        return "Query should have argument bookid"


# List of authors
# List of books of an author(using HTTP query ?author=aaaaaa)
@app.route('/authors')
def list_authors():
    if len(request.query) == 0:
        return "List all authors.<br>You can search by an author with ?author=author_name"
    if "author" in request.query.keys():
        return "List books written by %s" % request.query["author"]
    else:
        return "Query should have argument author"


# Creation of a book: localhost:8080/createbook?author=aaaaaaa&title=ttttttt&year=yyyyyyy
@app.route('/createbook')
def create_book():
    if "author" in request.query.keys():
        if "title" in request.query.keys():
            if "year" in request.query.keys():
                return "Added a new book:<br>Author: {}<br>Title: {}<br>Year: {}<br>".format(
                    request.query["author"],
                    request.query["title"],
                    request.query["year"])
            else:
                return "Query should have argument year.<br>Create with ?author=author_name&title=title&year=year"
        else:
            return "Query should have argument title.<br>Create with ?author=author_name&title=title&year=year"
    else:
        return "Query should have argument author.<br>Create with ?author=author_name&title=title&year=year"


# A form to search books by author
@app.get('/forms/search')  # or @app.route('/forms/search')
def form_search():
    return '''
        <form action="/forms/search" method="post">
            Author: <input name="author" type="text" />
            <input value="Search" type="submit" />
        </form>
    '''


@app.post('/forms/search')  # or @app.route('/forms/search', method='POST')
def do_form_search():
    author = request.forms.get('author')
    return "<p>Listing all books from {}</p>".format(author)


# A form to create a new book
@app.get('/forms/create')  # or @app.route('/forms/create')
def form_create():
    return '''
        <form action="/forms/create" method="post">
            Author: <input name="author" type="text" />
            Title: <input name="title" type="text" />
            Year: <input name="year" type="text" />
            <input value="Add" type="submit" />
        </form>
    '''


@app.post('/forms/create')  # or @app.route('/forms/create', method='POST')
def do_form_create():
    author = request.forms.get('author')
    title = request.forms.get('title')
    year = request.forms.get('year')
    return "Added a new book:<br>Author: {}<br>Title: {}<br>Year: {}<br>".format(author, title, year)


debug(True)
run(app, host='localhost', port=8080, reloader=True)
