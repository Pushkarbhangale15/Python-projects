class User:
    pass
    def __init__(self,id,username):
        print("New object being created....")
        self.id=id
        self.username=username
        self.followers=0
        self.following=0
    def follow(self,user):
        user.followers+=1
        self.following+=1



user_1=User("001","Pushkar")
user_2=User("002","Love")

user_1.follow(user_2)
print(user_1.followers,user_1.following,user_2.followers,user_2.following)