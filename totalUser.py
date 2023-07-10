import requests

def getTotalUser():
    # url = "http://52.79.144.104:8080/api/v1/users/total"
    url = "http://localhost:8080/api/v1/users/total"
    userList = requests.get(url)

    # print(userList.json());
    return userList.json().get('data')