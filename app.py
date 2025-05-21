from flask import Flask
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, CryptoPython !'

@app.route('/generate_key')
def generate_key():
    return Fernet.generate_key().decode()

@app.route('/encrypt/<key>/<text>')
def encrypt_with_key(key, text):
    try:
        fernet = Fernet(key.encode())
        encrypted = fernet.encrypt(text.encode())
        return encrypted
    except Exception as e:
        return f"Erreur chiffrement : {e}"

@app.route('/decrypt/<key>/<encrypted_text>')
def decrypt_with_key(key, encrypted_text):
    try:
        fernet = Fernet(key.encode())
        decrypted = fernet.decrypt(encrypted_text.encode())
        return decrypted.decode()
    except Exception as e:
        return f"Erreur déchiffrement : {e}"
