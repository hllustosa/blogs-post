import shortuuid

def create_id(prefix):
    return f'{prefix}_{shortuuid.uuid()}'