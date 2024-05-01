import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

def ler_arquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        return file.read()

def resumo(texto):
    response = client.completions.create(
        model="babbage-002",
        prompt=f"Resuma o seguinte texto: {texto}",
        temperature=0.7,
        max_tokens=2048,
        n=1,
        stop=None
    )
    return response.choices[0].text

def main():
    try:
        arquivo = 'guiadosporamor.txt'
        texto = ler_arquivo(arquivo)
        print(resumo(texto))
    except ValueError:
        print("Ops! Algo deu errado")

main()