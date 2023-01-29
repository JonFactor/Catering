# starts website
### create app
## get create app function
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug = True)