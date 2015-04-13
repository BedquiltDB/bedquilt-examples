from flask import Flask, render_template, redirect, url_for, request
import pybedquilt


# Create a flask app
app = Flask(__name__)

# Get a BedquiltClient instance
# You will need to create a postgres database called bedquilt_example first:
#     CREATE DATABASE bedquilt_example;
# Then, enable the bedquilt extension on the database:
#     CREATE EXTENSION IF NOT EXISTS pgcrypto;
#     CREATE EXTENSION bedquilt;
# See the getting-started guide here: http://bedquiltdb.readthedocs.org
bq = pybedquilt.BedquiltClient("dbname=bedquilt_example")
items_collection = bq['items']


@app.route('/')
def home():

    items = items_collection.find()

    return render_template('home.html', items=items)


@app.route('/item', methods=['POST'])
def new_item():
    description = request.form['description']
    doc = {
        'description': description,
        'done': False
    }
    items_collection.save(doc)
    return redirect(url_for('home'))


@app.route('/item/<item_id>/delete', methods=['POST'])
def delete_item(item_id):
    items_collection.remove_one_by_id(item_id)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
