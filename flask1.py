from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add():
    # a = request.form["a"]
    # b = request.form["b"]
    # c = request.form["c"]
    return "Hello World" #str(int(a) + int(b) + int(c))

# def predict(house_size, house_beds):
#     prediction = ml_model.predict(house_size, house_beds)
#     return prediction


if __name__ == '__main__':
    app.run(port=7000)

