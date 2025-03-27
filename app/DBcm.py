import mariadb


class DBConnectionError(Exception):
    pass


class CredentialsError(Exception):
    pass


class SQLError(Exception):
    pass


class UseDatabase:
    def __init__(self, config: dict) -> None:
        self.configuration = config
        self.conn = None
        self.cursor = None

    def __enter__(self) -> 'cursor':
        try:
            self.conn = mariadb.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mariadb.InterfaceError as err:
            raise DBConnectionError(err) from err
        except mariadb.ProgrammingError as err:
            raise CredentialsError(err) from err

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        # Add any extra exception-handling-code AFTER doing the __exit__ things
        if exc_type is mariadb.ProgrammingError:
            raise SQLError(exc_value)
