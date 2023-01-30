# import function from other program
from website import create_app 

# app is the function from __init__.py
app = create_app() 

# make sure that the app is only ran with this file
if __name__ == '__main__': 
    # run server
    app.run(debug=True) 