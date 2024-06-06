# Pour utiliser le projet avec docker il faut cloner les 5 répertoires git de l’organisation et respecter l’architecture suivante :
│création d'un dossier qui contient l'ensempble projet/
├── api_clients/
│  
├── api_commandes/
│    
├── api_produits/
│   
├── message_broker/
│  
├── docker-compose.yml

Le fichier docker-compose.yml se trouve dans le répertoire docker_config.
Il faut ensuite utiliser les commandes suivantes dans le dossier qui contient l'ensemble du projet
docker-compose down -v
docker-compose up --build

Une fois le projet monté dans docker il suffit de lancer le container de du message broker en premier puis celui des API
Les requêtes peuvent être faite sà l’aide de la collection postman disponible dans le repertoire git postman. 
Elle est configurée pour faire des requêtes sur les API qui tournent sur docker.
