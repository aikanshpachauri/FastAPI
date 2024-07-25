from fastapi import FastAPI

api = FastAPI()

@api.get("/{id}")
def base_function(id : int):
    return {"Data" : "Hello " + str(id)} 