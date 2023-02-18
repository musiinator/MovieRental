from domain.entities import Film
from exceptions.exceptions import ValidationException, ClientNotFoundException
from domain.validators import film_validator
from repository.filme_repo import InMemoryRepository_film, InMemoryRepository_film_file

class service_films:

    def __init__(self, repo, val):
        self.__repo_film = repo
        self.__validator_film = val

    def exists_with_id_film(self, id):
        """
        Verifica daca exista film cu id-ul dat
        :param id: id-ul filmului
        :return: val = True/False
        """
        return self.__repo_film.exists_with_id_film_repo(id)

    def add_film(self, id, titlu, descriere, gen):
        """
        Adaugare film

        :param id:
        :param titlu:
        :param descriere:
        :param gen:
        :return:
        """
        movie = Film(id, titlu, descriere, gen)
        self.__validator_film.validate_film(movie)
        self.__repo_film.store_film(movie)
        return movie

    def del_films(self, id):
        """

        :param id: id-ul dupa care se va sterge filmul
        :return:
        """
        self.__repo_film.del_by_id_film(id)

    def get_film_by_id(self, id):
        """
        Gaseste film dupa id
        :param id: id-ul dupa care se va cauta filmul
        :return:
        """
        film = self.__repo_film.get_film_by_id(id)
        return film

    def update_titlu_film(self, id, titlu_nou):
        """
        Modifica informatiile despre un film dat dupa id
        :return:noul film cu numele modificat
        """
        film_nou = self.__repo_film.update_titlu_by_id(id, titlu_nou)
        return film_nou

    def update_descriere_film(self, id, descriere_noua):
        """
        Modifica informatiile despre un film dat dupa id
        :return:noul film cu descrierea modificata
        """
        film_nou = self.__repo_film.update_descriere_by_id(id, descriere_noua)
        return film_nou

    def update_gen_film(self, id, gen_nou):
        """
        Modifica informatiile despre un film dat dupa id
        :return:noul film cu genul modificat
        """
        film_nou = self.__repo_film.update_gen_by_id(id, gen_nou)
        return film_nou

    def get_all_films(self):
        """
        Returneaza o lista cu toate filmele
        :return: lista de filme
        :rtype: list of films objects
        """
        return self.__repo_film.get_all_films()

def test_add_film():
    """
    Verifica daca functia 'add_film' functioneaza corespunzator
    :return:
    """
    repo = InMemoryRepository_film()
    validator = film_validator()
    test_srv = service_films(repo, validator)

    added_film = test_srv.add_film(1, 'Venom', 'Eddie Brock attempts to reignite his career by interviewing serial \
killer Cletus Kasady, who becomes the host of the symbiote Carnage and escapes prison after a failed execution.',
'action')
    assert (added_film.get_titlu() == 'Venom')
    assert (len(test_srv.get_all_films()) == 1)

    try:
        added_film = test_srv.add_film(1, 'Batman', 'fsas', 'fsdfs')
        assert False
    except ValueError:
        ValidationException(ValueError)
        assert True

def test_del_films():
    """
    Verifica daca functia 'del_films' functioneaza corespunzator
    :return:
    """
    repo = InMemoryRepository_film()
    validator = film_validator()
    test_srv = service_films(repo, validator)

    test_srv.add_film(1, 'Eternals', 'Eternals is a 2021 American epic superhero film based on the Marvel Comics race \
of the same name.', 'action')
    test_srv.add_film(2, 'The Godfather', 'The Godfather is a 1972 American crime film directed by Francis Ford Coppola, \
who co-wrote the screenplay with Mario Puzo, based on Puzo s best-selling 1969 novel of the same name.', 'drama')
    test_srv.del_films(1)
    assert (len(test_srv.get_all_films()) == 1)
    assert test_srv.get_all_films()[0].get_id() == 2
    try:
        test_srv.del_films(-5)
        assert False
    except ValueError:
        ValidationException(ValueError)
        assert True

def test_update_titlu_film():
    """
    Verifica daca functia 'update_titlu_film' functioneaza corespunzator
    :return:
    """
    repo = InMemoryRepository_film()
    validator = film_validator()
    test_srv = service_films(repo, validator)

    film = test_srv.add_film(1, 'Eternals', 'Eternals is a 2021 American epic superhero film based on the Marvel Comics race \
of the same name.', 'action')
    test_srv.update_titlu_film(1, 'Star Wars')
    assert film.get_titlu() == 'Star Wars'

def test_update_descriere_film():
    """
    Verifica daca functia 'update_descriere_film' functioneaza corespunzator
    :return:
    """
    repo = InMemoryRepository_film()
    validator = film_validator()
    test_srv = service_films(repo, validator)

    film = test_srv.add_film(1, 'Eternals', 'Eternals is a 2021 American epic superhero film based on the Marvel Comics race \
of the same name.', 'action')
    test_srv.update_descriere_film(1, 'descriere_test')
    assert film.get_descriere() == 'descriere_test'

def test_update_gen_film():
    """
    Verifica daca functia 'update_gen_film' functioneaza corespunzator
    :return:
    """
    repo = InMemoryRepository_film()
    validator = film_validator()
    test_srv = service_films(repo, validator)

    film = test_srv.add_film(1, 'Eternals', 'Eternals is a 2021 American epic superhero film based on the Marvel Comics race \
of the same name.', 'action')
    test_srv.update_gen_film(1, 'gen_test')
    assert film.get_gen() == 'gen_test'

def test_get_film_by_id():
    """
    Verifica daca functia 'get_film_by_id' functioneaza corespunzator
    :return:
    """
    repo = InMemoryRepository_film()
    validator = film_validator()
    test_srv = service_films(repo, validator)

    film1 = test_srv.add_film(1, 'Venom', 'Eddie Brock attempts to reignite his career by interviewing serial killer Cletus Kasady, \
who becomes the host of the symbiote Carnage and escapes prison after a failed execution.', 'action')
    film2 = test_srv.add_film(2, 'The Godfather', 'The Godfather is a 1972 American crime film directed by Francis Ford Coppola, \
who co-wrote the screenplay with Mario Puzo, based on Puzo s best-selling 1969 novel of the same name.', 'drama')
    assert test_srv.get_film_by_id(1) == film1
    assert test_srv.get_film_by_id(2) == film2
    try:
        test_srv.get_film_by_id('m')
        assert False
    except ValueError:
        ValidationException(ValueError)
        assert True

def test_get_all_films():
    """
        Verifica daca functia 'get_all_clients' functioneaza corespunzator
        :return:
    """
    repo = InMemoryRepository_film()
    validator = film_validator()
    test_srv = service_films(repo, validator)

    film1 = test_srv.add_film(1, 'Batman', 'After training with his mentor, Batman begins his fight to free crime-ridden \
Gotham City from corruption.', 'adventure')
    film2 = test_srv.add_film(2, 'Venom', 'Eddie Brock attempts to reignite his career by interviewing serial killer Cletus Kasady, \
who becomes the host of the symbiote Carnage and escapes prison after a failed execution.', 'action')
    assert (len(test_srv.get_all_films()) == 2)
    assert test_srv.get_all_films()[0] == film1
    assert test_srv.get_all_films()[1] == film2
    test_srv.del_films(1)
    assert test_srv.get_all_films()[0] == film2

test_add_film()
test_del_films()
test_update_titlu_film()
test_update_descriere_film()
test_update_gen_film()
test_get_film_by_id()
test_get_all_films()