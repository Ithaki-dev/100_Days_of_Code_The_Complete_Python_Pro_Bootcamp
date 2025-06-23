from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
import os
current_directory = os.path.dirname(os.path.abspath(__file__))

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(current_directory, 'instance/cafes.db')
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

def to_dict(self):
    return {
        "id": self.id,
        "name": self.name,
        "map_url": self.map_url,
        "img_url": self.img_url,
        "location": self.location,
        "seats": self.seats,
        "has_toilet": self.has_toilet,
        "has_wifi": self.has_wifi,
        "has_sockets": self.has_sockets,
        "can_take_calls": self.can_take_calls,
        "coffee_price": self.coffee_price,
    }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def random_cafe():
    cafe = Cafe.query.order_by(func.random()).first()
    return jsonify(cafe=to_dict(cafe))

@app.route("/all")
def all_cafes():
    cafes = Cafe.query.all()
    cafes_list = [to_dict(cafe) for cafe in cafes]
    return jsonify(cafes=cafes_list)

@app.route("/search")
def search_cafe():
    query_location = request.args.get("loc")
    cafe = Cafe.query.filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=to_dict(cafe))
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

# HTTP POST - Create Record
# Create a new cafe using form data
# This was tested using Postman with the following form data:
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=request.form.get("has_toilet") == "true",
        has_wifi=request.form.get("has_wifi") == "true",
        has_sockets=request.form.get("has_sockets") == "true",
        can_take_calls=request.form.get("can_take_calls") == "true",
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    if new_cafe:
        return jsonify(response={"success": "Successfully added the new cafe."}), 201
    else:
        return jsonify(error={"Not Found": "Sorry, we couldn't add the cafe."}), 404
    
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_cafe_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        new_price = request.form.get("coffee_price")
        if new_price:
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the coffee price."}), 200
        else:
            return jsonify(error={"Bad Request": "Please provide a new coffee price."}), 400
    else:
        return jsonify(error={"Not Found": "Cafe not found."}), 404
    
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed_cafe(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully reported the cafe as closed."}), 200
    else:
        return jsonify(error={"Not Found": "Cafe not found."}), 404


if __name__ == '__main__':
    app.run(debug=True)
