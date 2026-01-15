
import json
import random

f = open("words.json", encoding="utf8") #SERVE PARA ABRIR ARQUIVOS DENTRO DO SCRIPT

words = json.load(f) #CARREGAR OS DADOS DO JSON
choiceC = random.choice(list(words.keys())) #FORMA PARA ESCOLHER O DADO ALEATORIAMENTE, PEGANDO SÓ A CHAVE DO ESCOLHIDO COM O ".keys"
                                            #"list" para forçar a tranformação do String pra lista. OUTRO EX: int("1") = 1 passando de sring para int
print ("Olá, seja bem vindo!")
print("##################################")

nChoices = 5 #numero de chances
win = False

while nChoices > 0 and win is not True:
    print ("Dica: " + words[choiceC])
    answerUser = input("Data: DDMMAAAA\n")

    if len(answerUser) != 8: #len para medir o tamanho do array, quantos "i" será medido
        print("Erro na entrada. A resposta deve conter 8 digitos! (Digite Novamente)")
        continue

    if answerUser.isdigit(): #"isdigit" para verificar se o objeto é um numero
        check = []
        pontuation = 0
        for i in range(8):
            if answerUser[i] == choiceC[i]:
                check.append("✅")
                pontuation = pontuation + 1
            else:
                check.append("❌")
        
        print("Resposta: \n")
        print("|".join(check)) #JOIN -> Serve para colocar o objeto entre aspas, entre o espaçamento EX: SEM JOIN 1 2 3 4. COM JOIN 1|2|3|4
        print(" |".join(answerUser))
        print("#####################\n")

        if pontuation == 8:
            win = True
    else:
        print("Erro na entrada. A resposta deve ser uma data! (Digite Novamente)")
        continue
    nChoices = nChoices - 1

if win == True:
    print("Vitória!!!")
else:
    print("Derrota!!!")
    print("A resposta era: " + choiceC)