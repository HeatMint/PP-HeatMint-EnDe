# show information to developer while it's imported to any file
print "------------------------------------------------------------"
print "|       Welcome to use HeatMint en/decrypt service         |"
print "|   This is open sourced encryption method to make this    |"
print "|meaningless in real life. That means you can use this for |"
print "|fun or using this to prevent people close to you watching |"
print "|your communication secretly.                              |"
print "|Licence: None                                             |"
print "------------------------------------------------------------"


class Encrypt:
    def __init__(self, text, password=""):
        self.text = text
        self.password = password
        self.method = 5 % len(text)
        if len(password) <= 4 and len(password) >= 0:
            self.code = len(password)
        else:
            raise ValueError("Password should have a length from 0 to 4, revise your checker")

    @staticmethod
    def antigen(password):
        #Generate the decryption password
        if password == "":
            return ""
        if password == "0000":
            return "0000"
        length = len(str(password))
        num = "1" + length * "0"
        res = str(int(num) - int(password))
        while len(res) < length:
            res = "0" + res
        return res

    @staticmethod
    def md5pass(password):
        #called in encryption
        import hashlib
        if len(password) > 1:
            after_code = hashlib.md5()
            after_code.update(password[1:])
            return after_code.hexdigest()
        else:
            return ""

    @staticmethod
    def flood(ori_list, num):
        #to prevent list index out of range
        if num > len(ori_list) - 1:
            return num - len(ori_list)
        else:
            return num

    @classmethod
    def mainencrypt(cls, text, password=""):
        origin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', ' ', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                  't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        main_chaos = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                      'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S',
                      'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', ' ', 'V', 'B', 'N', 'M']
        encrypted = ""
        for alphabet in text:
            if alphabet in origin:
                position = origin.index(alphabet)
                if password != "":
                    position = origin.index(alphabet) + int(password[0]) + 1
                    position = Encrypt.flood(origin, position)
                encrypted += main_chaos[position]
            else:
                encrypted += alphabet
        encrypted += Encrypt.md5pass(password)
        return encrypted

    @property
    def encrypted(self):
        text = self.mainencrypt(self.text, self.password)

        return text


if __name__ == "__main__":
    encrypted_text = Encrypt('IBMYP', "4234")
    print encrypted_text.encrypted
    print Encrypt.mainencrypt('IBMYP')
    print Encrypt.mainencrypt('IBMYP ', "1")
