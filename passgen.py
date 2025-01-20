import secrets
import string

R1 = "\033[0m" 
Y2 = "\033[93m"  
R2 = "\033[91m"

def generate_secure_password(length=16, use_uppercase=True, use_digits=True, use_special_chars=True):
    if length < 8:
        raise ValueError("La longitud mínima recomendada es de 8 caracteres.")

    char_pool = string.ascii_lowercase
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_special_chars:
        char_pool += string.punctuation

    password = []
    if use_uppercase:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_special_chars:
        password.append(secrets.choice(string.punctuation))

    password += [secrets.choice(char_pool) for _ in range(length - len(password))]

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    print(R2 + r"""
'''''''''',:ldOXWMMMWk,   .lKMMMMN0xol:,''''''''''
'''''''',:lx0XWMMMWKl.     .;OWMMMWNKOdl:,''''''''
'''''',:oOXWMMMMWKl.       .co0WMMMMMWN0xoc,''''''
'''',;lkXWMMMMWKl.      .,:dOKNWKKNMMMMMN0xo:''''#                           
''',:o0WMMMMWKl.      .:dkkKNWKkc,;xXMMMMWXkdc,'''                                  
'',:dKMMMMWKl.      .:dkKXNWKkl,.  .;xXMMMMNOdl,''
',:dKMMMMMXo.       ,ldKNXKkl,.      .;xXMMMXkdc''
';o0WMWX0XWXk:.      .,lddl'.          .;xNMMKkd;'                               Made by: Ҝ卂尺卂ㄒ乇Ҝ卂卄
,cxXWKocokOXWXk:.      ....      ''      .;xNNOxc'                                    Version: 1.0
;lkOl.  .;ok0XWXk:.            'lkxl'      .;xkko,
;lo;.      ,okOXNOl,         .'dXWKOxl'      .:kd,            ██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗ 
;lxOl.      .,okxl,.          .,lONWKOxl,.  ,odko,            ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║ 
,lxKW0l.       ,,.      ..      .,oONWKOxolxXXkxl'            ██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║
':oOWMWKl.            'ldo:.      .,oONWXNWMW0kd;'            ██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║
',lx0WMMW0l.        'oKWX0ko;       .;OMMMMMKkkl''            ██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║
'';ox0WMMMW0l.    'oKWN0kkd:.      .,dNMMMMXkko,''            ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝ 
''';ldONMMMMW0l''oKWN0kd:,.      .,dXWMMMWXOkl,'''
'''',cdkKWMMMMWXXWN0kd:.        ,dXWMMMWXOOkc'''''
'''''';ldOKNMMMMMMKxd,       .,dXWMMMWX0Oxl;''''''
'''''''';ldk0KNWMMMXd'     .,dXWMMNXK0kxl;''''''''
'''''''''';oxkkOXWMMWk,   .:0WMWN0kkOkl,''''''''''

"""+ R1)        
    print(R2+"++++++Generador de contraseñas seguras++++++"+R1)
    try:
        length = int(input(Y2+"Ingrese la longitud deseada de la contraseña (mínimo 8): "+R1))
        use_uppercase = input(Y2+"¿Incluir mayúsculas? (s/n): "+R1).lower() == 's'
        use_digits = input(Y2+"¿Incluir dígitos? (s/n): "+R1).lower() == 's'
        use_special_chars = input(Y2+"¿Incluir caracteres especiales? (s/n): "+R1).lower() == 's'

        password = generate_secure_password(length, use_uppercase, use_digits, use_special_chars)
        print(Y2+f"Contraseña generada: {R2}{password}{R1}")
    except ValueError as e:
        print(f"Error: {e}")

