def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        print("Inicializando uma nova instância da conexão com o banco de dados.")

# Testando o padrão Singleton
if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    print(f"db1 é db2? {'Sim' if db1 is db2 else 'Não'}")
