from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    

if not inspect(db.engine).has_table('book'):
    db.create_all()
    
    
def to_dict(self):
        #Method 1. 
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
    

@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record

@app.route("/random") # methods=["GET"] is included by default in all routes
def get_random():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=to_dict(random_cafe))


@app.route("/all")
def get_all():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[to_dict(cafe) for cafe in cafes])


@app.route("/search")
def search():
    my_loc = request.args.get('loc') # this is the ?loc= part
    cafes = db.session.query(Cafe).filter_by(location=my_loc).all()
    if cafes:
        return jsonify(cafes=[to_dict(cafe) for cafe in cafes])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    all_cafes = db.session.query(Cafe).all()
    for x in range(1, len(all_cafes)):
        if all_cafes[x-1].name == all_cafes[x].name:
            cafe_to_delete = Cafe.query.get(all_cafes[x].id)
            db.session.delete(cafe_to_delete)
            db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record
# PUT substitutes the whole tinh
# PATCH updates only one piece of data
# this part of the project was completed on Postman

## HTTP DELETE - Delete Record
@app.route("/delete", methods=["POST","GET"])
def delete():
    if request.method == "POST":
        all_cafes = db.session.query(Cafe).all()
        cafe_name_to_delete = request.form.get('cafe_name')
        print(f"Checking cafe: {cafe_name_to_delete}")
        for cafe in all_cafes:
            if cafe.name == cafe_name_to_delete:
                db.session.delete(cafe)
                db.session.commit()
                all_cafes = db.session.query(Cafe).all()
    all_cafes = db.session.query(Cafe).all()
    return render_template('delete.html', cafes=all_cafes)
    

if __name__ == '__main__':
    app.run(debug=True)
