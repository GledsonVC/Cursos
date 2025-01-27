def build_profile(first, last, **user_info):
    """Cria um dicionário contendo tudo o que sabemos sobre um usuário"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
use_profile = build_profile(
    'gledson', 
    'vasconcellos cavalheiro',
    data_nascimento = '21/05/1982',
    local_nascimento = 'são paulo',
    profissao = 'programador',
    )
print(use_profile)
