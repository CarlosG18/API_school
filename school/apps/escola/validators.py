import re
from validate_docbr import CPF

def validate_nome(nome):
    return not nome.isalpha()

def validate_cpf(number_cpf):
    cpf = CPF()
    return not cpf.validate(number_cpf)

def validate_telefone(telefone):
    regex_modelo = r'^\(?\d{2}\)?[\s-]?\d{4,5}-\d{4}$|^\d{4,5}-\d{4}$'
    return not re.findall(regex_modelo, telefone)