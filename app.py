from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import icecreams
from werkzeug import exceptions
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
CORS(app)

class Fact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fact = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.id}.{self.fact}'

@app.route('/')
def home():
    return jsonify({'message': 'Hello from APIcecream!'}), 200

@app.route('/facts', methods=['GET', 'POST'])
def facts_handler():
    fns = {
        'GET': icecreams.index,
        'POST': icecreams.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/facts/<int:fact_id>', methods=['GET', 'DELETE'])
def fact_handler(fact_id):
    fns = {
        'GET': icecreams.show,
        'DELETE': icecreams.destroy
    }
    resp, code = fns[request.method](request, fact_id)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)
