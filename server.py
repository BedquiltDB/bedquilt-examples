from flask import Flask, render_template
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


@app.route("/")
def home():

    items_coll = bq['items']
    items = items_coll.find()

    return render_template('home.html', items=items)


if __name__ == "__main__":
    app.run(debug=True)
