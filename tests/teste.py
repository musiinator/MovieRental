from service.clienti_service import *
from service.filme_service import *
from repository.clienti_repo import *
from repository.filme_repo import *
from service.inchiriere_service import *
from repository.inchiriere_repo import *
import unittest

#clienti
class TesteCase(unittest.TestCase):

    def setUp(self):
        file_path_client = "clienti.txt"
        file_path_film = "filme.txt"
        file_path_inchiriere = "inchiriere.txt"
        with open(file_path_client, "w") as f:
            f.write("")
        self.repo_client = InMemoryRepository_client_file(file_path_client)
        self.valid_client = client_validator()
        self.srv_client = service_clients(self.repo_client, self.valid_client)
        with open(file_path_film, "w") as g:
            g.write("")
        self.repo_film = InMemoryRepository_film_file(file_path_film)
        self.valid_film = film_validator()
        self.srv_film = service_films(self.repo_film, self.valid_film)
        with open(file_path_inchiriere, "w") as h:
            h.write("")
        self.repo_inchiriere = InMemoryRepository_inchiriere_file(file_path_inchiriere)
        self.valid_inchiriere = inchiriere_validator()
        self.srv_inchiriere = service_inchiriere(self.repo_inchiriere, self.valid_inchiriere, self.repo_client, self.repo_film)

    def test_store(self):
        """
        Verifica daca functia 'store' functioneaza corespunzator
        :return:
        """
        lst = InMemoryRepository_client()
        client1 = Client(1, 'Radu Suciu', 5020909260065)
        lst.store_client(client1)
        self.assertTrue(len(lst.get_all_clients()) == 1)
        self.assertTrue(lst.get_all_clients()[0] == client1)

    def test_del_by_id_client(self):
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
        self.assertTrue (len(lst.get_all_clients()) == 1)
        self.assertTrue (lst.get_all_clients()[0] == client2)

    def test_get_all_clients(self):
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

    def test_add_client(self):
        """
        Verifica daca functia 'add_client' functioneaza corespunzator
        :return:
        """


        self.srv_client.add_client(1, 'Radu Suciu', 5020909260065)
        self.assertTrue(len(self.srv_client.get_all_clients()) == 1)

        with self.assertRaises(ValueError)as ve:
            self.srv_client.add_client(1, 'Rafael Nadal', 'a')
        self.assertTrue(str(ve.exception) == "Cnp-ul clientului este invalid.")


    def test_del_clients(self):
        """
        Verifica daca functia 'del_clients' functioneaza corespunzator
        :return:
        """


        self.srv_client.add_client(1, 'Radu Suciu', 5020909260065)
        self.srv_client.add_client(2, 'Vlad Suciu', 5141107265194)
        self.srv_client.del_clients(1)
        self.assertTrue (len(self.srv_client.get_all_clients()) == 1)
        self.assertTrue (self.srv_client.get_all_clients()[0].get_id() == 2)

        with self.assertRaises(ValueError) as ve:
            self.srv_client.del_clients(-5)
        self.assertEqual(str(ve.exception) , "Id invalid!")


    def test_get_client_by_id(self):
        """
        Verifica daca functia 'get_client_by_id' functioneaza corespunzator
        :return:
        """

        client1 = self.srv_client.add_client(1, 'Radu Suciu', 5020909260065)
        client2 = self.srv_client.add_client(2, 'Vlad Suciu', 5141107265194)
        assert self.srv_client.get_client_by_id(1) == client1
        assert self.srv_client.get_client_by_id(2) == client2

        with self.assertRaises(ValueError) as ve:
            self.srv_client.get_client_by_id(-5)
        self.assertEqual(str(ve.exception), "Id invalid!")

    def test_get_all_clients_2(self):
        """
        Verifica daca functia 'get_all_clients' functioneaza corespunzator
        :return:
        """

        client1 = self.srv_client.add_client(1, 'Radu Suciu', 5020909260065)
        client2 = self.srv_client.add_client(2, 'Vlad Suciu', 5141107265194)
        self.assertTrue((len(self.srv_client.get_all_clients()) == 2))
        self.assertTrue( self.srv_client.get_all_clients()[0] == client1)
        self.assertTrue( self.srv_client.get_all_clients()[1] == client2)
        self.srv_client.del_clients(1)
        self.assertTrue( self.srv_client.get_all_clients()[0] == client2)

    def test_update_nume_client(self):
        """
            Verifica daca functia 'update_nume_client' functioneaza corespunzator
            :return:
            """
        client1 = self.srv_client.add_client(1, 'Radu Suciu', 5020909260065)
        self.srv_client.update_nume_client(1, 'Mircea Suciu')
        self.assertTrue( client1.get_nume() == 'Mircea Suciu')

    def test_update_cnp_client(self):
        """
            Verifica daca functia 'update_cnp_client' functioneaza corespunzator
            :return:
        """

        client1 = self.srv_client.add_client(1, 'Radu Suciu', 5020909260065)
        self.srv_client.update_cnp_client(1, 1234567890123)
        self.assertTrue( client1.get_cnp() == 1234567890123)

    #filme

    def test_store_film(self):
        """
        Verifica daca functia 'store' functioneaza corespunzator
        :return:
        """
        lst = InMemoryRepository_film()
        film1 = Film(1, 'Batman', 'After training with his mentor, Batman begins his fight to free crime-ridden \
    Gotham City from corruption.', 'adventure')
        lst.store_film(film1)
        self.assertTrue(len(lst.get_all_films()) == 1)
        self.assertTrue(lst.get_all_films()[0] == film1)

    def test_del_by_id_film(self):
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
        self.assertTrue (len(lst.get_all_films()) == 1)
        self.assertTrue (lst.get_all_films()[0] == film2)

    def test_get_all_films(self):
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
        self.assertTrue (type(lst.get_all_films()) == list)
        self.assertTrue (len(lst.get_all_films()) == 1)

        lst.store_film(film2)
        self.assertTrue (len(lst.get_all_films()) == 2)
        self.assertTrue (lst.get_all_films()[0] == film1)
        self.assertTrue (lst.get_all_films()[1] == film2)

        lst.del_by_id_film(2)
        self.assertTrue (len(lst.get_all_films()) == 1)
        self.assertTrue (lst.get_all_films()[0] == film1)

    def test_add_film(self):
        """
        Verifica daca functia 'add_film' functioneaza corespunzator
        :return:
        """

        added_film = self.srv_film.add_film(1, 'Venom', 'Eddie Brock attempts to reignite his career by interviewing serial \
    killer Cletus Kasady, who becomes the host of the symbiote Carnage and escapes prison after a failed execution.',
    'action')
        self.assertTrue (added_film.get_titlu() == 'Venom')
        self.assertTrue (len(self.srv_film.get_all_films()) == 1)

        with self.assertRaises(ValueError) as ve:
            self.srv_film.add_film(1, 'Batman', 'fsas', 'fsdfs')
        self.assertEqual(str(ve.exception), "Exista deja un film cu id-ul dat!")

    def test_del_films(self):
        """
        Verifica daca functia 'del_films' functioneaza corespunzator
        :return:
        """

        self.srv_film.add_film(1, 'Eternals', 'Eternals is a 2021 American epic superhero film based on the Marvel Comics race \
    of the same name.', 'action')
        self.srv_film.add_film(2, 'The Godfather', 'The Godfather is a 1972 American crime film directed by Francis Ford Coppola, \
    who co-wrote the screenplay with Mario Puzo, based on Puzo s best-selling 1969 novel of the same name.', 'drama')
        self.srv_film.del_films(1)
        self.assertTrue (len(self.srv_film.get_all_films()) == 1)
        self.assertTrue( self.srv_film.get_all_films()[0].get_id() == 2)

        with self.assertRaises(ValueError) as ve:
            self.srv_film.del_films(-5)
        self.assertEqual(str(ve.exception), "Id invalid!")

    def test_update_titlu_film(self):
        """
        Verifica daca functia 'update_titlu_film' functioneaza corespunzator
        :return:
        """

        film = self.srv_film.add_film(1, 'Eternals', 'Eternals is a 2021 American epic superhero film based on the Marvel Comics race \
    of the same name.', 'action')
        self.srv_film.update_titlu_film(1, 'Star Wars')
        self.assertTrue( film.get_titlu() == 'Star Wars')

    def test_update_descriere_film(self):
        """
        Verifica daca functia 'update_descriere_film' functioneaza corespunzator
        :return:
        """
        film = self.srv_film.add_film(1, 'Eternals', 'Eternals is a 2021 American epic superhero film based on the Marvel Comics race \
    of the same name.', 'action')
        self.srv_film.update_descriere_film(1, 'descriere_test')
        self.assertTrue( film.get_descriere() == 'descriere_test')

    def test_update_gen_film(self):
        """
        Verifica daca functia 'update_gen_film' functioneaza corespunzator
        :return:
        """

        film = self.srv_film.add_film(1, 'Eternals', 'Eternals is a 2021 American epic superhero film based on the Marvel Comics race \
    of the same name.', 'action')
        self.srv_film.update_gen_film(1, 'gen_test')
        self.assertTrue( film.get_gen() == 'gen_test')

    def test_get_film_by_id(self):
        """
        Verifica daca functia 'get_film_by_id' functioneaza corespunzator
        :return:
        """
        film1 = self.srv_film.add_film(1, 'Venom', 'Eddie Brock attempts to reignite his career by interviewing serial killer Cletus Kasady, \
    who becomes the host of the symbiote Carnage and escapes prison after a failed execution.', 'action')
        film2 = self.srv_film.add_film(2, 'The Godfather', 'The Godfather is a 1972 American crime film directed by Francis Ford Coppola, \
    who co-wrote the screenplay with Mario Puzo, based on Puzo s best-selling 1969 novel of the same name.', 'drama')
        assert self.srv_film.get_film_by_id(1) == film1
        assert self.srv_film.get_film_by_id(2) == film2
        with self.assertRaises(ValueError) as ve:
            self.srv_film.get_film_by_id('m')
        self.assertEqual(str(ve.exception), "Id invalid!")

    def test_get_all_films_2(self):
        """
            Verifica daca functia 'get_all_clients' functioneaza corespunzator
            :return:
        """

        film1 = self.srv_film.add_film(1, 'Batman', 'After training with his mentor, Batman begins his fight to free crime-ridden \
    Gotham City from corruption.', 'adventure')
        film2 = self.srv_film.add_film(2, 'Venom', 'Eddie Brock attempts to reignite his career by interviewing serial killer Cletus Kasady, \
    who becomes the host of the symbiote Carnage and escapes prison after a failed execution.', 'action')
        self.assertTrue (len(self.srv_film.get_all_films()) == 2)
        self.assertTrue (self.srv_film.get_all_films()[0] == film1)
        self.assertTrue (self.srv_film.get_all_films()[1] == film2)
        self.srv_film.del_films(1)
        self.assertTrue (self.srv_film.get_all_films()[0] == film2)