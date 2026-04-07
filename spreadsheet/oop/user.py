class User:
    def __init__(self,user_email,name,password,current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self,new_password):
        self.password = new_password

    def change_job_title(self,new_job_title):
        self.current_job_title = new_job_title
        # do smth
    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them  at {self.email}")


# app_user_one=User("nn@c.cn","nana","pwd1","devops")
# app_user_one.get_user_info()
#
# app_user_two = User("aa@aa.com","james","supersec" ,"Agent")
# app_user_two.get_user_info()

#
# "/home/evan/data/github/python/devops /.venv/spreadsheet/bin/python" /home/evan/data/github/python/spreadsheet/user.py
# User nana currently works as a devops. You can contact them  at nn@c.cn
# User james currently works as a Agent. You can contact them  at aa@aa.com
