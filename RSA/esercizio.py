
modulus= "00d36eac78542885369046525b7164516806f4e37dcb20208951ef4fffc75e9815d376d41fcbc1b8bb312b93d9d61a98eb06516042a1231f19d1a0d2e9cfb3e5258eb21cdc74cf35fbcf0554a9b252ef5b96290f8668869ca348bd714d7698ef5a02efd4e5f6a8fed6279f77cfb91e17bdd0a749b000d58353b8ff10ed2df02025b9e593745c11976cc709523a1626e171bf26d178e55f88c20cf2b7f49d2e5993c99c52466cf188c6f9921907ef3ae713559233338a62f73bb2b8fbe2009695e46c6ca2eb03fa36c0a93659f6c8c70a65b616e09ad434e75bd5f333458375adb42af8ef8c2de4cb446abad0b9416515a40b4337d483bc6357f59a0ac74380f4a1"
publicExponent= "3"#
privateExponent= "08cf472fae2c5ae24602ee1924b98364559f897a932156b06369f8aaa84e9bab937a48d6a87d67b27761d0d3be411bb47598b9581c0c214bbe115e1f1352298c3b476bde84ddf79528a038dc676e1f4e7b970b50445af131785d3a0de4f109f91574a8deea470a9e41a6a4fdfd0beba7e8b1a3120008e578d25ff609e1ea0156d455bb2a45f0e5b384bd7ba6e80b9701b1bc33fe66e0656dfbddcb867864c99f4652150f8f0d43ed4bfd944ce18a442d7d75db5e0139788129e1b343dcfe1371fb8b0bf4239715da8c46c642b92c5cc79d9070cb59706c2faad1c94296752610050222c21be8c9cf129953321341faa7a0cce33b5c2fac79d6acc96bf7a2b58b"

#RSA NON LAVORA CON LETTERE MA SOLO CON NUMERI INTERI

def clean_hex_to_int(clean_h:str) -> int:

    return int(clean_h,16)

# converto il numero hex in int
n =clean_hex_to_int(modulus)
e =publicExponent
d =clean_hex_to_int(privateExponent)

print("n=",n)
print("e=",n)
print("d=",n)

msg = "CIAO"
esponente_bytes = len(msg)
print("esp_bytes=",esponente_bytes)

# converto il messaggio in numero intero

msg_bytes = list(msg.encode())
print("msg_bytes=",msg_bytes)

# il messaggio all'inizio non c'è quindi è 0
M = 0

for b in msg_bytes:
    M = M*256+b
    M+=1

print("messaggio cifrato=", M)

bytes_list = []

while M > 0:
    b=M%256
    bytes_list.insert(0,b)
    M=M//256

msg_back= bytes(bytes_list).decode()

print("messaggio decifrato=", msg_back)


# m = 1234567890

# cifrato = pow(m, e, n)

# decifra= pow(cifrato, d, n)

# numero = 8735

