#pip install nltk numpy tensorflow

#from chatbot import ChatBot --> isso está comentado pois estamos rodando usando o Google Colab
myChatBot = ChatBot()


#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o modelo
myChatBot.createModel()




print("Bem vindo ao Chatbot")


pergunta = input("como posso te ajudar? ")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")


while (intencao[0]['intent']!="despedida"):
    pergunta = input("posso lhe ajudar com algo a mais?")
    resposta, intencao = myChatBot.chatbot_response(pergunta)
    print(resposta + "   [" + intencao[0]['intent'] + "]")

print("Foi um prazer atendê-lo")
