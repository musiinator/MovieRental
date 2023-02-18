from domain.entities import Inchiriere
from domain.validators import inchiriere_validator
from service.clienti_service import service_clients
from service.filme_service import service_films

class service_inchiriere():

    def __init__(self, repo, val, clienti, filme):
        self.__repo_inchiriere = repo
        self.__validator_inchiriere = val
        self.__srv_clienti = clienti
        self.__srv_filme = filme

    def exists_with_id_inchiriere(self, id):
        """
        Verifica daca exista film cu id-ul dat
        :param id: id-ul filmului
        :return: val = True/False
        """
        return self.__repo_inchiriere.exists_with_id_inchiriere_repo(id)

    def add_inchiriere(self, id_inchiriere, id_client, id_film):
        """

        :param id_inchiriere:
        :param id_client:
        :param id_film:
        :return:
        """
        self.__validator_inchiriere.validate_id_inchiriere(id_inchiriere)
        inchiriere = self.__repo_inchiriere.create_inchiriere(id_inchiriere, id_client, id_film)
        self.__repo_inchiriere.store_inchiriere(inchiriere)
        return inchiriere

    def sort_inchiriere_by_nume_client(self):
        """
        Returneaza lista cu toate inchirierile ordonata dupa numele clientilor
        """
        self.__repo_inchiriere.ord_by_nume_client()

    def sort_inchiriere_by_nr_of_films(self):
        """
        Returneaza lista cu toate inchirierile ordonata dupa numarul de filme inchiriate
        """
        self.__repo_inchiriere.ord_by_filme()

    def get_top3_movies(self):
        """
        Returneaza o lista cu top 3 filme cele mai inchiriate
        """
        return self.__repo_inchiriere.top3_rented_movies()

    def get_top3_clients(self):
        """
        Returneaza o lista cu top 3 clienti cu cele mai multe filme inchiriate
        """
        return self.__repo_inchiriere.top3_rented_clients()

    def get_top30_la_suta(self):
        """
        Returneaza o lista cu primii 30% clienti cu cele mai multe filme inchiriate
        """
        return self.__repo_inchiriere.top_30_la_suta()

    def nr_of_movies_film(self, film):
        """
        Returneaza nr de filme inchiriate dintr-un film dat
        """
        return self.__repo_inchiriere.nr_of_movies_rented2(film)

    def nr_of_movies_client(self, client):
        """
        Returneaza nr de filme inchiriate de catre un client dat
        """
        return self.__repo_inchiriere.nr_of_movies_rented(client)

    def get_all_rentals(self):
        """
        Returneaza o lista cu toate inchirierile
        :return: lista de inchirieri
        :rtype: list of rents objects
        """
        return self.__repo_inchiriere.get_all_rentals()