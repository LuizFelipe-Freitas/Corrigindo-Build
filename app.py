import csv

def ler_preco(nome_produto):
    try:
        with (open('Dados.csv', 'r')) as f:  
            reader = csv.DictReader(f)
            for row in reader:
                if row['produto'].strip() == nome_produto.strip():
                    return float(row['preco'])
    except FileNotFoundError:
        return None
    return None

def calcular_desconto(preco):
    if preco is None:
        return None
    return preco * 0.9  # 10% discount

def main():
    produto = input("Digite o nome do produto: ")
    preco = ler_preco(produto)
    desconto = calcular_desconto(preco)
    if desconto is not None:
        print(f"Preço com 10% de desconto: R$ {desconto:.2f}")
    else:
        print("Produto não encontrado ou erro no arquivo.")

if __name__ == "__main__":
    main()
