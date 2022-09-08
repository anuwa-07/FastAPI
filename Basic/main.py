

from fastapi import FastAPI

# make app
app = FastAPI()


@app.get("/")
async def root():
    return {"nessage": "Hello World!"}


# with path params
@app.get("/items/{item_id}")
async def read_time(item_id: int):
    return {
        "item_id": item_id
    }


# Query Parameters.
'''
    When you declare other function parameters that are not part of the path parameters, 
    they are automatically interpreted as "query" parameters.
'''
@app.get("/myinfo/")
async def read_info(age: int, email: str):
    return {
        "Info": f"My age is: {age} and email: {email}"
    }



# Optional parameters
''' Here even we do not need to tell FastAPI to home_name is a path parameter, FastAPI knows it :) '''
@app.get("/home/{home_id}")
async def find_home(home_id: int, home_name: str | None = None):
    if home_name:
        return {"home_id": home_id, "home_name": home_name}
    return {"home_id": home_id}



# Query parameter type conversion
''' 
    Here we set default value to "home_name", 
    also we define default value for "short", Right ??? 
        No! it is not what you think, it is a type conversion in FastAPI, we can't assign default values like that, 
        Because if we didn't provide that value, it take that assing data type's Type. 
'''
@app.get("/homepage/{home_id}")
async def get_home(home_id: int, home_name: str | None = None, short: bool = False):
    home = {"id": home_id}
    if home_name:
        home.update({"name": home_name})
    if not short:
        home.update({
            "description": "This is a very simple home!"
        })
    # 
    return home



# Multiple path and query parameters
'''
    You can declare multiple path parameters and query parameters at the same time,
    FastAPI knows which is which. And you don't have to declare them in any specific order.
    They will be detected by name
'''
@app.get("/users/{user_id}/items/{item_id}/")
async def get_user_info(
    user_id: int, item_id: str, user_email: str, user_phone: str | None = None, is_married: bool = False
):
    user_item = {
        "user_id": user_id,
        "item_id": item_id,
        "email": email,
    }
    if user_phone is not None:
        user_item.update({"phone": user_phone})
    
    if not is_married:
        user_item.update({"married": is_married})
    # 
    return user_item






