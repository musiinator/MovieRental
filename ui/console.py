from termcolor import colored
import random
import string
from random import seed
from random import randint
from exceptions.exceptions import DuplicateIDException

def randomword(length):
    length = int(length)
    string1 = ''.join(random.choices(string.ascii_lowercase, k=length))
    return string1

def randomint():
    string2 = random.randint(10**12, 10**13-1)
    return string2

class Console:

    def __init__(self, srv_film, film_validator, srv_client, client_validator, srv_inchiriere, val_inchiriere):
        self.__srv_film = srv_film
        self.__val_film = film_validator
        self.__srv_client = srv_client
        self.__val_client = client_validator
        self.__srv_inchiriere = srv_inchiriere
        self.__val_inchiriere = val_inchiriere

    def __generate_client(self):
        ok = True
        try:
            numar_generari = int(input("Introduceti numarul de generari:"))
            id_generari = int(input("Introduceti id-ul de la care sa inceapa generarile:"))
        except ValueError:
            print()
            print(colored("Valoare invalida!", 'red'), '\n')
            return
        seed(1)
        for i in range(id_generari, numar_generari + 1):
            id_client = i
            nume = randomword(7)
            cnp = randomint()
            try:
                self.__srv_client.add_client(id_client, nume, cnp)
            except ValueError:
                print()
                print(colored('Exista deja clienti cu id-urile generate!', 'red'), '\n')
                ok = False
                break
        if ok:
            print()
            print(numar_generari, 'clienti', colored('au fost adaugati cu succes!', 'cyan'), '\n')

    def __generate_film(self):
        ok = True
        try:
            numar_generari = int(input("Introduceti numarul de generari:"))
            id_generari = int(input("Introduceti id-ul de la care sa inceapa generarile:"))
        except ValueError:
            print()
            print(colored("Valoare invalida!", 'red'), '\n')
            return
        seed(1)
        for i in range(id_generari, numar_generari + 1):
            id_film = i
            titlu = randomword(6)
            descriere = randomword(10)
            gen = randomword(4)
            try:
                self.__srv_film.add_film(id_film, titlu, descriere, gen)
            except ValueError:
                print()
                print(colored('Exista deja filme cu id-urile generate!', 'red'), '\n')
                ok = False
                break
        if ok:
            print()
            print(numar_generari, 'filme', colored('au fost adaugate cu succes!', 'cyan'), '\n')

    #films_ui
    def __show_all_films(self):
        """
        Afiseaza toate filmele disponibile
        """
        films = self.__srv_film.get_all_films()
        if len(films) == 0:
            print(colored('Nu exista filme in lista!', 'yellow'))
        else:
            print('Lista de filme este: ')
            for film in films:
                print('Id:', colored(film.get_id(),'cyan'), ' - Titlu:', colored(film.get_titlu(), 'cyan'),
                      '- Descriere:',colored(film.get_descriere(), 'cyan'),' - Gen:', colored(film.get_gen(), 'cyan'))

    def __add_film(self):
        """
        Adauga un film
        """
        try:
            id = input('Id-ul filmului este: ')
            self.__val_film.validate_id_film(id)
            id = int(id)
            if self.__srv_film.exists_with_id_film(id):
                raise ValueError('Exista deja un film cu id-ul dat!')
            titlu = input('Titlul filmului este: ')
            self.__val_film.validate_titlu_film(titlu)
            descriere = input('Descrierea filmului este: ')
            self.__val_film.validate_descriere_film(descriere)
            gen = input('Genul filmului este: ')
            self.__val_film.validate_gen_film(gen)
            try:
                added_film = self.__srv_film.add_film(id, titlu, descriere, gen)
                print()
                print(colored('Filmul: ','cyan'), added_film, colored('a fost adaugat cu succes!','cyan'))
                print()
            except ValueError as ve:
                print()
                print(colored(str(ve), 'red'),'\n')
        except ValueError as VE:
            print()
            print('Validation error: ' + colored(str(VE), 'red'), '\n')

    def __delete_film(self):
        """
        Sterge filmul cu id-ul dat
        :return:
        """
        try:
            id = input("Se va sterge filmul cu id-ul: ")
            self.__val_film.validate_id_film(id)
            id = int(id)
        except ValueError as VE:
            print()
            print('Validation error: ' + colored(str(VE), 'red'), '\n')
            return
        try:
            self.__srv_film.del_films(id)
        except ValueError as VE:
            print()
            print('Validation error: ' + colored(str(VE),'red'),'\n')

    def __update_film(self):
        """
        Modifica infromatiile despre un client dat dupa id
        :return:
        """
        try:
            id = input("Se va modifica filmul cu id-ul: ")
            self.__val_film.validate_id_film(id)
            id = int(id)
            if self.__srv_film.exists_with_id_film(id) == False:
                raise ValueError('Nu exista film cu id-ul dat!')
        except ValueError as VE:
            print()
            print('Validation error: ' + colored(str(VE), 'red'), '\n')
            return

        try:
            film = self.__srv_film.get_film_by_id(id)
            modificare = input('Se va face o modificare la (titlu/descriere/gen): ')
            modificare = modificare.lower().strip()
            if modificare == 'titlu':
                titlu_nou = input('Noul titlu este: ')
                self.__val_film.validate_titlu_film(titlu_nou)
                film = self.__srv_film.update_titlu_film(id, titlu_nou)
                print()
                print(colored('Filmul: ', 'cyan'), film, colored('a fost modificat cu succes!', 'cyan'), '\n')
            elif modificare == 'descriere':
                descriere_noua = input('Noua descriere este: ')
                self.__val_film.validate_descriere_film(descriere_noua)
                film = self.__srv_film.update_descriere_film(id, descriere_noua)
                print()
                print(colored('Filmul: ', 'cyan'), film, colored('a fost modificat cu succes!', 'cyan'))
                print()
            elif modificare == 'gen':
                gen_nou = input('Noul gen este: ')
                self.__val_film.validate_gen_film(gen_nou)
                film = self.__srv_film.update_gen_film(id, gen_nou)
                print()
                print(colored('Filmul: ', 'cyan'), film, colored('a fost modificat cu succes!', 'cyan'))
                print()
            else:
                print()
                print(colored('Modificare invalida!', 'red'), '\n')
        except ValueError as VE:
            print()
            print('Validation error: ' + colored(str(VE), 'red'), '\n')

    def __get_film_by_id(self):
        """
        Gaseste film dupa id
        :return:
        """
        try:
            id = input("Se va cauta filmul cu id-ul: ")
            self.__val_film.validate_id_film(id)
            id = int(id)
        except ValueError as VE:
            print()
            print('Validation error: ' + colored(str(VE), 'red'), '\n')
            return
        try:
            film = self.__srv_film.get_film_by_id(id)
            print()
            print(colored('Clientul: ', 'cyan'), film, colored('a fost gasit cu succes!', 'cyan'))
            print()
        except ValueError as VE:
            print()
            print('Validation error: ' + colored(str(VE), 'red'), '\n')


    #clients_ui
    def __show_all_clients(self):
        """
        Afiseaza toti clientii disponibili
        """
        clients = self.__srv_client.get_all_clients()
        if len(clients) == 0:
            print(colored('Nu exista clienti in lista!', 'yellow'))
        else:
            print('Lista de clienti este: ')
            for client in clients:
                print('Id:', colored(client.get_id(), 'cyan'), ' - Nume:', colored(client.get_nume(), 'cyan'),
                      '- Cnp:', colored(client.get_cnp(), 'cyan'))

    def __add_client(self):
        """
        Adauga un client
        """
        try:
            id = input('Id-ul clientului este: ')
            self.__val_client.validate_id_client(id)
            id = int(id)
            if self.__srv_client.exists_with_id_client(id):
                raise ValueError('Exista deja un client cu id-ul dat!')
            nume = input('Numele clientului este: ')
            self.__val_client.validate_nume_client(nume)
            cnp = input('Cnp-ul clientului este: ')
            self.__val_client.validate_cnp_client(cnp)
            cnp = int(cnp)
            try:
                added_client = self.__srv_client.add_client(id, nume, cnp)
                print()
                print(colored('Clientul: ', 'cyan'), added_client, colored('a fost adaugat cu succes!', 'cyan'))
                print()
            except ValueError as ve:
                print()
                print(colored(str(ve), 'red'), '\n')
        except ValueError as VE:
            print()
            print('Validation error: ' + colored(str(VE), 'red'), '\n')

    def __delete_client(self):
        """
        Sterge clientul cu id-ul dat
        :return:
        """
        try:
            id = input("Se va sterge clientul cu id-ul: ")
            self.__val_client.validate_id_client(id)
            id = int(id)
        except ValueError as VE:
            print()
            print('Validation error: ' + colored(str(VE), 'red'), '\n')
            return
        try:
            deleted_client = self.__srv_client.get_client_by_id(id)
            self.__srv_client.del_clients(id)
            print()
            print(colored('Clientul: ', 'cyan'), deleted_client, colored('a fost sters cu succes!', 'cyan'))
            print()
        except ValueError as ve:
            print()
            print(colored(str(ve), 'red'), '\n')

    def __update_client(self):
        """
        Modifica infromatiile despre un client dat dupa id
        :return:
        """
        try:
            id = input("Se va modifica clientul cu id-ul: ")
            self.__val_client.validate_id_client(id)
            id = int(id)
            if self.__srv_client.exists_with_id_client(id) == False:
                raise ValueError('Nu exista client cu id-ul dat!')
        except ValueError as VE:
            print()
            print('Validation error: ' + colored(VE, 'red'), '\n')
            return

        try:
            client = self.__srv_client.get_client_by_id(id)
            modificare = input('Se va face o modificare la (nume/cnp): ')
            modificare = modificare.lower().strip()
            if modificare == 'nume':
                nume_nou = input('Noul nume este: ')
                self.__val_client.validate_nume_client(nume_nou)
                client = self.__srv_client.update_nume_client(id, nume_nou)
                print()
                print(colored('Clientul: ', 'cyan'), client, colored('a fost modificat cu succes!', 'cyan'))
                print()
            elif modificare == 'cnp':
                cnp_nou = input('Noul cnp este: ')
                self.__val_client.validate_cnp_client(cnp_nou)
                cnp_nou = int(cnp_nou)
                client = self.__srv_client.update_cnp_client(id, cnp_nou)
                print()
                print(colored('Clientul: ', 'cyan'), client, colored('a fost modificat cu succes!', 'cyan'))
                print()
            else:
                print()
                print(colored('Modificare invalida!', 'red'), '\n')
        except ValueError as VE:
            print()
            print('Validation error: ' + colored(str(VE), 'red'), '\n')


    def __get_client_by_id(self):
        """
        Gaseste client dupa id
        :return:
        """
        try:
            id = input("Se va cauta clientul cu id-ul: ")
            self.__val_client.validate_id_client(id)
            id = int(id)
        except ValueError as VE:
            print()
            print('Validation error: ' + colored(str(VE), 'red'), '\n')
            return
        try:
            client = self.__srv_client.get_client_by_id(id)
            print()
            print(colored('Clientul: ', 'cyan'), client, colored('a fost gasit cu succes!', 'cyan'))
            print()
        except ValueError as VE:
            print()
            print('Validation error: ' + colored(str(VE), 'red'), '\n')


    def __Inchiriere(self):
        """
        Realizeaza inchirierea filmelor de catre clienti
        :return:
        """
        try:
            id_inchiriere = input('Id-ul inchirierii va fi:')
            self.__val_inchiriere.validate_id_inchiriere(id_inchiriere)  # se aplica aceleasi validari pt id-ul inscrierii
            id_inchiriere = int(id_inchiriere)
            if self.__srv_inchiriere.exists_with_id_inchiriere(id_inchiriere) == True:
                raise ValueError('Exista deja o inchiriere cu id-ul dat!')
            id_client = input('Id-ul clientului care va inchiria un film:')
            self.__val_client.validate_id_client(id_client)
            id_client = int(id_client)
            if self.__srv_client.exists_with_id_client(id_client) == False:
                raise ValueError('Nu exista client cu id-ul dat!')
            id_film = input('Id-ul filmului care va fi inchiriat:')
            self.__val_film.validate_id_film(id_film)
            id_film = int(id_film)
            if self.__srv_film.exists_with_id_film(id_film) == False:
                raise ValueError('Nu exista film cu id-ul dat!')

            try:

                inchiriere = self.__srv_inchiriere.add_inchiriere(id_inchiriere, id_client, id_film)
                print()
                print(colored('Inchirierea: ', 'cyan'), inchiriere, colored('a fost efectuata cu succes!', 'cyan'))
                print()
            except ValueError as VE:
                print()
                print('Validation error: ' + colored(str(VE), 'red'), '\n')
        except ValueError as VE:
            print()
            print('Validation error: ' + colored(VE, 'red'), '\n')

    def __sort_by_name(self):
        """
        Ordoneaza toate inchirierile dupa numele clientilor
        """
        rentals = self.__srv_inchiriere.get_all_rentals()
        if len(rentals) == 0:
            print()
            print(colored('Nu exista inchirieri in lista!', 'yellow'), '\n')
        else:
            self.__srv_inchiriere.sort_inchiriere_by_nume_client()
            print()
            print(colored('Sortarea listei de inchirieri, dupa numele clientilor, a fost efectuata cu succes!', 'green'),'\n')

    def __sort_by_films(self):
        """
        Ordoneaza toate inchirierile dupa numarul de filme inchiriate
        """
        rentals = self.__srv_inchiriere.get_all_rentals()
        if len(rentals) == 0:
            print()
            print(colored('Nu exista inchirieri in lista!', 'yellow'), '\n')
        else:
            self.__srv_inchiriere.sort_inchiriere_by_nr_of_films()
            print()
            print(colored('Sortarea listei de inchirieri, dupa numarul de filme inchiriate, a fost efectuata cu succes!', 'green'),'\n')

    def __show_top_3_movies(self):
        """
        Afiseaza primele 3 cele mai inchiriate filme
        """
        rentals = self.__srv_inchiriere.get_all_rentals()
        if len(rentals) == 0:
            print()
            print(colored('Nu exista inchirieri in lista!', 'red'), '\n')
        else:
            try:
                top_3_movies = []
                top_3_movies = self.__srv_inchiriere.get_top3_movies()
                if len(top_3_movies) < 3:
                    raise ValueError('Nu exista destule inchirieri in lista pt a afisa un top 3!')
                else:
                    print()
                    print(colored('Top 3 cele mai inchiriate filme sunt: ', 'magenta'))
                    for rent in top_3_movies:
                        film = rent.get_Film()
                        print('Titlu:', colored(film.get_titlu(), 'cyan'),
                              ' - Nr de inchirieri:', colored(self.__srv_inchiriere.nr_of_movies_film(film), 'cyan'))
                    print()
            except ValueError as VE:
                print()
                print(colored(VE, 'red'), '\n')


    def __show_top_3_clients(self):
        """
        Afiseaza primii 3 clienti cu cele mai multe filme inchiriate
        """
        rentals = self.__srv_inchiriere.get_all_rentals()
        if len(rentals) == 0:
            print()
            print(colored('Nu exista inchirieri in lista!', 'red'), '\n')
        else:
            try:
                top_3_clients = []
                top_3_clients = self.__srv_inchiriere.get_top3_clients()
                if len(top_3_clients) < 3:
                    raise ValueError('Nu exista destule inchirieri in lista pt a afisa un top 3!')
                else:
                    print()
                    print(colored('Top 3 clienti cu cele mai multe filme inchiriate sunt: ', 'magenta'))
                    for rent in top_3_clients:
                        client = rent.get_Client()
                        print('Nume:', colored(client.get_nume(), 'cyan'), ' - Nr de filme inchiriate:',
                              colored(self.__srv_inchiriere.nr_of_movies_client(client), 'cyan'))
                    print()
            except ValueError as VE:
                print()
                print(colored(VE, 'red'), '\n')

    def __show_top_30_la_suta_clients(self):
        """
        Afiseaza primii 30 % clienti cu cele mai multe filme inchiriate
        """
        rentals = self.__srv_inchiriere.get_all_rentals()
        if len(rentals) == 0:
            print()
            print(colored('Nu exista inchirieri in lista!', 'red'), '\n')
        else:
            top_30_clients = []
            try:
                top_30_clients = self.__srv_inchiriere.get_top30_la_suta()
                if len(top_30_clients) < 1:
                    raise ValueError('Nu exista destule inchirieri in lista pt a afisa primii 30% din clienti!')
                else:
                    print()
                    print(colored('Primii 30% clienti cu cele mai multe filme inchiriate sunt: ', 'magenta'))
                    for rent in top_30_clients:
                        client = rent.get_Client()
                        print('Nume:', colored(client.get_nume(), 'cyan'), ' - Filme inchiriate:',
                              colored(self.__srv_inchiriere.nr_of_movies_client(client), 'cyan'))
                    print()
            except ValueError as VE:
                print()
                print(colored(VE, 'red'), '\n')

    def __show_all_rentals(self):
        """
        Afiseaza toate inchirierile
        """
        rentals = self.__srv_inchiriere.get_all_rentals()
        if len(rentals) == 0:
            print()
            print(colored('Nu exista inchirieri in lista!', 'yellow'), '\n')
        else:
            print(colored('Lista de inchirieri este: ', 'magenta'))
            for rent in rentals:
                print('Id:', colored(rent.get_id(), 'cyan'), ' - Client:', colored(rent.get_Client().get_nume(), 'cyan'),
                      '- Film:', colored(rent.get_Film().get_titlu(), 'cyan'))


    def show_ui(self):
        print()
        while True:
            option = input(colored('Se va gestiona o lista de (filme/clienti/inchirieri): ', 'cyan'))
            option = option.lower().strip()
            if option == 'filme':
                print(colored('Comenzi disponibile: ','magenta'), 'add, delete, update, find, random, show_all, exit')
                cmd = input('Comanda dvs este: ')
                cmd = cmd.lower().strip()
                if cmd == 'add':
                    self.__add_film()
                elif cmd == 'delete':
                    self.__delete_film()
                elif cmd == 'update':
                    self.__update_film()
                elif cmd == 'find':
                    self.__get_film_by_id()
                elif cmd == 'random':
                    self.__generate_film()
                elif cmd == 'show_all':
                    self.__show_all_films()
                elif cmd == 'exit':
                    return
                else:
                    print()
                    print(colored('Comanda invalida!', 'red'),'\n')
            elif option == 'clienti':
                print(colored('Comenzi disponibile: ', 'magenta'), 'add, delete, update, find, random, show_all, exit')
                cmd = input('Comanda dvs este: ')
                cmd = cmd.lower().strip()
                if cmd == 'add':
                    self.__add_client()
                elif cmd == 'delete':
                    self.__delete_client()
                elif cmd == 'update':
                    self.__update_client()
                elif cmd == 'find':
                    self.__get_client_by_id()
                elif cmd == 'random':
                    self.__generate_client()
                elif cmd == 'show_all':
                    self.__show_all_clients()
                elif cmd == 'exit':
                    return
                else:
                    print()
                    print(colored('Comanda invalida!', 'red'), '\n')
            elif option == 'inchirieri':
                print(colored('Comenzi disponibile: ', 'magenta'), 'add, sort_by_name, sort_by_nr_of_movies, top_3_movies, top_3_clients, top_30%_clients, show_all, exit')
                cmd = input('Comanda dvs este: ')
                cmd = cmd.lower().strip()
                if cmd == 'add':
                    self.__Inchiriere()
                elif cmd == 'sort_by_name':
                    self.__sort_by_name()
                elif cmd == 'sort_by_nr_of_movies':
                    self.__sort_by_films()
                elif cmd == 'top_3_movies':
                    self.__show_top_3_movies()
                elif cmd == 'top_3_clients':
                    self.__show_top_3_clients()
                elif cmd == 'top_30%_clients':
                    self.__show_top_30_la_suta_clients()
                elif cmd == 'show_all':
                    self.__show_all_rentals()
                elif cmd == 'exit':
                    return
                else:
                    print()
                    print(colored('Comanda invalida!', 'red'), '\n')
            else:
                print()
                if str(option) == '':
                    print(colored('Lista invalida!', 'red'), '\n')
                else:
                    print(colored('Lista de ','red'), str(option), colored('este invalida!','red'), '\n')