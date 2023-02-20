from API.Location.constants import ConstantLogin
import requests
import allure
import json


class TestAPI:
    @allure.description("login correctlly")
    def test_login_api(self):
        url = ConstantLogin.url_login
        data = ConstantLogin.valid_data
        res = requests.post(url, json=data)
        res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10

    @allure.description("login incorrect email")
    def test_login_api(self):
        url = ConstantLogin.url_login
        data = ConstantLogin.invalid_data_email
        res = requests.post(url, json=data)
        res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10

    @allure.description("signup correct email")
    def test_signup_api(self):
        url = ConstantLogin.url_signup
        data = ConstantLogin.correct_data
        res = requests.post(url, json=data)
        res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10