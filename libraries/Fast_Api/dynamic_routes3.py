from fastapi import FastAPI

app = FastAPI()

#Users Route
@app.get("/users/{user_id}") #route is changing automatically so dynamic routes
def get_user(user_id:int): #if abc is given then error, since abc is integer
	return {"user_id":user_id}


