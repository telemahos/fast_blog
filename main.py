from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': 'My Name is kostas'}

@app.get('/about')
def about():
    return {'data': 'This is the about Page'}

