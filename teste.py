import time

def efeito_digitacao(texto, intervalo=0.05):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(intervalo)
    print()  # Pula linha no final

efeito_digitacao("Olá, este texto será digitado aos poucos!")