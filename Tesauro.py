import json
from difflib import SequenceMatcher
from difflib import get_close_matches
lexical = json.load(open("JUR.json"))

def tesauro(w):
    '''Procura pelo termo w ou similares no dicionario lexical e retorna um
    significado caso encontrado. Se o termo desejado não existir, retorna None.
    '''
    if w in lexical:
        return w, lexical[w][0]
    if w.title() in lexical:
        return w, lexical[w.title()][0]
    if w.upper() in lexical:
        return w, lexical[w.upper()][0]

    close_matches = get_close_matches(w, lexical.keys())
    while len(close_matches) > 0:
        print("Você quis dizer algum destes termos?")
        for i,m in enumerate(close_matches):
            print(f'  {i+1} - {m}')
        print(f'  {i+2} - Nenhum destes!')

        answer = input('Digite um novo termo para buscar de novo, ou o número da opção desejada (1): ')
        if answer == '':
            answer = 1
        try:
            answer = int(answer)
            if answer in range(1, len(close_matches)+1):
                w = close_matches[answer-1]
                return w, lexical[close_matches[int(answer)-1]][0]
            elif answer == len(close_matches)+1:
                break
        except:
            w = answer.lower()
            close_matches = get_close_matches(w, lexical.keys())
    return None

termo = input("Insira o termo aqui: ").lower()

output = tesauro(termo)
if output is None:
    print("Este termo ainda não está disponível no Tesauro. Entre em contato com @SofiaMarshallowitz e envie tua sugestão!")
else:
    print(output[0], '-', output[1])
