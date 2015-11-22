from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():

    file_name = request.args.get("file_name")
    print file_name
    str = open(file_name).read()
    print str
    if file_name:
        return open(file_name).read()
    return  'No file selected.'


if __name__ == "__main__":
    app.debug = True
    app.run()