import codecs
word = input("Gimme a word or a phrase !ONLY ENGLISH!\n")
turn_it_arround = codecs.getencoder( "rot-13" ) #Elpizo na epitrepetai autos o tropos kathos den exei shmeiothei oti apagoreyetai h xrhsh toy
wordP  = turn_it_arround( word )[0]
print ("This is the result:")
print (wordP)
