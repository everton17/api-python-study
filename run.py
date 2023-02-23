from app import create_app
#from waitress import serve #- WSGI server for windows

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #serve(app, listen='*:5000', threads=4) #Serve API with Waitress on Windows