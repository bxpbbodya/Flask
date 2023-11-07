from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/hello-world-16', methods=['GET'])
def hello_world():
    return 'Hello World 16', 200

@app.errorhandler(404)
def page_not_found(error):
    return 'Сторінка не знайдена', 404

if __name__ == '__main__':
    app.run()
