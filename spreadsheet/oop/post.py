class Post:
    def __init__(self,message,author):
        self.message = message
        self.author = author

    def get_post_info(self):
        print(f"Post: {self.message} written by  {self.author}")


# from  user import User
# app_user_one=User("nn@c.cn","nana","pwd1","devops")
# app_user_one.get_user_info()
#
# app_user_two = User("aa@aa.com","james","supersec" ,"Agent")
# app_user_two.get_user_info()
# import user
# app_user_one=user.User("nn@c.cn","nana","pwd1","devops")
# app_user_one.get_user_info()
#
# app_user_two = user.User("aa@aa.com","james","supersec" ,"Agent")
# app_user_two.get_user_info()

#reference