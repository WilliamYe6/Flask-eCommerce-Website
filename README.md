# Flask eCommerce Sneaker Market

Author: William Ye  
Language: Python  
Version: 3.9.1  

# Introduction  

"Sneaker Central MTL" is an eCommerce Website allowing users to purchase and sell sneakers built using Python, Flask, HTML ,and CSS.  

# Implementation

This website was built using the Flask web framework allowing the creation of multiple endpoints. The implementation of these endpoints allowed users to register, login ,and purchase their desired shoes. Furthermore, to keep track of all information of each user, a relational model database was created using SQLite3 which stores all information about each user such as their passwords (encrypted), emails, and usernames. Finally, all of the backend implentation was accessible for each user through an interactive UI created with HTML, CSS, bootstrap ,and Jinja.

# How to Run

 __Requirements__ : Python 3.9.1

1) Create a virtual env and active it 
  
    * Mac OS/linux  
    $ python3 -m venv /path/to/new/virtual/environment  
    $ source env/bin/activate  
    
  
    * Windows  
    $ py -m venv env  
    $ .\env\Scripts\activate  
    
 
2) Install all dependencies 
  $ pip install -r requirements.txt

3) Host the website locally 
  $ python run.py


# Final Product Sample
![image](https://user-images.githubusercontent.com/74033578/121573763-993bc880-c9f3-11eb-87b4-c3919d49e450.png)  
*Login form UI*  



![image](https://user-images.githubusercontent.com/74033578/121573903-bcff0e80-c9f3-11eb-9b2f-e86aeca6325d.png)  
*Registration form UI*  



![image](https://user-images.githubusercontent.com/74033578/121574574-6514d780-c9f4-11eb-89ad-cfe0713739ff.png)  
*Sneaker purchase UI*  
