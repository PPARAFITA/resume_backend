import pytest
from fastapi.testclient import TestClient
import sys
from src import main

client = TestClient(main.app_api)


def test_read_users(capsys):
    try:
        response = client.get("/users")
        print("Response JSON:", response.json())  # Usa response.json() para obtener el contenido JSON
        captured = capsys.readouterr()
        assert response.status_code == 200
        assert response.json() == [
            {
                "userid": 1,
                "nombre": "Priscila",
                "apellido": "Parafita",
                "email": "priscila.parafita56@gmail.com",
                "celular": 654591486,
                "nacionalidad": "Argentina",
                "ubicacion": "Barcelona"
            },
            {
                "userid": 2,
                "nombre": "Daniel",
                "apellido": "Fontana",
                "email": "daniel@gmail.com",
                "celular": 654591486,
                "nacionalidad": "Argentina",
                "ubicacion": "Barcelona"
            }
        ]
    except Exception as e:
        print("Error:", e)  # Imprime cualquier error que ocurra
        raise       

def test_read_one_user(capsys):
    try:
        response = client.get("/users/1")
        print("Response JSON:", response.json())  # Usa response.json() para obtener el contenido JSON
        captured = capsys.readouterr()
        assert response.status_code == 200
        assert response.json() == {
            "userid": 1,
            "nombre": "Priscila",
            "apellido": "Parafita",
            "email": "priscila.parafita56@gmail.com",
            "celular": 654591486,
            "nacionalidad": "Argentina",
            "ubicacion": "Barcelona"
        }
    except Exception as e:
        print("Error:", e)  # Imprime cualquier error que ocurra
        raise    

def test_post_new_user(capsys):
    try:
        new_user= {
            "nombre": "Tone",
            "apellido": "Parafita",
            "email": "tonebird@gmail.com",
            "celular": 123456789,
            "nacionalidad": "Argentina",
            "ubicacion": "Barcelona"
        }
        response = client.post("/users/",json=new_user)
        print("Response JSON:", response.json())  # Usa response.json() para obtener el contenido JSON
        captured = capsys.readouterr()
        assert response.status_code == 200
    except Exception as e:
        print("Error:", e)  # Imprime cualquier error que ocurra
        raise 