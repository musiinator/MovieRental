#modul care contine clasele din domeniul aplicatiei

#clasa de filme
class Film:
    def __init__(self, id, titlu, descriere, gen):
        """
        Initializeaza un obiect de tip Filme cu valorile date:
        :param id: id-ul filmului
        :type id: int
        :param titlu: titlul filmului
        :type titlu: str
        :param descriere: descrierea filmului
        :type descriere: str
        :param gen: genul filmului
        :type gen: str
        """
        self.__id = id
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen

    def get_id(self):
        return self.__id

    def get_titlu(self):
        return self.__titlu

    def get_descriere(self):
        return self.__descriere

    def get_gen(self):
        return self.__gen

    def set_id(self, value):
        self.__id = value

    def set_titlu(self, value):
        self.__titlu = value

    def set_descriere(self, value):
        self.__descriere = value

    def set_gen(self, value):
        self.__gen = value

    def __eq__(self, other):
        """
        Verifica egalitatea
        :param other: filmul cu care se compara filmul curent
        :type other: Product
        :return: True daca filmele sunt identice (au acelasi id), False altfel
        :rtype: bool
        """
        if self.__id == other.get_id():
            return True
        return False

    def __str__(self):
        return "Id:" + str(self.__id) + '  Titlu:' + str(self.__titlu) + '  Descriere:' + str(self.__descriere) + \
                '  Gen:' + str(self.__gen)

def test_create_film():
    p = Film(1, 'Venom', 'Eddie Brock attempts to reignite his career by interviewing serial killer Cletus Kasady, \
who becomes the host of the symbiote Carnage and escapes prison after a failed execution.', 'action')
    assert (p.get_id() == 1)
    assert (p.get_titlu() == 'Venom')
    assert (p.get_descriere() == 'Eddie Brock attempts to reignite his career by interviewing serial killer \
Cletus Kasady, who becomes the host of the symbiote Carnage and escapes prison after a failed execution.')
    assert (p.get_gen() == 'action')

    p.set_id(123)
    assert (p.get_id() == 123)
    p.set_titlu('Batman')
    p.set_descriere('After training with his mentor, Batman begins his fight to free crime-ridden Gotham City \
from corruption.')
    p.set_gen('adventure')
    assert (p.get_titlu() == 'Batman')
    assert (p.get_descriere() == 'After training with his mentor, Batman begins his fight to free crime-ridden \
Gotham City from corruption.')
    assert (p.get_gen() == 'adventure')

def test_equal_films():
    p1 = Film(121, 'Eternals', 'Eternals is a 2021 American epic superhero film based on the Marvel Comics race \
of the same name.', 'action')
    p2 = Film(121, 'Eternals', 'Eternals is a 2021 American epic superhero film based on the Marvel Comics race \
of the same name.', 'action')
    assert (p1 == p2)

    p3 = Film(151, 'The Godfather', 'The Godfather is a 1972 American crime film directed by Francis Ford Coppola, \
who co-wrote the screenplay with Mario Puzo, based on Puzo s best-selling 1969 novel of the same name.', 'drama')
    assert (p1 != p3)

test_create_film()
test_equal_films()


#clasa de clienti
class Client:
    def __init__(self, id, nume, cnp):
        """
        Initializeaza un obiect de tip Client cu valorile date:
        :param id: id-ul clientului
        :type id: int
        :param nume: numele clientului
        :type nume: str
        :param cnp: cnp-ul clientului
        :type cnp: int
        """
        self.__id = id
        self.__nume = nume
        self.__cnp = cnp

    def get_id(self):
        return self.__id

    def get_nume(self):
        return self.__nume

    def get_cnp(self):
        return self.__cnp

    def set_id(self, value):
        self.__id = value

    def set_nume(self, value):
        self.__nume = value

    def set_cnp(self, value):
        self.__cnp = value

    def __eq__(self, other):
        """
        Verifica egalitatea
        :param other: clientul cu care se compara clientul curent
        :type other: Clienti
        :return: True daca clientii sunt identici (au acelasi id), False altfel
        :rtype: bool
        """
        if not isinstance(other, Client):
            return False
        if self.__id != other.get_id():
            return False
        return True

    def __str__(self):
        return "Id:" + str(self.__id) + '  Nume:' + str(self.__nume) + '  Cnp:' + str(self.__cnp)

def test_create_client():
    p = Client(1,'Radu Suciu',5020909260065)
    assert (p.get_id() == 1)
    assert (p.get_nume() == 'Radu Suciu')
    assert (p.get_cnp() == 5020909260065)

    p.set_id(2)
    p.set_nume('Dorin Suciu')
    p.set_cnp(1720308269726)
    assert (p.get_id() == 2)
    assert (p.get_nume() == 'Dorin Suciu')
    assert (p.get_cnp() == 1720308269726)

def test_equal_clients():
    p1 = Client(1,'Radu Suciu', 5020909260065)
    p2 = Client(1,'Radu Suciu', 5020909260065)
    assert (p1 == p2)

    p3 = Client(2, 'Vlad Suciu', 5141107265194)
    assert (p1 != p3)

#clasa de inchiriere
class Inchiriere():

    def __init__(self, id, Client, Film):
        """
        Initializeaza un obiect de tip Inchiriere cu valorile date:
        :param id_client: id-ul clientului ce inchiriaza un film
        :param id_film: id-ul filmului inchiriat
        """
        self.__id = id
        self.__Client = Client
        self.__Film = Film

    def get_id(self):
        return self.__id

    def get_Client(self):
        return self.__Client

    def get_Film(self):
        return self.__Film

    def set_id(self, value):
        self.__id = value

    def set_Client(self, value):
        self.__Client = value

    def set_Film(self, value):
        self.__Film = value

    def __eq__(self, other):
        if self.__id == other.get_id():
            return True
        return False

    def __str__(self):
        return "Id:" + str(self.__id) + '  Client:' + str(self.__Client.get_nume()) + '  Film:' + str(self.__Film.get_titlu())






