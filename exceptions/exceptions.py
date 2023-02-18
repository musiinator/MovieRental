class ClientException(Exception):
    pass


class ValidationException(ClientException):
    def __init__(self, msgs):
        """
        :param msgs: lista de mesaje de eroare
        :type msgs: msgs
        """
        self.__err_msgs = msgs

    def getMessages(self):
        return self.__err_msgs

    def __str__(self):
        return 'Validation Exception: ' + str(self.__err_msgs)


class RepositoryException(ClientException):
    def __init__(self, msg):
        self.__msg = msg

    def getMessage(self):
        return self.__msg

    def __str__(self):
        return 'Repository Exception: ' + str(self.__msg)


class DuplicateIDException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "ID duplicat.")


'''class ScoreAlreadyAssignedException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Scor existent deja pentru atlet si categorie.")'''


class ClientNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Atletul nu a fost gasit.")


class ScoreNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Scorul nu a fost gasit.")


class CategoryNotFoundException(RepositoryException):
    def __init__(self):
        RepositoryException.__init__(self, "Categoria nu a fost gasita.")


class NotEnoughScoresException(ClientException):
    def __init__(self):
        pass

class CorruptedFileException(ClientException):
    def __init__(self):
        pass
