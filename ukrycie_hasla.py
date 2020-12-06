if __name__ == '__main__':
    input_string = list(input())
    if len(input_string) > 2:
        for i in range(1,len(input_string)-1):
            input_string[i] = '*'
        print (''.join(input_string))
    else:
        print ("Haslo za krotkie")
