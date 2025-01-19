def validate_user_data(data):
    required_fields = ['matricula', 'primeiro_nome', 'ultimo_nome', 'email', 'password']
    return all(field in data for field in required_fields)


def get_user_response(user):
    return {
        'id': user.id,
        'nome': user.first_name + " " + user.last_name,
        'email': user.email,
    }
