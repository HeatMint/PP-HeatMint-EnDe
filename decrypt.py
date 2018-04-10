# show information to developer while it's imported to any file
print "------------------------------------------------------------"
print "|       Welcome to use HeatMint en/decrypt service         |"
print "|   This is open sourced encryption method to make this    |"
print "|meaningless in real life. That means you can use this for |"
print "|fun or using this to prevent people close to you watching |"
print "|your communication secretly.                              |"
print "|Licence: None                                             |"
print "------------------------------------------------------------"


class Decrypt:
    def __init__(self, text, password=""):
        '''
        for functions that I didn't annotated here, see the encryption part for the same function name
        '''
        self.text = text
        self.password = password
        self.method = 5 % len(text)
        if len(password) <= 4 and len(password) >= 0:
            self.code = len(password)
        else:
            raise ValueError("Password should have a length from 0 to 4, revise your checker")

    @staticmethod
    def md5pass(password):
        import hashlib
        if len(password) > 1:
            after_code = hashlib.md5()
            after_code.update(password[1:])
            return after_code.hexdigest()
        else:
            return ""

    @staticmethod
    def flood(ori_list, num):
        if num < 0:
            return len(ori_list) + num
        else:
            return num

    @staticmethod
    def antigen(password):
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

    @classmethod
    def maindecrypt(cls, text, password=""):
        origin = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                  'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S',
                  'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', ' ', 'V', 'B', 'N', 'M']
        main_chaos = ['a', 'b', 'c', 'd', 'e', 'f', 'g', ' ', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                      's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                      'L', 'M',
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        password = Decrypt.antigen(password)
        if len(password) > 1:#when password have more than 1 integers
            if Decrypt.md5pass(password) == text[-32:]:
                encrypted = ""
                for alphabet in text[:-32]:
                    if alphabet in origin:
                        position = origin.index(alphabet)
                        if password != "":
                            position = origin.index(alphabet) - int(password[0]) - 1
                            position = Decrypt.flood(origin, position)
                        encrypted += main_chaos[position]
                    else:
                        encrypted += alphabet
                return encrypted
            else:
                return "Wrong password!"
        else:
            encrypted = ""
            if password == "":#When no password...
                for alphabet in text:
                    if alphabet in origin:
                        position = origin.index(alphabet)
                        encrypted += main_chaos[position]
                    else:
                        encrypted += alphabet
                return encrypted
            else:#when 1 int as password...
                for alphabet in text:
                    if alphabet in origin:
                        position = origin.index(alphabet)
                        if password != "":
                            position = origin.index(alphabet) - int(password[0]) - 1
                            position = Decrypt.flood(origin, position)
                        encrypted += main_chaos[position]
                    else:
                        encrypted += alphabet
                validate = 0
                for i in encrypted[-32:]:
                    if i == " ":
                        validate += 1
                if validate > 0:
                    return encrypted
                else:
                    return "Wrong password"

    @property
    def decrypted(self):
        text = self.maindecrypt(self.text, self.password)

        return text


if __name__ == "__main__":
    encrypted_text = Decrypt('GILrC289dff07669d7a23de0ef88d2f7129e7', "4234")
    print encrypted_text.decrypted
    print Decrypt.maindecrypt("STHqLp", "9")
    encrypted_text = Decrypt('LguecpujvuxpvaupmkxycpvaevpWkbpmejvpujtxWlvpauxu.289dff07669d7a23de0ef88d2f7129e7',
                             "1234")
    print encrypted_text.decrypted
    print Decrypt.antigen("0010"),Decrypt.antigen(Decrypt.antigen("0010"))
