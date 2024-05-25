from fastapi import FastAPI # type: ignore
import uvicorn # type: ignore 

app= FastAPI()

@app.get("/")
def hello():
    return "Hello aneela nasir cut off "

@app.get("/getttodos")
def getTodos():
    print("Get Todos called")
    return "gettodos called Aneela "

@app.post("/getttodos")
def getTodosPost():
    print("post Todos called")
    return "post Todos called"

@app.put("/update")
def updated():
    return "aneela has been updated"


@app.get("/getSingleTodos")
def getSingleTodos():
    print("Get getSingleTodos called ")
    
 # function to start the server   
def start():
    uvicorn.run("todos.main:app",host="127.0.0.1", port=8080, reload=True)
    