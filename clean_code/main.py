from fastapi import FastAPI, Request

app = FastAPI()
users = []
counter = 1

@app.post("/user")

async def create_user(req: Request):

    global counter
    # Stores data from json
    data = await req.json()
    name = data["n"]
    email = data["e"]

    for u in users:
        if u["e"] == email:
            return {"error": "taken"}

    new_user = {"id": counter, "n": name, "e": email}
    counter += 1
    users.append(new_user) # Adds user to the list
    return new_user

@app.get("/users")
def get_all():
    return users