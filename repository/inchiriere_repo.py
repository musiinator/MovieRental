from termcolor import colored
import math
from domain.entities import *
from repository.clienti_repo import *
from repository.filme_repo import *
class InMemoryRepository_inchiriere:
    """
        Clasa creata cu responsabilitatea de a gestiona lista de inchirieri
    """
    def __init__(self):
        self._rentals = []
        self.__copyy = []
        self.__top3 = []
        self.__list = []
        self._client = InMemoryRepository_client_file('client.txt')
        self._film = InMemoryRepository_film_file('film.txt')

    def merge(self, arr1, arr2, key):
        result = []

        i = 0
        j = 0

        while i < len(arr1) and j < len(arr2):
            if key(arr1[i]) < key(arr2[j]):
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        result.extend(arr1[i:])
        result.extend(arr2[j:])

        return result

    def merge_sort_with_key(self, my_list, key=lambda x: x):
        list_length = len(my_list)

        if list_length <= 1:
            return my_list

        middle = list_length // 2

        left = my_list[:middle]
        right = my_list[middle:]

        sorted_left = self.merge_sort_with_key(left, key)
        sorted_right = self.merge_sort_with_key(right, key)

        return self.merge(sorted_left, sorted_right, key)

    def bingo_sort(self, my_list):
        maxVal = int(self.nr_of_movies_rented(my_list[0].get_Client()))
        minVal = int(self.nr_of_movies_rented(my_list[0].get_Client()))
        for i in range(1, len(my_list)):
            if int(self.nr_of_movies_rented(my_list[i].get_Client())) > maxVal:
                maxVal = int(self.nr_of_movies_rented(my_list[i].get_Client()))
            if self.nr_of_movies_rented(my_list[i].get_Client()) < minVal:
                minVal = int(self.nr_of_movies_rented(my_list[i].get_Client()))
        bingo = minVal
        next_avail = 1
        next_bingo = maxVal
        while bingo < maxVal:
            start = next_avail
            for i in range(start, len(my_list)):
                if int(self.nr_of_movies_rented(my_list[i].get_Client())) == bingo:
                    aux = int(self.nr_of_movies_rented(my_list[i].get_Client()))
                    my_list[i] = my_list[next_avail]
                    my_list[next_avail] = aux
                    next_avail = next_avail + 1
                elif int(self.nr_of_movies_rented(my_list[i].get_Client())) < next_bingo:
                    next_bingo = int(my_list[i])
            bingo = next_bingo
            next_bingo = maxVal
        return my_list


    def nr_of_movies_rented(self, client):
        """
        returneaza numarul de filme inchiriate de catre un client dat
        """
        nr = 0  #numara cate filme a inchiriat clientul 'client'
        for rent in self._rentals:
            if rent.get_Client() == client:
                nr = nr + 1
        return nr

    def nr_of_movies_rented2(self, film):
        """
        returneaza numarul de filme inchiriate din acelasi fel
        """
        nr = 0
        for rent in self._rentals:
            if rent.get_Film() == film:
                nr = nr + 1
        return nr

    def exists_with_id_inchiriere_repo(self, id):
        """
        Verifica daca exista o inchiriere cu id-ul dat in lista
        :param id: id-ul dat
        :type id: int
        :return: True daca exista inchiriere cu id dat, False altfel
        :rtype: bool
        """
        for rent in self._rentals:
            if rent.get_id() == id:
                return True
        return False

    def create_inchiriere(self, id_inchiriere, id_client, id_film):
        """
        Creaza inchirierea cu id-urile date
        """
        client = self._client.get_client_by_id(id_client)
        film = self._film.get_film_by_id(id_film)
        return Inchiriere(id_inchiriere, client, film)

    def store_inchiriere(self, inchiriere):
        """
        Adauga inchiriere in lista
        :param inchiriere:
        :return:
        """
        if self.exists_with_id_inchiriere_repo(inchiriere.get_id()):
            raise ValueError('Exista deja o inchiriere cu id-ul dat!')
        self._rentals.append(inchiriere)

    def ord_by_nume_client(self):
        """
        Ordoneaza lista de inchirieri in ordine alfabetica dupa numele clientilor
        """
        """for i in range (0, len(self._rentals) - 1):
            for j in range(i+1, len(self._rentals)):
                name1 = str(self._rentals[i].get_Client().get_nume())
                name2 = str(self._rentals[j].get_Client().get_nume())
                if name1 > name2:
                    self._rentals[i], self._rentals[j] = self._rentals[j], self._rentals[i]
        """
        """self._rentals = sorted(self._rentals, key = lambda x: x.get_Client().get_nume())"""
        self._rentals = self.merge_sort_with_key(self._rentals, key = lambda x: x.get_Client().get_nume())


    def ord_by_filme(self):
        """
        Ordoneaza lista de inchirieri in ordine descrescatoare dupa numarul de filme inchiriate de un client
        for i in range (0, len(self._rentals) - 1):
            for j in range(i+1, len(self._rentals)):
                client1 = self._rentals[i].get_Client()
                client2 = self._rentals[j].get_Client()
                if int(self.nr_of_movies_rented(client1)) < int(self.nr_of_movies_rented(client2)):
                    self._rentals[i], self._rentals[j] = self._rentals[j], self._rentals[i]
        """
        """self._rentals = sorted(self._rentals, key=lambda x: self.nr_of_movies_rented(x.get_Client()), reverse=True)"""
        self._rentals = self.bingo_sort(self._rentals)

    def ord_by_filme1(self):
        """
        Ordoneaza lista de inchirieri in ordine descrescatoare dupa numarul de filme inchiriate de un client
        """
        self.__copyy = self._rentals[:]
        for i in range (0, len(self.__copyy)-1):
            for j in range(i+1, len(self.__copyy)):
                client1 = self.__copyy[i].get_Client()
                client2 = self.__copyy[j].get_Client()
                if int(self.nr_of_movies_rented(client1)) < int(self.nr_of_movies_rented(client2)):
                    self.__copyy[i], self.__copyy[j] = self.__copyy[j], self.__copyy[i]

    def ord_by_filme2(self):
        """
        Ordoneaza lista de inchirieri in ordine descrescatoare dupa numarul de aparitii a unui film inchiriat
        """
        self.__copyy = self._rentals[:]
        for i in range (0, len(self.__copyy)-1):
            for j in range(i+1, len(self.__copyy)):
                film1 = self.__copyy[i].get_Film()
                film2 = self.__copyy[j].get_Film()
                if int(self.nr_of_movies_rented2(film1)) < int(self.nr_of_movies_rented2(film2)):
                    self.__copyy[i], self.__copyy[j] = self.__copyy[j], self.__copyy[i]

    def top3_rented_movies(self):
        """
        Returneaza o lista cu top3 cele mai inchiriate filme
        """
        self.ord_by_filme2()
        self.__list = self.__copyy[:]
        self.__top3.clear()
        if len(self.__list) < 3:
            raise ValueError('Nu exista suficiente inchirieri pt a se realiza un top 3!')
        cnt = 1
        for i in range(1, len(self.__list)):
            if self.__list[i - 1].get_Film() != self.__list[i].get_Film():
                cnt = cnt + 1
        if cnt >= 3:
            self.__top3.append(self.__list[0])
            self.__top3.append(self.__list[0])
            self.__top3.append(self.__list[0])
            i = 1
            for j in range(0, len(self.__list)):
                if i < 3:
                    if self.__top3[i - 1].get_Film() != self.__list[j].get_Film():
                        self.__top3[i] = self.__list[j]
                        i = i + 1
                else:
                    break
            return self.__top3[:]
        else:
            raise ValueError('Nu exista suficiente filme diferite pt a se realiza un top 3!')

    def top3_rented_clients(self):
        """
        Returneaza o lista cu top3 clienti cu cele mai multe filme inchiriate
        """
        self.ord_by_filme1()
        self.__list = self.__copyy[:]
        self.__top3.clear()
        if len(self.__list) < 3:
            raise ValueError('Nu exista suficiente inchirieri pt a se realiza un top 3!')
        cnt = 1
        for i in range(1, len(self.__list)):
            if self.__list[i-1].get_Client() != self.__list[i].get_Client():
                cnt = cnt + 1
        if cnt >= 3:
            self.__top3.append(self.__list[0])
            self.__top3.append(self.__list[0])
            self.__top3.append(self.__list[0])
            i = 1
            for j in range(0, len(self.__list)):
                if i < 3:
                    if self.__top3[i-1].get_Client() != self.__list[j].get_Client():
                        self.__top3[i] = self.__list[j]
                        i = i + 1
                else:
                    break
            return self.__top3[:]
        else:
            raise ValueError('Nu exista suficienti clienti diferiti pt a se realiza un top 3!')

    def top_30_la_suta(self):
        """
        Returneaza o lista cu primii 30% clienti cu cele mai multe filme inchiriate
        """
        self.ord_by_filme1()
        self.__list = self.__copyy[:]
        self.__top3.clear()
        if len(self.__list) == 0:
            raise ValueError('Nu exista destule inchirieri pt a se afisa primii 30% clienti!')
        cnt = 1
        for i in range(1, len(self.__list)):
            if self.__list[i-1].get_Client() != self.__list[i].get_Client():
                cnt = cnt + 1
        if cnt <= 3:
            #pentru un numar mai mic sau egal de 3 clienti se va afisa unul singur
            nr_of_clients = 1
        else:
            nr_of_clients = int(math.trunc(0.3*cnt))
        aux = nr_of_clients
        while aux > 0:
            self.__top3.append(self.__list[0])
            aux = aux - 1
        i = 1
        for j in range(0, len(self.__list)):
            if i < nr_of_clients:
                if self.__top3[i - 1].get_Client() != self.__list[j].get_Client():
                    self.__top3[i] = self.__list[j]
                    i = i + 1
            else:
                break
        return self.__top3[:]


    def get_all_rentals(self):
        """
        Returneaza o lista cu toate inchirierile
        :rtype: list of rents objects
        """
        return self._rentals[:]

def test_store_inchiriere():
    """
    Verifica daca functia 'store_inchiriere' functioneaza corespunzator
    """
    test_list = InMemoryRepository_inchiriere[0]
    film = Film(1, 'Batman', 'descriere', 'gen')
    client = Client(1, 'Alin', 1234567890123)
    inchiriere = Inchiriere(1, client, film)
    test_list.store_inchiriere(inchiriere)
    assert len(test_list) == 1
    assert test_list[0] == inchiriere

#test_store_inchiriere()


class InMemoryRepository_inchiriere_file(InMemoryRepository_inchiriere):

    def __init__(self, file_path):
        self.__file_path = file_path
        InMemoryRepository_inchiriere.__init__(self)

    def __read_from_file(self):
        with open(self.__file_path, "r") as f:
            self._rentals = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    x = line.split(",")
                    id = int(x[0])
                    id_client = int(x[1])
                    id_film = int(x[2])
                    inchiriere = InMemoryRepository_inchiriere.create_inchiriere(self, id, id_client, id_film)
                    self._rentals.append(inchiriere)
            return self._rentals

    def __append_to_file(self, rent):
        with open(self.__file_path, "a") as f:
            f.write(str(rent.get_id()) + "," + str(rent.get_Client().get_id()) + "," +
                    str(rent.get_Film().get_id()) + '\n')

    def __write_to_file(self):
        with open(self.__file_path, "w") as f:
            for rent in self._rentals:
                f.write(str(rent.get_id()) + "," + str(rent.get_Client().get_id()) + "," +
                        str(rent.get_Film().get_id()) + '\n')

    def nr_of_movies_rented(self, client):
        self.__read_from_file()
        InMemoryRepository_inchiriere.nr_of_movies_rented(self, client)
        self.__write_to_file()
        return InMemoryRepository_inchiriere.nr_of_movies_rented(self, client)

    def nr_of_movies_rented2(self, film):
        self.__read_from_file()
        InMemoryRepository_inchiriere.nr_of_movies_rented2(self, film)
        self.__write_to_file()
        return InMemoryRepository_inchiriere.nr_of_movies_rented2(self, film)

    def exists_with_id_inchiriere_repo(self, id):
        self.__read_from_file()
        InMemoryRepository_inchiriere.exists_with_id_inchiriere_repo(self, id)
        self.__write_to_file()
        return InMemoryRepository_inchiriere.exists_with_id_inchiriere_repo(self, id)

    def create_inchiriere(self, id_inchiriere, id_client, id_film):
        self.__read_from_file()
        InMemoryRepository_inchiriere.create_inchiriere(self, id_inchiriere, id_client, id_film)
        self.__write_to_file()
        return InMemoryRepository_inchiriere.create_inchiriere(self, id_inchiriere, id_client, id_film)

    def store_inchiriere(self, inchiriere):
        self.__read_from_file()
        InMemoryRepository_inchiriere.store_inchiriere(self, inchiriere)
        self.__append_to_file(inchiriere)

    def ord_by_nume_client(self):
        self.__read_from_file()
        InMemoryRepository_inchiriere.ord_by_nume_client(self)
        self.__write_to_file()

    def ord_by_filme(self):
        self.__read_from_file()
        InMemoryRepository_inchiriere.ord_by_filme(self)
        self.__write_to_file()

    def ord_by_filme1(self):
        self.__read_from_file()
        InMemoryRepository_inchiriere.ord_by_filme1(self)
        self.__write_to_file()

    def ord_by_filme2(self):
        self.__read_from_file()
        InMemoryRepository_inchiriere.ord_by_filme2(self)
        self.__write_to_file()

    def top3_rented_movies(self):
        self.__read_from_file()
        InMemoryRepository_inchiriere.top3_rented_movies(self)
        self.__write_to_file()
        return InMemoryRepository_inchiriere.top3_rented_movies(self)

    def top3_rented_clients(self):
        self.__read_from_file()
        InMemoryRepository_inchiriere.top3_rented_clients(self)
        self.__write_to_file()
        return InMemoryRepository_inchiriere.top3_rented_clients(self)

    def top_30_la_suta(self):
        self.__read_from_file()
        InMemoryRepository_inchiriere.top_30_la_suta(self)
        self.__write_to_file()
        return InMemoryRepository_inchiriere.top_30_la_suta(self)

    def get_all_rentals(self):
        self.__read_from_file()
        InMemoryRepository_inchiriere.get_all_rentals(self)
        self.__write_to_file()
        return InMemoryRepository_inchiriere.get_all_rentals(self)
