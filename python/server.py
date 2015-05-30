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
notes_collection = bq['notes']


@app.route('/')
def home():
    notes = notes_collection.find()
    return render_template('home.html', notes=notes)


@app.route('/note', methods=['POST'])
def new_note():
    title = request.form['title']
    description = request.form['description']
    doc = {
        'title': title,
        'description': description,
        'tags': []
    }
    notes_collection.save(doc)
    return redirect(url_for('home'))


@app.route('/note/<note_id>/delete', methods=['GET'])
def delete_note(note_id):
    notes_collection.remove_one_by_id(note_id)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
