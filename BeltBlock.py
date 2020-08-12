import binascii

class BeltBlock:

    def decode(input,key):
        pass

    def encode(input,key):
        block_size = 32
        count = len(input)/block_size
        [a,b,c,d] = [int(input[i:i+block_size-1],2) for i in range(0,len(input),block_size)]
        print("Blocks")
        print(a)
        print(b)
        print(c)
        print(d)
        key_count = len(key)/block_size
        [t1,t2,t3,t4,t5,t6,t7,t8] = [input[i:i+block_size-1] for i in range(0,len(key),block_size)]
        x = BeltBlock.__rotate__("12345678",7)
        key1 = list(binascii.unhexlify('E9DEE72C8F0C0FA62DDB49F46F73964706075316ED247A3739CBA38303A98BF6'))
        print(key1)
        return x


#
# inner function for byte replacement
#
#
    def __replace__(byte):
        x = byte[0]
        y = byte[1]
        array = [["B1","94","BA","C8","0A","08","F5","3B","36","6D","00","8E","58","4A","5D","E4"],
				 ["85","04","FA","9D","1B","B6","C7","AC","25","2E","72","C2","02","FD","CE","0D"],
				 ["5B","E3","D6","12","17","B9","61","81","FE","67","86","AD","71","6B","89","0B"],
				 ["5C","B0","C0","FF","33","C3","56","B8","35","C4","05","AE","D8","E0","7F","99"],
				 ["E1","2B","DC","1A","E2","82","57","EC","70","3F","CC","F0","95","EE","8D","F1"],
				 ["C1","AB","76","38","9F","E6","78","CA","F7","C6","F8","60","D5","BB","9C","4F"],
				 ["F3","3C","65","7B","63","7C","30","6A","DD","4E","A7","79","9E","B2","3D","31"],
				 ["3E","98","B5","6E","27","D3","BC","CF","59","1E","18","1F","4C","5A","B7","93"],
				 ["E9","DE","E7","2C","8F","0C","0F","A6","2D","DB","49","F4","6F","73","96","47"],
				 ["06","07","53","16","ED","24","7A","37","39","CB","A3","83","03","A9","8B","F6"],
				 ["92","BD","9B","1C","E5","D1","41","01","54","45","FB","C9","5E","4D","0E","F2"],
				 ["68","20","80","AA","22","7D","64","2F","26","87","F9","34","90","40","55","11"],
				 ["BE","32","97","13","43","FC","9A","48","A0","2A","88","5F","19","4B","09","A1"],
				 ["7E","CD","A4","D0","15","44","AF","8C","A5","84","50","BF","66","D2","E8","8A"],
				 ["A2","D7","46","52","42","A8","DF","B3","69","74","C5","51","EB","23","29","21"],
 				 ["D4","EF","D9","B4","3A","62","28","75","91","14","10","EA","77","6C","DA","1D"]]
        return array[int(x,16)][int(y,16)]

    def __rotate__(word,shift):
        print(word)
        block_size = 2
        count = len(word)/block_size
        [a,b,c,d] = [word[i:i+block_size] for i in range(0,len(word),block_size)]
        a = BeltBlock.__replace__(a)
        b = BeltBlock.__replace__(b)
        c = BeltBlock.__replace__(c)
        d = BeltBlock.__replace__(d)
        replaced = a + b + c + d
        arr = list(replaced)
        print(arr)
        arr = arr[1:len(arr)-shift] + arr[len(arr)-shift+1:len(arr)]
        print(arr)
        return replaced
		