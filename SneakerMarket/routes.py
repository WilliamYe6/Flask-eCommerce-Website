from SneakerMarket import app
from flask import render_template, redirect, url_for, flash, request 
from SneakerMarket.models import Sneaker, User
from SneakerMarket.form import RegistrationForm, LoginForm, PurchaseSneaker, SellSneaker
from SneakerMarket import db
from flask_login import login_user, logout_user, login_required, current_user

#Home page endpoint
@app.route('/')
@app.route('/home')
def homePage():
    return render_template('home.html') 
    
#Sneaker market endpoint
@app.route('/sneakers', methods = ['GET', 'POST']) 
@login_required
def sneakers():
    purchase_form = PurchaseSneaker() #created instance of PurchaseSneaker()
    sell_form = SellSneaker()  #created instance of SellSneaker()

    if request.method == 'POST':
        #purchasing sneaker logic
        purchased_sneaker = request.form.get('purchased_sneaker')
        p_sneaker_obj = Sneaker.query.filter_by(name = purchased_sneaker).first() #created an instance of the class Sneaker
        if p_sneaker_obj:
            if current_user.check_price(p_sneaker_obj):
                if p_sneaker_obj.buy(current_user):
                    flash(f'Congradulation! You have purchased the {p_sneaker_obj.name} for {p_sneaker_obj.price}')
            else:
                flash (f"You do not have enough funds to purchase the {p_sneaker_obj.name}", category = 'danger')
            return redirect(url_for('sneakers'))

        #selling sneaker logic 
        sold_sneaker = request.form.get ('sold_sneaker')
        s_sneaker_obj = Sneaker.query.filter_by(name  = sold_sneaker).first()
        if s_sneaker_obj:
            if current_user.check_sell(s_sneaker_obj):
                s_sneaker_obj.sell(current_user)
                flash(f'Congradulation! You have sold the {s_sneaker_obj.name} for {s_sneaker_obj.price} $', category = "success")
            else:
                flash(f'Unfortunately, {current_user.name} is unable to sell {s_sneaker_obj}.', category = "danger")
        return redirect(url_for('sneakers'))

    if request.method == "GET":
        sneakers = Sneaker.query.filter_by(owner = None)
        owned_sneakers = Sneaker.query.filter_by(owner = current_user.id)
        #displays HTML template to the user
        return render_template('sneaker.html', sneakers = sneakers, purchase_form = purchase_form, owned_sneakers = owned_sneakers, sell_form = sell_form)

#Registration endpoint 
@app.route('/register', methods = ['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit(): #once user clicks register it will create a new User inside the database 
        user_to_create = User(username = form.username.data, email = form.email_address.data, password = form.password.data)
        db.session.add(user_to_create)
        db.session.commit()

        login_user(user_to_create)
        flash(f'Account created succesfully! You are logged in as {user_to_create.username}', category="success")
        return redirect(url_for('sneakers')) #returns the user to the sneaker market URL after registration 

    if form.errors != {}: #if there are not errors from validations
        for error in form.errors.values():
            flash (f'There was an error with creating user: {error}', category = 'danger')
    return render_template('registration.html', form = form)

#Login endpoint 
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm() #creates instance of the LoginForm()
    #checks if the user entered correct information
    if form.validate():
        attempted_user = User.query.filter_by(username = form.username.data).first()
        #succesful login logic
        if attempted_user and attempted_user.check_password(attempted_password = form.password.data):
            login_user(attempted_user)
            flash(f'Success! {attempted_user.username} has logged in!', category = 'success')
            return redirect(url_for('sneakers'))
        #unsuccesful login logic
        else:
            flash(f'Username or Password is incorrect. Please try again', category = 'danger')
    return render_template('login.html', form = form)
#Logout endpoint
@app.route('/logout')
def logout():
    logout_user()
    flash(f'You have been logged out!', category = 'info')
    return redirect(url_for('homePage')) #returns user to the homepage

@app.route('/upcomingDrops')
@login_required
def upcomingDrops():
    return render_template('upcomingDrops.html')



