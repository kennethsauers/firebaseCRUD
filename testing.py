from firebaseCRUD import firebaseCRUD

if __name__ == "__main__":
    tempDataBase = "https://fir-python-9dae6.firebaseio.com/"
    tempPath = "/Testing"
    firebase = firebaseCRUD(tempDataBase)
    responce = firebase.write(tempPath, {"testing" : 1222})
    read = firebase.read(tempPath, responce["name"])
    firebase.update(tempPath + "/" + responce["name"], "testing", "updated")
    #firebase.delete(tempPath, responce["name"])
    #this will delete the whole path
    #firebase.delete(tempPath)
