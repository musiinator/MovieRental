from domain.entities import Film
from domain.entities import Client
from exceptions.exceptions import DuplicateIDException

#clasa de validare a filmului
class film_validator:
    """
        clasa pentru incapsularea algoritmului de validare
        (validate putea fi metoda in clasa Film - choice of design)
    """
    def validate_film(self, film):
        errors = []
        if type(film.get_id()) == int:
            if film.get_id() < 0:
                errors.append("Id-ul filmului nu poate fi negativ.")
        elif type(film.get_id()) != int:
                errors.append("Id-ul filmului este invalid.")
        if film.get_id() == '':
            errors.append("Id-ul filmului nu poate fi vid.")
        if film.get_titlu() == '':
            errors.append("Titlul filmului nu poate fi vid.")
        if film.get_descriere() == '':
            errors.append("Descrierea filmului nu poate fi vida.")
        if film.get_gen() == '':
            errors.append("Genul filmului nu poate fi vid.")

        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)
            # raise ValidationException

    def validate_id_film(self, id):
        errors = []
        # val stabileste daca id-ul e de tipul int
        try:
            int(id)
            val = True
        except ValueError:
            val = False

        if val == False:
            errors.append('Formatul id-ului este incorect!')
        else:
            id = int(id)
            if id < 0:
                errors.append('Id-ul filmului nu poate fi negativ!')
        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)

    def validate_titlu_film(self, titlu):
        errors = []
        if titlu == '':
            errors.append('Formatul titlului este incorect!')
        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)

    def validate_descriere_film(self, descriere):
        errors = []
        if descriere == '':
            errors.append('Formatul descrierii este incorect!')
        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)

    def validate_gen_film(self, gen):
        errors = []
        if gen == '':
            errors.append('Formatul genului este incorect!')
        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)


def test_validate_film():
    validator = film_validator()
    p = Film(151,'The Godfather', 'The Godfather is a 1972 American crime film directed by Francis Ford Coppola, \
who co-wrote the screenplay with Mario Puzo, based on Puzo s best-selling 1969 novel of the same name.', 'drama')
    validator.validate_film(p)

    p1 = Film(1, '', 'Batman is a superhero who appears in American comic books published by DC Comics.', 'action')
    try:
        validator.validate_film(p1)
        assert False
    except ValueError:
        assert True

    p2 = Film(-2,'The Maze Runner', 'Thomas is deposited in a community of boys after his memory is erased, \
soon learning they;re all trapped in a maze that will require him to join forces with fellow "runners" for \
a shot at escape.', 'action')

    try:
        validator.validate_film(p2)
        assert False
    except ValueError:
        assert True

def test_validate_id_film():
    """
    Verifica daca functia 'validate_id_film' functioneaza corespunzator
    :return:
    """
    validator = film_validator()
    p1 = Film(-1, 'The Godfather', 'The Godfather is a 1972 American crime film directed by Francis Ford Coppola, \
who co-wrote the screenplay with Mario Puzo, based on Puzo s best-selling 1969 novel of the same name.', 'drama')
    try:
        validator.validate_id_film(p1.get_id)
        assert False
    except ValueError:
        assert True

    p2 = Film(' ', 'The Maze Runner', 'Thomas is deposited in a community of boys after his memory is erased, \
soon learning they;re all trapped in a maze that will require him to join forces with fellow "runners" for \
a shot at escape.', 'action')
    try:
        validator.validate_film(p2.get_id())
        assert False
    except ValueError:
        assert True

def test_validate_titlu_film():
    """
    Verifica daca functia 'validate_titlu_film' functioneaza corespunzator
    :return:
    """
    validator = film_validator()
    p = Film(1, '', 'The Godfather is a 1972 American crime film directed by Francis Ford Coppola, \
who co-wrote the screenplay with Mario Puzo, based on Puzo s best-selling 1969 novel of the same name.', 'drama')
    try:
        validator.validate_titlu_film(p.get_titlu)
        assert False
    except ValueError:
        assert True

def test_validate_descriere_film():
    """
    Verifica daca functia 'validate_descriere_film' functioneaza corespunzator
    :return:
    """
    validator = film_validator()
    p = Film(1, 'The Godfather', '', 'drama')
    try:
        validator.validate_descriere_film(p.get_descriere)
        assert False
    except ValueError:
        assert True

def test_validate_gen_film():
    """
    Verifica daca functia 'validate_gen_film' functioneaza corespunzator
    :return:
    """
    validator = film_validator()
    p = Film(1, 'The Godfather', 'The Godfather is a 1972 American crime film directed by Francis Ford Coppola, \
    who co-wrote the screenplay with Mario Puzo, based on Puzo s best-selling 1969 novel of the same name.', '')
    try:
        validator.validate_gen_film(p.get_gen)
        assert False
    except ValueError:
        assert True


#clasa de validare a clientului
class client_validator:
    """
        clasa pentru incapsularea algoritmului de validare
        (validate putea fi metoda in clasa Client - choice of design)
    """
    def validate_client(self, client):
        errors = []
        if type(client.get_id()) == int:
            if client.get_id() < 0:
                errors.append("Id-ul clientului nu poate fi negativ.")
        elif type(client.get_id()) != int:
            errors.append("Id-ul clientului este invalid.")
        if client.get_id() == '':
            errors.append("Id-ul clientului nu poate fi vid.")
        if client.get_nume() == '':
            errors.append("Numele clientului nu poate fi vid")
        if client.get_cnp() == '':
            errors.append("Cnp-ul clientului nu poate fi vid")
        if type(client.get_cnp()) == int:
            if len(str(client.get_cnp())) != 13:
                errors.append("Cnp-ul clientului trebuie sa fie format din 13 cifre.")
        elif type(client.get_cnp()) != int:
            errors.append("Cnp-ul clientului este invalid.")

        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)
            # raise ValidationException

    def validate_id_client(self, id):
        #val stabileste daca id-ul e de tipul int sau nu
        errors = []
        try:
            int(id)
            val = True
        except ValueError:
            val = False

        if val == False:
            errors.append('Formatul id-ului este incorect!')
        else:
            id = int(id)
            if id < 0:
                errors.append('Id-ul clientului nu poate fi negativ!')
        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)

    def validate_nume_client(self, nume):
        errors = []
        if nume == '':
            errors.append('Formatul numelui este incorect!')
        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)

    def validate_cnp_client(self, cnp):
        errors = []
        try:
            int(cnp)
            val = True
        except ValueError:
            val = False

        if val == False:
            errors.append('Formatul cnp-ului este incorect!')
        else:
            cnp = int(cnp)
            if cnp < 0:
                errors.append('Formatul cnp-ului este incorect!')
            if len(str(cnp)) != 13:
                errors.append('Formatul cnp-ului este incorect!')
        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)

def test_validate_id_client():
    """
    Verifica daca functia 'validate_id_client' functioneaza corespunzator
    :return:
    """
    validator = client_validator()
    p1 = Client(-1, 'Radu Suciu', 5020909260065)
    p2 = Client('', 'Radu Suciu', 5020909260065)
    try:
        validator.validate_client(p1.get_id)
        assert False
    except ValueError:
        assert True

    try:
        validator.validate_client(p2.get_id)
        assert False
    except ValueError:
        assert True

def test_validate_nume_client():
    """
    Verifica daca functia 'validate_nume_client' functioneaza corespunzator
    :return:
    """
    validator = client_validator()
    p = Client(1, '', 5028282942766)
    try:
        validator.validate_id_client(p.get_nume)
        assert False
    except ValueError:
        assert True

def test_validate_cnp_client():
    """
    Verifica daca functia 'validate_cnp_client' functioneaza corespunzator
    :return:
    """
    validator = client_validator()
    p1 = Client(1, 'Radu Suciu', 'a')
    p2 = Client(1, 'Radu Suciu', 1234)
    try:
        validator.validate_cnp_client(p1.get_cnp)
        assert False
    except ValueError:
        assert True

    try:
        validator.validate_cnp_client(p2.get_cnp)
        assert False
    except ValueError:
        assert True

#clasa de validare a inchirierii
class inchiriere_validator:
    """
        clasa pentru incapsularea algoritmului de validare
        (validate putea fi metoda in clasa Client - choice of design)
    """

    def validate_id_inchiriere(self, id):
        #val stabileste daca id-ul e de tipul int sau nu
        errors = []
        try:
            int(id)
            val = True
        except ValueError:
            val = False

        if val == False:
            errors.append('Formatul id-ului este incorect!')
        else:
            id = int(id)
            if id < 0:
                errors.append('Id-ul inchirierii nu poate fi negativ!')
        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)
