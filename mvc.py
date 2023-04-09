class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

class UserView:
    def show_user(self, user):
        print(f"Name: {user.get_name()}")
        print(f"Email: {user.get_email()}")

class UserController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_user_name(self, name):
        self.model.name = name

    def set_user_email(self, email):
        self.model.email = email

    def set_user_password(self, password):
        self.model.password = password

    def update_view(self):
        self.view.show_user(self.model)

# Tạo một đối tượng User
user = User("John Doe", "john.doe@example.com", "password123")

# Tạo một đối tượng UserView
view = UserView()

# Tạo một đối tượng UserController và kết nối Model và View
controller = UserController(user, view)

# Hiển thị thông tin người dùng
controller.update_view()
