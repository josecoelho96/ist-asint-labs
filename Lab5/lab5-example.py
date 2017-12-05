from bottle import Bottle, run, template, request, debug


class storage:
    def __init__(self):
        self.data = []

    def store(self, query):
        self.data.append(query)

    def show(self):
        return self.data

    def show_dic(self):
        return {"storage": self.data}


app = Bottle()
st = storage()


@app.route('/')
@app.route('/hello')
def hello():
    return "Hello World!" + " access "


# example: http://localhost:8080/number/12
@app.route('/number/<num:int>')
def num_function(num):
    return template('The url is correct <br>received the Number {{value}}', value=num)


temp = """ returning all the array<br><ul>
   %for item in list:
    <li>{{item}}</li>
   %end
</ul>"""

# example: http://localhost:8080/query?a=12
#         http://localhost:8080/query?add=12
#         http://localhost:8080/query


@app.route('/query')
def query_function():
    if len(request.query) == 0:
        return template(temp, list=st.show())
    if "add" in request.query.keys():
        st.store(request.query["add"])
        return "just inserted %s to the array<br>" % request.query["add"]
    else:
        return "query should have add argument: example: <b>http://localhost:8080/query?a=12</b>"
    # for a in request.query:
    #	print (a, request.query[a])
    #	st.store(request.query[a])
    #	return "just inserted %s to the array<br>"%request.query[a]

# example: http://localhost:8080/data


@app.route('/data')
def data_function():
    return st.show_dic()


debug(True)
run(app, host='localhost', port=8080, reloader=True)
