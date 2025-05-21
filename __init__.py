from cryptography.fernet import Fernet
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/encrypt/<key>/<valeur>')
def encrypt_with_key(key, valeur):
    try:
        f = Fernet(key.encode())
        valeur_bytes = valeur.encode()
        token = f.encrypt(valeur_bytes)
        return f"Valeur encryptée avec clé perso : {token.decode()}"
    except Exception as e:
        return f"Erreur lors de l'encryptage : {str(e)}"

@app.route('/decrypt/<key>/<token>')
def decrypt_with_key(key, token):
    try:
        f = Fernet(key.encode())
        valeur_decryptee = f.decrypt(token.encode())
        return f"Valeur décryptée : {valeur_decryptee.decode()}"
    except Exception as e:
        return f"Erreur lors du décryptage : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
