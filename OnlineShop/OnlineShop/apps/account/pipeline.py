def get_username(strategy, details, backend, user=None, *args, **kwargs):
    username = details['email'].split('@')[0]
    return {'username' : username}