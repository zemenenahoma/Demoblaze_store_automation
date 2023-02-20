class ConstantLogin:
    url_login = "https://api.demoblaze.com/login"
    valid_data = {"username": "zemeneabinet06@gmail.com", "password": "bm0xODI1NTE="}
    invalid_data_email = {"username": "zemeneabinet06mail.com", "password": "bm0xODI1NTE="}
    invalid_password = {"username": "zemeneabinet06mail.com", "password": "bm0xODI1NT"}
    empty_user_email = {"username": "", "password": "bm0xODI1NTE="}
    empty_password = {"username": "zemeneabinet06mail.com", "password": ""}
    ###########################################################################
    url_signup = "https://api.demoblaze.com/signup"
    correct_data = {"username": "zemeneabinet06@gmail.com;l", "password": "bm0xODI1NTE="}
