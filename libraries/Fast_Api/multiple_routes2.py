from fastapi import FastAPI

app = FastAPI()

#Home Route
@app.get("/")
def home():
	return {"message":"Welcome to FastAPI"}

#About route
@app.get("/about")
def about():
	return {"message":"This is About Page"}

#Users route
@app.get("/users")
def users():
	return {
		"users":["ice","fire","water"]
	}
