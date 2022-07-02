from app import * 
class Client(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self) -> str:
        client_stringfy = f'{self.id},{self.nome},{self.email}'
        return client_stringfy

    def json(self):
        client = {
            "id": self.id,
            "nome":self.nome,
            "email":self.email
        }
        return client