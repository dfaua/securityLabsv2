from aead import AEAD

cryptor = AEAD(AEAD.generate_key())

print("cryptor: ", cryptor)

l1 = ["Dasdsdfsdfsdfsdfdsfsfsdfsaslkdfjbvgfbhnjdkmqhbvefhcevfdumjynhtrgvfdsntgrnyil", "Fetydwfgytthgasdfasdfasfasdfasdfasdfasdfaddorov", "Security"]

ct = cryptor.encrypt(l1[0].encode(), l1[1].encode())

print("ct: ", ct)