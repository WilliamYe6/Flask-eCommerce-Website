from SneakerMarket import db, login_manager
from SneakerMarket import bcrypt
from flask_login import UserMixin # this import helps prevent writing necessary functions when users login 

#function needed for user login to function in a Flask WebFrame 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Class to store all users onto a table inside the db sqlite3
class User(db.Model, UserMixin):
    #attributes to help give properties to each User
    id = db.Column(db.Integer(), primary_key = True)
    username= db.Column(db.String(length = 25), nullable = False, unique = True)
    email = db.Column(db.String(length = 30), nullable = False, unique = True)
    password_encrypt = db.Column(db.String(length = 60), nullable = False)
    balance = db.Column(db.Integer(), nullable = False, default = 1000)
    sneakers = db.relationship('Sneaker', backref = 'owned_sneaker', lazy = True)

    #method that allows to show the balance available for each user
    @property
    def optimized_balance(self):
        if len(str(self.balance)) >= 4:
            return f'{str(self.balance)[:-3]}, {str(self.balance)[-3:]}$'
        else:
            return f"{self.balance}$"
    #method that returns the users password
    @property
    def password(self):
        return self.password
    #method that encrypts the users password when stored in database
    @password.setter
    def password(self, plain_password):
        self.password_encrypt = bcrypt.generate_password_hash(plain_password).decode('utf-8')
    #method that checks if passwords match
    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_encrypt, attempted_password)
    #method that indicates if the user is capable of purchasing a product
    def check_price(self, item_obj):
        return self.balance >= item_obj.price
    #method that sells the sneakers for users
    def check_sell(self, item_obj):
        return item_obj in self.sneakers

#Class to store all sneakers models onto a table inside the db sqlite3
class Sneaker(db.Model):

    #attributes to create properties for each Sneaker
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length=30), nullable = False )
    size = db.Column(db.String(length=30), nullable = False)
    price = db.Column(db.Integer(), nullable = False)
    description = db.Column(db.String(length = 1024), nullable = False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    
    #Allows the sneakers added on the database to be identified by their name
    def __repr__(self):
        return f'Sneaker{self.name}'
    # Method that updates user balance and ownership
    def buy(self, user):
        self.owner = user.id
        user.balance -=self.price
        if user.balance < 0:
            user.balance = 0
    # Method that updates user balance and ownership
    def sell(self, user):
        self.owner = None
        user.balance += self.price
        db.session.commit() 
   
