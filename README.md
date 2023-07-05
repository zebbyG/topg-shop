# UNDER_CONSTRUCTION
A project under construction.
==================================
Top Gz is an online shoe shop that offers a wide range of high-quality footwear for customers.
- Technologies used:
    - Python-Django
    - HTML
    - Bootstrap css
    - Javascript
## To run the project on your machine:
+ [X] `git clone https://github.com/zebbyG/UNDER_CONSTRUCTION`

Then Create a virtual environment
+ [X] `python3 -m venv topg`
     
    - The name of the virtual environment here will be `topg`

Activate the virtual environment
+ [X] `source topg/bin/activate`

Once the v-env is activated,:
+ [X] (topg1) will be visible at the very start of the path on your terminal
    
    - Install the following:
        
        - `pip install Django` - Required for any django project
        - `python3 -m pip install django-debug-toolbar` - Required for the debug toolbar to work.
        - `python3 -m pip install Pillow` - Required for all image fields in the project

After everything above has installed successfully, navigate to the main directory and start server:
+ [X]  `cd TOP\ Gz\ SHOE\ SHOP/`


+ [X] `python3 manage.py runserver`

    - The server runs on port 8000 by default. If you want to specify the port number:
        - `python3 manage.py runserver [port number]`