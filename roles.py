from flask import request, jsonify

#Les roles dépendent de la valeur du token
#1 Read
#2 Read Update
#3 Read Update Create User
#4 Read Update Create Delete

#pour vérifier le rôle de l'utilisateur et générer un token en conséquence
def check_token_right(token):
    if token == 'omzRfFaKaZsI1LkziC8co7dMEb9cKgzBvJbOfrHkv0KDcXQGfMZj1iFHeLRmoXPD':
        return 1
    elif token == 'A6s4kRxuawKMrXzKe9Y6drksvDXLAcOc6GISk7v8RDlPM8VLxqYSBAQrWfQkzm44':
        return 2
    elif token == 'vyS2L3ieJBe4hI5k5CQZ1JGY3OqUl7G8suTvtJAxvuYDaX85y0d9e9UzW7wQsUeE':
        return 3
    elif token == 'keFcYRLjAS4Tq6hEp4JFPkGR1d0IHJd58Xe2mvkz2gidmRg4v5B0QWhbAVlJ4Kts':
        return 4
    else:
        return 0  
    
def read_possible(token):
    if check_token_right(token)>=1:
        return True
    return False

def update_possible(token):
    if  check_token_right(token)>=2:
        return True
    return False

def creation_possible(token):
    if check_token_right(token)>=3:
        return True
    return False

def delete_possible(token):
    if  check_token_right(token)>=4:
        return True
    return False