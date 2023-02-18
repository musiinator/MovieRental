from domain.entities import Film

class InMemoryRepository_film:
    """
        Clasa creata cu responsabilitatea de a gestiona lista de filme
    """

    def __init__(self):
        self._films = []

    def exists_with_id_film_repo(self, id):
        """
        Verifica daca exista un film cu id-ul dat in lista
        :param id: id-ul dat
        :type id: int
        :return: True daca exista film cu id dat, False altfel
        :rtype: bool
        """
        for film in self._films:
            if film.get_id() == id:
                return True
        return False

    def store_film(self, film):
        """
        Adauga film in lista
        :param film: filmul de adaugat
        :type film: Film
        :return: -; lista de filme se modifica prin adaugarea filmului
        :rtype: -; filmul este adaugat
        :raises:ValueError daca exista deja un film cu id-ul dat
        """
        # verificare sa nu existe atlet duplicat
        if self.exists_with_id_film_repo(film.get_id()):
            raise ValueError('Exista deja un film cu id-ul dat!')
        self._films.append(film)

    def del_by_id_film(self, id):
        """
        Sterge film din lista dupa id
        :return:

        """
        if self._films == []:
            raise ValueError('Nu se poate efectua stergerea deoarece lista de filme este goala!')
        if type(id) == int:
            if id < 0:
                raise ValueError('Id invalid!')
        if not (self.exists_with_id_film_repo(id)):
            raise ValueError('Nu exista film cu id-ul dat!')
        poz = 0
        for el in self._films:
            if el.get_id() == id:
                poz = self._films.index(el)
        self._films.remove(self._films[poz])

    def get_film_by_id(self, id):
        """
        Afiseaza film dupa id
        :param id: id-ul filmului
        :return:
        """
        if self._films == []:
            raise ValueError('Nu se poate efectua gasirea deoarece lista de filme este goala!')
        if type(id) == int:
            if id < 0:
                raise ValueError('Id invalid!')
        else: raise ValueError('Id invalid!')
        if not (self.exists_with_id_film_repo(id)):
            raise ValueError('Nu exista film cu id-ul dat!')
        for el in self._films:
            if el.get_id() == id:
                return el

    def update_titlu_by_id(self, id, titlu_nou):
        """
        :param id: id-ul filmului
        :return:filmul cu numele modificat
        """
        if self._films == []:
            raise ValueError('Nu se poate efectua gasirea deoarece lista de filme este goala!')
        if type(id) == int:
            if id < 0:
                raise ValueError('Id invalid!')
        if not (self.exists_with_id_film_repo(id)):
            raise ValueError('Nu exista film cu id-ul dat!')
        el = 0
        for el in self._films:
            if el.get_id() == id:
                break
        el.set_titlu(titlu_nou)
        return el

    def update_descriere_by_id(self, id, descriere_noua):
        """
        :param id: id-ul filmului
        :return:filmul cu descrierea modificata
        """
        if self._films == []:
            raise ValueError('Nu se poate efectua gasirea deoarece lista de filme este goala!')
        if type(id) == int:
            if id < 0:
                raise ValueError('Id invalid!')
        if not (self.exists_with_id_film_repo(id)):
            raise ValueError('Nu exista film cu id-ul dat!')
        el = 0
        for el in self._films:
            if el.get_id() == id:
                break
        el.set_descriere(descriere_noua)
        return el

    def update_gen_by_id(self, id, gen_nou):
        """
        :param id: id-ul filmului
        :return:filmul cu genul modificata
        """
        if self._films == []:
            raise ValueError('Nu se poate efectua gasirea deoarece lista de filme este goala!')
        if type(id) == int:
            if id < 0:
                raise ValueError('Id invalid!')
        if not (self.exists_with_id_film_repo(id)):
            raise ValueError('Nu exista film cu id-ul dat!')
        el = 0
        for el in self._films:
            if el.get_id() == id:
                break
        el.set_gen(gen_nou)
        return el

    def get_all_films(self):
        """
        Returneaza o lista cu toate filmele disponibile
        :rtype: list of film objects
        """
        return self._films[:]

def test_store():
    """
    Verifica daca functia 'store' functioneaza corespunzator
    :return:
    """
    lst = InMemoryRepository_film()
    film1 = Film(1, 'Batman', 'After training with his mentor, Batman begins his fight to free crime-ridden \
Gotham City from corruption.', 'adventure')
    lst.store_film(film1)
    assert (len(lst.get_all_films()) == 1)
    assert (lst.get_all_films()[0] == film1)

def test_del_by_id():
    """
    Verifica daca functia 'del_by_id' functioneaza corespunzator
    :return:
    """
    lst = InMemoryRepository_film()
    film1 = Film(1, 'Batman', 'After training with his mentor, Batman begins his fight to free crime-ridden \
    Gotham City from corruption.', 'adventure')
    film2 = Film(2, 'Venom', 'Eddie Brock attempts to reignite his career by interviewing serial killer Cletus Kasady, \
    who becomes the host of the symbiote Carnage and escapes prison after a failed execution.', 'action')
    lst.store_film(film1)
    lst.store_film(film2)
    lst.del_by_id_film(1)
    assert (len(lst.get_all_films()) == 1)
    assert (lst.get_all_films()[0] == film2)

def test_get_all_films():
    """
    Verifica daca functia 'get_all_films' functioneaza corespunzator
    :return:
    """
    lst = InMemoryRepository_film()
    film1 = Film(1, 'Batman', 'After training with his mentor, Batman begins his fight to free crime-ridden \
Gotham City from corruption.', 'adventure')
    film2 = Film(2, 'Venom', 'Eddie Brock attempts to reignite his career by interviewing serial killer Cletus Kasady, \
who becomes the host of the symbiote Carnage and escapes prison after a failed execution.', 'action')
    lst.store_film(film1)
    assert (type(lst.get_all_films()) == list)
    assert (len(lst.get_all_films()) == 1)

    lst.store_film(film2)
    assert (len(lst.get_all_films()) == 2)
    assert (lst.get_all_films()[0] == film1)
    assert (lst.get_all_films()[1] == film2)

    lst.del_by_id_film(2)
    assert (len(lst.get_all_films()) == 1)
    assert (lst.get_all_films()[0] == film1)

test_store()
test_del_by_id()
test_get_all_films()


class InMemoryRepository_film_file(InMemoryRepository_film):

    def __init__(self, file_path):
        InMemoryRepository_film.__init__(self)
        self.__file_path = file_path

    def _read_from_file(self):
        with open(self.__file_path, "r") as f:
            self._films = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    x = line.split(",")
                    id = int(x[0])
                    titlu = str(x[1])
                    descriere = str(x[2])
                    gen = str(x[3])
                    film = Film(id, titlu, descriere, gen)
                    self._films.append(film)
            return self._films

    def __append_to_file(self, film):
        with open(self.__file_path, "a") as f:
            f.write(str(film.get_id()) + "," + str(film.get_titlu()) + "," +
                    str(film.get_descriere()) + "," + str(film.get_gen()) + '\n')

    def __write_to_file(self):
        with open(self.__file_path, "w") as f:
            for film in self._films:
                f.write(str(film.get_id()) + "," + str(film.get_titlu()) + "," +
                        str(film.get_descriere()) + "," + str(film.get_gen()) + '\n')

    def exists_with_id_film_repo(self, id):
        self._read_from_file()
        InMemoryRepository_film.exists_with_id_film_repo(self, id)
        self.__write_to_file()
        return InMemoryRepository_film.exists_with_id_film_repo(self, id)

    def store_film(self, film):
        self._read_from_file()
        InMemoryRepository_film.store_film(self, film)
        self.__append_to_file(film)

    def del_by_id_film(self, id):
        self._read_from_file()
        InMemoryRepository_film.del_by_id_film(self, id)
        self.__write_to_file()

    def get_film_by_id(self, id):
        self._read_from_file()
        return InMemoryRepository_film.get_film_by_id(self, id)

    def update_titlu_by_id(self, id, titlu_nou):
        self._read_from_file()
        InMemoryRepository_film.update_titlu_by_id(self, id, titlu_nou)
        self.__write_to_file()
        return InMemoryRepository_film.update_titlu_by_id(self, id, titlu_nou)

    def update_descriere_by_id(self, id, descriere_noua):
        self._read_from_file()
        InMemoryRepository_film.update_descriere_by_id(self, id, descriere_noua)
        self.__write_to_file()
        return InMemoryRepository_film.update_descriere_by_id(self, id, descriere_noua)

    def update_gen_by_id(self, id, gen_nou):
        self._read_from_file()
        InMemoryRepository_film.update_gen_by_id(self, id, gen_nou)
        self.__write_to_file()
        return InMemoryRepository_film.update_gen_by_id(self, id, gen_nou)

    def get_all_films(self):
        return self._read_from_file()

