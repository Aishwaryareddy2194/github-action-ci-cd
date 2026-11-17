def login(username, password):
    if username == "admin" and password == "1234":
        return "Welcome! Login successful"
    else:
        return "Sorry! Invalid username or password"


if __name__ == "__main__":
    print(login("admin", "1234"))
    print(login("user", "wrong"))
