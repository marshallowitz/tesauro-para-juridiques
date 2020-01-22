import json
from difflib import SequenceMatcher
from difflib import get_close_matches
lexical = json.load(open("JUR.json"))

def tesauro(w):
    if w in lexical:
        return lexical[w]
    elif w.title() in lexical:
        return lexical[w.title()]
    elif w.upper() in lexical: 
        return lexical[w.upper()]    
    elif len(get_close_matches(w,lexical.keys())) > 0:
        answer = input("Você quis dizer %s ? Se sim, aperte S. Caso contrário, aperte N:"%get_close_matches(w,lexical.keys())[0])
        answer = answer.lower()
        if answer == "S" or answer == "sim" or answer == "s" or answer == "Sim" or answer == "SIM":
            return lexical[get_close_matches(w,lexical.keys())[0]]
        elif answer == "N" or answer == "não" or answer == "n" or answer == "Não" or answer == "NÃO" or answer == "Nao" or answer == "nao":
            return "Experimente outro termo:"
        else:
            return "Ooops... não entendemos se você quis digitar S para sim ou N para não:"
    else:
        print ("Este termo ainda não está disponível no Tesauro. Entre em contato com @SofiaMarshallowitz e envie tua sugestão!")

termo = input("Insira o termo aqui:")

termo = termo.lower()

print(tesauro(termo))
output = tesauro(termo)
