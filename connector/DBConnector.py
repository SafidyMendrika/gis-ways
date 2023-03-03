import psycopg2

class DBConnector:
    def __init__(self):
        pass

    def connect(self):
        con = psycopg2.connect(
            host = "localhost",
            database = "lalana",
            user = "postgres",
            password = "azerty"
        )

        return con