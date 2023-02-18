from domain.entities import Client

class InMemoryRepository_client:
    """
        Clasa creata cu responsabilitatea de a gestiona lista de clienti
    """

    def __init__(self):
        self._clients = []

    def exists_with_id_client_repo_rec(self, id, poz):
        """
                Verifica recursiv daca exista un client cu id-ul dat in lista
                :param id: id-ul dat
                :type id: int
                :return: True daca exista client cu id dat, False altfel
                :rtype: bool
        """
        if poz == len(self._clients):
            return [False, 0]
        elif self._clients[poz].get_id() == id:
            return [True, self._clients[poz]]
        else:
            return self.exists_with_id_client_repo_rec(id, poz+1)

    def exists_with_id_client_repo(self, id):
        """
        Verifica daca exista un client cu id-ul dat in lista
        :param id: id-ul dat
        :type id: int
        :return: True daca exista client cu id dat, False altfel
        :rtype: bool


        Studiu complexitate:
        caz favorabil: primul element este cel dorit, cautat => T(n) = 1 apartine teta(1)
        caz defavorabil: ultimul element este cel dorit, cautat => T(n) = n apartine teta(n)
        caz mediu: se pot parcurge 1,2,3,...,n-1,n pasi, avand aceeasi probabilitate de 1/n
                   deci T(n) = (1+2+3+...+(n-1)+n)/n = (n+1)/2 apartine teta(n)
        => complexitate: O(n)


        for client in self._clients:
            if client.get_id() == id:
                return True
        return False

        """
        lst = self.exists_with_id_client_repo_rec(id, 0)
        if lst[0]:
            return lst[1]


    def store_client_rec(self, client, poz):
        """
        Adauga client in lista in mod recursiv
        :param client: clientul de adaugat
        :type client: Client
        :return: -; lista de clienti se modifica prin adaugarea clientului
        :rtype: -; clientul este adaugat
        :raises:ValueError daca exista deja un clientul in lista
        """

        if poz == len(self._clients):
            return False
        elif self._clients[poz] == client:
            return True
        else:
            return self.store_client_rec(client, poz+1)


    def store_client(self, client):
        """
        Adauga client in lista
        :param client: clientul de adaugat
        :type client: Client
        :return: -; lista de clienti se modifica prin adaugarea clientului
        :rtype: -; clientul este adaugat
        :raises:ValueError daca exista deja un clientul in lista
        if self.exists_with_id_client_repo(client.get_id()):
            raise ValueError('Exista deja un client cu id-ul dat!')
        self._clients.append(client)

        """

        exist_in_list = self.store_client_rec(client, 0)
        if exist_in_list == False:
            self._clients.append(client)

    def del_by_id_client(self, id):
        """
        Sterge client din lista dupa id
        :return:

        """
        if self._clients == []:
            raise ValueError('Nu se poate efectua stergerea deoarece lista de clienti este goala!')
        if type(id) == int:
            if id < 0:
                raise ValueError('Id invalid!')
        if not (self.exists_with_id_client_repo(id)):
            raise ValueError('Nu exista client cu id-ul dat!')
        poz = 0
        for el in self._clients:
            if el.get_id() == id:
                poz = self._clients.index(el)
        self._clients.remove(self._clients[poz])

    def get_client_by_id(self, id):
        """
        Afiseaza client dupa id
        :param id: id-ul clientului
        :return:
        """
        if self._clients == []:
            raise ValueError('Nu se poate efectua gasirea deoarece lista de clienti este goala!')
        if type(id) == int:
            if id < 0:
                raise ValueError('Id invalid!')
        if not (self.exists_with_id_client_repo(id)):
            raise ValueError('Nu exista client cu id-ul dat!')
        for el in self._clients:
            if el.get_id() == id:
                return el

    def update_nume_by_id(self, id, nume_nou):
        """
        :param id: id-ul clientului
        :return:clientul cu numele modificat
        """
        if self._clients == []:
            raise ValueError('Nu se poate efectua gasirea deoarece lista de clienti este goala!')
        if type(id) == int:
            if id < 0:
                raise ValueError('Id invalid!')
        if not (self.exists_with_id_client_repo(id)):
            raise ValueError('Nu exista client cu id-ul dat!')
        el = 0
        for el in self._clients:
            if el.get_id() == id:
                break
        el.set_nume(nume_nou)
        return el

    def update_cnp_by_id(self, id, cnp_nou):
        """
        :param id: id-ul clientului
        :return:clientul cu cnp-ul modificat
        """
        if self._clients == []:
            raise ValueError('Nu se poate efectua gasirea deoarece lista de clienti este goala!')
        if type(id) == int:
            if id < 0:
                raise ValueError('Id invalid!')
        if not (self.exists_with_id_client_repo(id)):
            raise ValueError('Nu exista client cu id-ul dat!')
        el = 0
        for el in self._clients:
            if el.get_id() == id:
                break
        el.set_cnp(cnp_nou)
        return el

    def get_all_clients(self):
        """
        Returneaza o lista cu toti clientii
        :rtype: list of film objects
        """
        return self._clients[:]

def test_store():
    """
    Verifica daca functia 'store' functioneaza corespunzator
    :return:
    """
    lst = InMemoryRepository_client()
    client1 = Client(1, 'Radu Suciu', 5020909260065)
    lst.store_client(client1)
    assert (len(lst.get_all_clients()) == 1)
    assert (lst.get_all_clients()[0] == client1)

def test_del_by_id():
    """
    Verifica daca functia 'del_by_id' functioneaza corespunzator
    :return:
    """
    lst = InMemoryRepository_client()
    client1 = Client(1, 'Radu Suciu', 5020909260065)
    client2 = Client(2, 'Vlad Suciu', 5141107265194)
    lst.store_client(client1)
    lst.store_client(client2)
    lst.del_by_id_client(1)
    assert (len(lst.get_all_clients()) == 1)
    assert (lst.get_all_clients()[0] == client2)

def test_get_all_clients():
    """
    Verifica daca functia 'get_all_clients' functioneaza corespunzator
    :return:
    """
    lst = InMemoryRepository_client()
    client1 = Client(1, 'Radu Suciu', 5020909260065)
    lst.store_client(client1)
    assert (type(lst.get_all_clients()) == list)
    assert (len(lst.get_all_clients()) == 1)
    assert (lst.get_all_clients()[0] == client1)

    client2 = Client(2, 'Vlad Suciu', 5141107265194)
    lst.store_client(client2)
    assert (len(lst.get_all_clients()) == 2)
    assert (lst.get_all_clients()[1] == client2)

test_store()
test_del_by_id()
test_get_all_clients()

class InMemoryRepository_client_file(InMemoryRepository_client):

    def __init__(self, file_path):
        InMemoryRepository_client.__init__(self)
        self.__file_path = file_path

    def _read_from_file(self):
        with open(self.__file_path, "r") as f:
            self._clients = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    x = line.split(",")
                    id = int(x[0])
                    nume = str(x[1])
                    cnp = int(x[2])
                    client = Client(id, nume, cnp)
                    self._clients.append(client)
            return self._clients

    def __append_to_file(self, client):
        with open(self.__file_path, "a") as f:
            f.write(str(client.get_id()) + "," + str(client.get_nume()) + "," +
                    str(client.get_cnp()) + '\n')

    def __write_to_file(self):
        with open(self.__file_path, "w") as f:
            for client in self._clients:
                f.write(str(client.get_id()) + "," + str(client.get_nume()) + "," +
                        str(client.get_cnp()) + '\n')

    def exists_with_id_client_repo(self, id):
        self._read_from_file()
        InMemoryRepository_client.exists_with_id_client_repo(self, id)
        self.__write_to_file()
        return InMemoryRepository_client.exists_with_id_client_repo(self, id)

    def store_client(self, client):
        self._read_from_file()
        InMemoryRepository_client.store_client(self, client)
        self.__append_to_file(client)

    def del_by_id_client(self, id):
        self._read_from_file()
        InMemoryRepository_client.del_by_id_client(self, id)
        self.__write_to_file()

    def get_client_by_id(self, id):
        self._read_from_file()
        InMemoryRepository_client.get_client_by_id(self, id)
        self.__write_to_file()
        return InMemoryRepository_client.get_client_by_id(self, id)

    def update_nume_by_id(self, id, nume_nou):
        self._read_from_file()
        InMemoryRepository_client.update_nume_by_id(self, id, nume_nou)
        self.__write_to_file()
        return InMemoryRepository_client.update_nume_by_id(self, id, nume_nou)

    def update_cnp_by_id(self, id, cnp_nou):
        self._read_from_file()
        InMemoryRepository_client.update_cnp_by_id(self, id, cnp_nou)
        self.__write_to_file()
        return InMemoryRepository_client.update_cnp_by_id(self, id, cnp_nou)

    def get_all_clients(self):
        return self._read_from_file()
