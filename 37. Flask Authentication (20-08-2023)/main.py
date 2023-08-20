from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user



app = Flask(__name__)

app.config['SECRET_KEY'] = 'my-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

# LOGIN
login_manager = LoginManager()
login_manager.init_app(app)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
#db.create_all()

'''try: 
    new_user = User(
        email = "sokka",
        password = "bokka",
        name = "dokka"
    )
    db.session.add(new_user)
    db.session.commit()
except:
    print("some issue")'''

@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)
                                        # checking if the user is already logged in


@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "POST":
        
        if User.query.filter_by(email=request.form.get('email')).first():
            #User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))
        
        username = request.form['name']
        user_email = request.form['email']
        user_password = generate_password_hash(password=request.form['password'],method="pbkdf2:sha256",salt_length=8)
        try:
            new_user = User(name=username,email=user_email,password=user_password)
            db.session.add(new_user)
            db.session.commit()
        except:
            print("Possible integrity issue")
        return render_template('secrets.html',name=username)
    return render_template("register.html")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        
        #Find user by email entered.
        user = User.query.filter_by(email=email).first()
        
        #Check stored password hash against entered password hashed.
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets'))
                
           
    return render_template("login.html",logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required #for all pages where being logged in is required
def secrets():
    print(current_user.name)
    return render_template("secrets.html",name=current_user.name,logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download', methods=["GET","POST"])
@login_required
def download():
    return send_from_directory('static', filename="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
