#!/usr/bin/env python3
""" End-to-end integration test
"""
import requests

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """Testing the register user endpoint
    """
    payload = {"email": email, "password": password}
    res = requests.post("http://localhost:5000/users", data=payload)
    message = {"email": email, "message": "user created"}

    assert res.status_code == 200
    assert res.json() == message


def log_in_wrong_password(email: str, password: str) -> None:
    """ Testing the login end-point with wrong credentials
    """
    payload = {"email": email, "password": password}
    res = requests.post("http://localhost:5000/sessions", data=payload)
    assert res.status_code == 401


def log_in(email: str, password: str) -> str:
    """ Testing login end-point with correct credentials
    """
    payload = {"email": email, "password": password}
    res = requests.post("http://localhost:5000/sessions", data=payload)
    message = {"email": email, "message": "logged in"}

    assert res.status_code == 200
    assert res.json() == message

    session_id = res.cookies.get("session_id")
    return session_id


def profile_unlogged() -> None:
    """ Testing profile page with a user that is not logged in
    """
    res = requests.get("http://localhost:5000/profile")

    assert res.status_code == 403


def profile_logged(session_id: str) -> None:
    """ Testing the profile page with a logged in user
    """
    cookies = {"session_id": session_id}
    res = requests.get("http://localhost:5000/profile", cookies=cookies)
    message = {"email": EMAIL}

    assert res.status_code == 200
    assert res.json() == message


def log_out(session_id: str) -> None:
    """ Testing the logout end-point
    """
    cookies = {"session_id": session_id}
    res = requests.delete("http://localhost:5000/sessions", cookies=cookies)
    message = {"message": "Bienvenue"}

    assert res.status_code == 200
    assert res.json() == message


def reset_password_token(email: str) -> str:
    """ Testing the reset_password end-point
    """
    payload = {"email": email}
    res = requests.post("http://localhost:5000/reset_password", data=payload)
    reset_token = res.json().get("reset_token")
    message = {"email": email, "reset_token": reset_token}

    assert res.status_code == 200
    assert res.json() == message

    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Testing the update_password end-point
    """
    payload = {"email": email,
               "reset_token": reset_token,
               "new_password": new_password}
    res = requests.put("http://localhost:5000/reset_password", data=payload)
    message = {"email": email, "message": "Password updated"}

    assert res.status_code == 200
    assert res.json() == message


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
