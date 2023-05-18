import random
#Definir o banco de palavras
secretWord = ['F A R M A C I A','C A C H O R R O','P R I M A T A','G O R I L A','R I C H A R L I S O N']

#Criar a variavel para armazenar as letras ja digitadas que estao erradas.
triedLetters = ''

#Armazenando o indice aleatório, que sera usado tambem depois.
randomNumber= random.randint(0, len(secretWord)-1)

#usando o .split() para criar um vetor em todo lugar onde tem um espaço
choosenWord = secretWord[randomNumber].split()

#Vetor resposta, com base no tamanho da palavra
resultWord = ['_'] * len(choosenWord)

tentativas = 5

while True:
	  #Todo inicio de tentativa, define success para False
    #assim usando-o para definir se a letra tem ou nao na palavra
    
    success = False
    letter = str(input(f'\nVocê tem {tentativas} tentativas restantes...\nDigite uma letra: '))
		
    #o for olha todas as letras da palavra, buscando a letra inserida, se achar,
    #substitui no resultWord[i] por letter e define o success para True )  
    for i in range(len(choosenWord)) :
        
        if choosenWord[i] == letter:
            resultWord[i] = letter
            success = True
    if success == False:
        print(f'A letra {letter} não tem na palavra :( ')
        triedLetters += f' {letter},'
        tentativas -= 1

        if tentativas <=0:
            print(f'Você perdeu, a resposta era {secretWord[randomNumber]}')
            break
    else:
        print(f'{letter} esta correto!')
        if choosenWord == resultWord:
            print(f'Parabéns!\nVocê conseguiu! a palavra era {secretWord[randomNumber]} ')
            break
    print(f'{resultWord}\nLetras já tentadas: {triedLetters}')
