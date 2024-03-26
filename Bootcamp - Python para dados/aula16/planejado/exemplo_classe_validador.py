from datetime import datetime
import re

class Venda:
    def __init__(self, id, produto, valor, quantidade, data, email_do_comprador):
        self.id = id
        self.produto = produto
        self.valor = self.validar_valor(valor)
        self.quantidade = self.validar_quantidade(quantidade)
        self.data = data
        self.email_do_comprador = self.validar_email(email_do_comprador)

    def __repr__(self):
        return f"Venda(id={self.id}, produto={self.produto}, valor={self.valor}, quantidade={self.quantidade}, data={self.data}, email_do_comprador={self.email_do_comprador})"

    def validar_valor(self, valor):
        if valor <= 0:
            raise ValueError("O valor deve ser positivo.")
        return valor

    def validar_quantidade(self, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser positiva.")
        return quantidade

    def validar_email(self, email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Email inválido.")
        return email
