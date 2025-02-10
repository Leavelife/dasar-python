
class Users:
    userId = 10
    __secure = True
    
    def __init__(self, username, email):
        self.__username = username
        self.__email = email
        self.userId += 1
    def info(self):
        print("\nUsername: ", self.__username)
        print("Email: ", self.__email)
        print("Secure: ", self.__secure)
        
        
class Mahasiswa(Users): 
    def __init__(self, nim, username, email, password):
        super().__init__(username, email)
        self.__nim = nim
        self.__username = username
    def info(self):
        super().info()
        print("\nNim mahasiswa: ", super().userId + self.__nim)
        print("Nama mahasiswa: ", self.__username)


mahasiswa = Mahasiswa(20201, "saya", "saya@gmail.com", "qweqwe")
mahasiswa.info()