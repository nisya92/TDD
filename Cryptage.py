import string

class Cryptage():
    def crypt(message):
        caracteres = string.ascii_letters + string.punctuation + string.digits + " "
        message_crypte = ""

        for lettre in message:
            if lettre in caracteres:
                index = caracteres.index(lettre)
                lettre_cryptee = caracteres[(index + 1) % len(caracteres)]
                message_crypte += lettre_cryptee
            else:
                message_crypte += lettre

        return message_crypte