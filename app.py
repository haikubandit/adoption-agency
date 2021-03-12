from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():
    """Render home page"""

    pets = Pet.query.all()

    return render_template("pets.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Renders add pet form (GET) or handles add pet form submission (POST)"""
    form = AddPetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age,
            notes=notes)

        db.session.add(new_pet)
        db.session.commit()
        
        flash(f"The {species} {name} has been added!")
        
        return redirect('/')
    else:
        return render_template("add_pet.html", form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def display_edit_pet(pet_id):
    """Renders add pet form (GET) or handles add pet form submission (POST)"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        
        flash(f"{pet.name} has been updated")
        
        return redirect(f"/{pet_id}")
    else:
        return render_template('pet_details_edit.html', form=form, pet=pet)
