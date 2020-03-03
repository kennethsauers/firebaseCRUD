from firebase import firebase


class firebaseCRUD():
    def __init__(self, firebaseDataBase = None):
        self.firebaseDataBase = firebaseDataBase
        self.firebase = firebase.FirebaseApplication(firebaseDataBase, None)

    def write(self, path = "temp", data = {}, verbose = True):
        result = self.firebase.post(path,data)
        if verbose:
            print(result)
        return result

    def read(self, path = "temp", value = "", verbose = True):
        result = self.firebase.get(path, value)
        if verbose:
            print(result)
        return result

    def update(self, path = "temp", index = "", value = "", verbose = True):
        result = self.firebase.put(path, index, value)
        if verbose:
            print("updateing: {} to {}".format(index, result))
        return True

    def delete(self, path = "temp", table = "", verbose = True):
        self.firebase.delete(path, table)
        if verbose:
            print("deleteing {}".format(table))
        return True
