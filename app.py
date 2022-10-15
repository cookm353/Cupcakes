"""Flask app for Cupcakes"""
from flask import Flask, render_template, abort, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from models import Cupcake, connect_db
from forms import CupcakeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'yummy'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_home():
    """Display homepage"""
    form = CupcakeForm()
    cupcakes = Cupcake.get_cupcakes()
    
    return render_template('index.html', form=form, cupcakes=cupcakes)

"""API Routes"""

@app.route('/api/cupcakes', methods=['GET'])
def get_cupcakes():
    """Return all cupcakes"""
    cupcakes = Cupcake.get_cupcakes()
    serialized_cupcakes = {'cupcakes': [Cupcake.serialize_cupcake(c) 
                                        for c in cupcakes]}
    
    return jsonify(serialized_cupcakes)


@app.route('/api/cupcakes', methods=['POST'])
def make_cupcake():
    print(request.json)
    data = {k:v for k,v in request.json.items()}

    cupcake = Cupcake.make_cupcake(data)
    serialized_cupcake = {'cupcake': Cupcake.serialize_cupcake(cupcake)}
    resp = jsonify(serialized_cupcake)
    
    return (resp, 201)
    

@app.route('/api/cupcakes/<cupcake_id>')
def get_cupcake(cupcake_id):
    """Get a single cupcake"""
    cupcake = Cupcake.get_cupcake(cupcake_id)
    
    if not cupcake:
        abort(404)
    else:
        serialized_cupcake = {'cupcake': Cupcake.serialize_cupcake(cupcake)}
        return jsonify(serialized_cupcake)


@app.route('/api/cupcakes/<cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    """Edit a cupcake"""
    cupcake = Cupcake.get_cupcake(cupcake_id)

    Cupcake.edit_cupcake(cupcake, request)
    
    serialized_cupcake = {'cupcake': Cupcake.serialize_cupcake(cupcake)}
    return jsonify(serialized_cupcake)


@app.route('/api/cupcakes/<cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """Delete a cupcake"""
    cupcake = Cupcake.get_cupcake(cupcake_id)
    
    if cupcake:
        Cupcake.delete_cupcake(cupcake_id)
        return jsonify({'message': 'Deleted'})
    else:
        abort(404)