import re


def verificar_arquivo(arquivo_user: str)-> str:
    try:
        with open(arquivo_user, "r") as arquivo:
            info = arquivo.read()
    except FileNotFoundError:
        return None
    else:
        return info
    
def encontrar_emails(arquivo_user: str):
    info = verificar_arquivo(arquivo_user)
    
    if info:
        email_regex = re.compile(r"[\w\d.-]+@{1}[\w\d\.-]+")
        emails_encontrados = re.findall(email_regex, info)
        
        if emails_encontrados:
            print("Emails encontrados:\n")
            
            for email in emails_encontrados:
                print(f"-> {email}")
                
        else:
            print("Nenhum email foi encontrado neste arquivo!")
            
    else:
        print("Esse arquivo não foi encontrado ou está vazio! Tente novamente!")