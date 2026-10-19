from fastapi import FastAPI

app = FastAPI()


# /users?name=Ice ---> after question mark, name is key and its value is handled by Query Parameter
# /products?price=1000 ---> after question mark, price is key and its value is handled by Query Parameter

@app.get("/users")
# def get_users(name):
# 	return {"Name":name} # to display name, give url /users?name=Ice

# in above case if name parameter isnot gives then it will give error, so error is not handled

def get_users(name: str=None):
	return {"Name":name} # if parameter is not given then null is given
#in above case optional value was given not default 


#in below case a default value is given, which is changed if ?limit=20 is given
@app.get("/products")
def get_products(limit: int = 10):
	return {"limit":limit}
#In this case only one query parameter was handled

#In below case multiple queries is handled
@app.get("/items")
def get_items(name: str=None, price: int=0):
	return{
		"name":name,
		"price":price
	}