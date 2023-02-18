from domain.entities import Client
from exceptions.exceptions import ValidationException, ClientNotFoundException
from domain.validators import client_validator
from repository.clienti_repo import InMemoryRepository_client

class service_clients:

    def __init__(self, repo, val):
        self.__repo_client = repo
        self.__validator_client = val

    def exists_with_id_client(self, id):
        """
        Verifica daca exista client cu id-ul dat
        :param id: id-ul clientului
        :return: val = True/False
        """
        return self.__repo_client.exists_with_id_client_repo(id)

    def add_client(self, id, nume, cnp):
        """
        Adaugare client

        :param id: id-ul clientului
        :param nume: numele clientului
        :param cnp: cnp-ul clientului
        :return: clientul creat
        """
        client = Client(id, nume, cnp)
        self.__validator_client.validate_client(client)
        self.__repo_client.store_client(client)
        return client

    def del_clients(self, id):
        """
        Sterge client dupa id
        :param id: id-ul dupa care se va sterge clientul
        :return:
        """
        self.__repo_client.del_by_id_client(id)

    def get_client_by_id(self, id):
        """
        Gaseste client dupa id
        :param id: id-ul dupa care se va cauta clientul
        :return:
        """
        client = self.__repo_client.get_client_by_id(id)
        return client

    def update_nume_client(self, id, nume_nou):
        """
        Modifica informatiile despre un client dat dupa id
        :return:noul client cu numele modificat
        """
        client_nou = self.__repo_client.update_nume_by_id(id, nume_nou)
        return client_nou

    def update_cnp_client(self, id, cnp_nou):
        """
        Modifica informatiile despre un client dat dupa id
        :return:noul client cu cnp-ul modificat
        """
        client = self.__repo_client.get_client_by_id(id)
        client_nou = self.__repo_client.update_cnp_by_id(id, cnp_nou)
        return client_nou

    def get_all_clients(self):
        """
        Returneaza o lista cu toti clientii
        :return: lista de clienti
        :rtype: list of clients objects
        """
        return self.__repo_client.get_all_clients()

def test_add_client():
    """
    Verifica daca functia 'add_client' functioneaza corespunzator
    :return:
    """
    repo = InMemoryRepository_client()
    validator = client_validator()
    test_srv = service_clients(repo, validator)

    added_client = test_srv.add_client(1, 'Radu Suciu', 5020909260065)
    assert (added_client.get_nume() == 'Radu Suciu')
    assert (len(test_srv.get_all_clients()) == 1)

    try:
        added_client = test_srv.add_client(1, 'Rafael Nadal', 'a')
        assert False
    except Exception:
        ValidationException(ValueError)
        assert True

def test_del_clients():
    """
    Verifica daca functia 'del_clients' functioneaza corespunzator
    :return:
    """
    repo = InMemoryRepository_client()
    validator = client_validator()
    test_srv = service_clients(repo, validator)

    test_srv.add_client(1, 'Radu Suciu', 5020909260065)
    test_srv.add_client(2, 'Vlad Suciu', 5141107265194)
    test_srv.del_clients(1)
    assert (len(test_srv.get_all_clients()) == 1)
    assert test_srv.get_all_clients()[0].get_id() == 2
    try:
        test_srv.del_clients(-5)
        assert False
    except ValueError:
        ValidationException(ValueError)
        assert True

def test_get_client_by_id():
    """
    Verifica daca functia 'get_client_by_id' functioneaza corespunzator
    :return:
    """
    repo = InMemoryRepository_client()
    validator = client_validator()
    test_srv = service_clients(repo, validator)

    client1 = test_srv.add_client(1, 'Radu Suciu', 5020909260065)
    client2 = test_srv.add_client(2, 'Vlad Suciu', 5141107265194)
    assert test_srv.get_client_by_id(1) == client1
    assert test_srv.get_client_by_id(2) == client2
    try:
        test_srv.get_client_by_id(-5)
        assert False
    except ValueError:
        ValidationException(ValueError)
        assert True

def test_get_all_clients():
    """
    Verifica daca functia 'get_all_clients' functioneaza corespunzator
    :return:
    """
    repo = InMemoryRepository_client()
    validator = client_validator()
    test_srv = service_clients(repo, validator)

    client1 = test_srv.add_client(1, 'Radu Suciu', 5020909260065)
    client2 = test_srv.add_client(2, 'Vlad Suciu', 5141107265194)
    assert (len(test_srv.get_all_clients()) == 2)
    assert test_srv.get_all_clients()[0] == client1
    assert test_srv.get_all_clients()[1] == client2
    test_srv.del_clients(1)
    assert test_srv.get_all_clients()[0] == client2

def test_update_nume_client():
    """
        Verifica daca functia 'update_nume_client' functioneaza corespunzator
        :return:
        """
    repo = InMemoryRepository_client()
    validator = client_validator()
    test_srv = service_clients(repo, validator)

    client1 = test_srv.add_client(1, 'Radu Suciu', 5020909260065)
    test_srv.update_nume_client(1, 'Mircea Suciu')
    assert client1.get_nume() == 'Mircea Suciu'

def test_update_cnp_client():
    """
        Verifica daca functia 'update_cnp_client' functioneaza corespunzator
        :return:
    """
    repo = InMemoryRepository_client()
    validator = client_validator()
    test_srv = service_clients(repo, validator)

    client1 = test_srv.add_client(1, 'Radu Suciu', 5020909260065)
    test_srv.update_cnp_client(1, 1234567890123)
    assert client1.get_cnp() == 1234567890123

test_add_client()
test_del_clients()
test_update_nume_client()
test_update_cnp_client()
test_get_client_by_id()
test_get_all_clients()
