# import function from other program
from website import createApp 

# app is the function from __init__.py
app = createApp() 

# make sure that the app is only ran with this file
if __name__ == '__main__': 
    # run server
    app.run(debug=True) 