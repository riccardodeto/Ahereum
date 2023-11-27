from cryptography.fernet import Fernet


class Contract():
    def __int__(self, idMission, idDrone, coordinates, isDeleted=False):
        self.idMission = idMission
        self.idDrone = idDrone
        self.coordinates = coordinates
        self.isDeleted = isDeleted
        self.keys = None

    def addTask(self):
        "NELLA SEGUENTE FUNZIONE, INIZIALIZZO ID MISSIONE, ID DRONE E LE COORDINATE, ASSOCIANDOLE ALLA VARIABILE SELF"
        "IN MANIERA TALE DA POTER ESSERE PRELEVATE GLOBALMENTE NELLA FUNZIONE"
        self.idMission = 1
        self.idDrone = 123
        self.coordinates = ["1.1, 1.1", "2.2, 2.2", "3.3, 3.3"]
        "RICHIAMO LA FUNZIONE CYPHER PER CIFRARE I MESSAGGI"
        enc_mess = self.cypher()
        "CREO IL BLOCCO E LO RESTITUISCO"
        block = [self.idMission, self.idDrone, enc_mess]
        return block

    def getTask(self):
        "NELLA SEGUENTE FUNZIONE RICHIAMO I MESSAGGI DECIFRATI"
        dec_mess = self.dechiper()
        "CREO IL BLOCCO E LO RESTITUISCO"
        block = [self.idMission, self.idDrone, dec_mess]
        return block

    def cypher(self):
        "NELLA SEGUENTE FUNZIONE CREO UN DIZIONARIO DI CHIAVI E UN DIZIONARIO DI COORDINATE CIFRATE"
        "N.B.: IN OTTICA REALE, LE CHIAVI NON SONO SALVATE"
        keys = {}
        enc_coordinates = {}
        "MEDIANTE LA LIBRERIA FERNET CREO TANTE CHIAVI QUANTE SONO LE COORDINATE E LE SALVO NEL DIZIONARIO NELLA FORMA"
        "{ key0: chiave, key1: chiave, ... }"
        for i in range(len(self.coordinates)):
            keys['key'+str(i)] = Fernet.generate_key()
        "SCORRO LE CHIAVI E CON LA CHIAVE I-ESIMA CIFRO LA COORDINATA I-ESIMA"
        for i in range(len(keys)):
            fernet = Fernet(keys['key'+str(i)])
            message = self.coordinates[i]
            enc_coord = fernet.encrypt(message.encode())
            enc_coordinates['enc_coord'+str(i)] = enc_coord
        "SALVO LE CHIAVI NELLA VARIABILE SELF E TORNO LE COORDINATE CIFRATE"
        self.keys = keys
        return enc_coordinates

    def dechiper(self):
        "NELLA SEGUENTE FUNZIONE CREO UN DIZIONARIO DI MESSAGGI DECODIFICATI"
        dec_messages = {}
        "SALVO IN ENC_COORDINATES I MESSAGGI CIFRATI"
        enc_coordinates = self.cypher()
        "PRELEVO LE CHIAVI DA SELF E LE SALVO NELLA VARIABILE KEYS"
        keys = self.keys
        "SCORRO LE SINGOLE COORDINATE E ASSOCIO A fernet LA SINGOLA CHIAVE CHE STO PRELEVANDO"
        for i in range(len(self.coordinates)):
            fernet = Fernet(keys['key'+str(i)])
            print('-----------------------------------------------------')
            "PROVO A DECIFRARE IL J-ESIMO MESSAGGIO CON LA I-ESIMA CHIAVE. SE LA DECIFRATURA VA A BUON FINE, SALVO IL"
            "MESSAGGIO ALL'INTERNO DEL DIZIONARIO DI MESSAGGI DECODIFICATI. IN ALTERNATIVA, ESEGUO UN'OPERAZIONE"
            "CASUALE, COME A = 0, SE SI VERIFICA UN'ECCEZIONE NEL TENTATIVO DI DECIFRATURA."
            "N.B.: AL POSTO DI A=0 SI PUO' INSERIRE UNA QUALSIASI OPERAZIONE"
            for j in range(len(enc_coordinates)):
                try:
                    dec_mess = fernet.decrypt(enc_coordinates['enc_coord'+str(j)]).decode()
                    dec_messages['dec_mess' + str(i)] = dec_mess
                    print(dec_messages)
                except:
                    print(f"La chiave {i} non decifra la coordinata {j}")
                    a = 0
        return dec_messages



