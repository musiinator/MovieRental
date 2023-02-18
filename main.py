from domain.validators import film_validator
from domain.validators import client_validator
from domain.validators import inchiriere_validator
from repository.filme_repo import InMemoryRepository_film, InMemoryRepository_film_file
from repository.clienti_repo import InMemoryRepository_client, InMemoryRepository_client_file
from repository.inchiriere_repo import InMemoryRepository_inchiriere, InMemoryRepository_inchiriere_file
from service.filme_service import service_films
from service.clienti_service import service_clients
from service.inchiriere_service import service_inchiriere
from ui.console import Console

val_film = film_validator()
repo_film = InMemoryRepository_film()
repo_film_file = InMemoryRepository_film_file('film.txt')
srv_film = service_films(repo_film_file, val_film)

val_client = client_validator()
repo_client = InMemoryRepository_client()
repo_client_file = InMemoryRepository_client_file('client.txt')
srv_client = service_clients(repo_client_file, val_client)

repo_inchiriere = InMemoryRepository_inchiriere()
repo_inchiriere_file = InMemoryRepository_inchiriere_file('inchiriere.txt')
val_inchiriere = inchiriere_validator()
srv_inchiriere = service_inchiriere(repo_inchiriere_file, val_inchiriere, srv_client, srv_film)


ui = Console(srv_film, val_film, srv_client, val_client, srv_inchiriere, val_inchiriere)
ui.show_ui()