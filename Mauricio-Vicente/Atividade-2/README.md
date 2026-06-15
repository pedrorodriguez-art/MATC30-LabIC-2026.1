# Atividade 2 - Soma de todos os elementos de um array

## Descrição

Essa função irá percorrer um array e retornar a soma de todos os itens dele.

## Parâmetros

| Parâmetro | Tipo | Descrição       |
|-----------|------|-----------------|
| `tamanho`       | int  | Tamanho do Array |
| `valor`       | int  | Valores que serão adicionados ao Array  |

## Retorno

O retorno será um `int` retornando a soma de todos os itens do array.

## Restrições

- `0 < tamanho `
- `valor < 1000`

## Lógica

A solução é dada através da criação de duas classes, uma para ser o Array (`List`) e a outra para ser cada elemento (`No`).
Através disso é possível usar essa lista de mão única (Só podemos acessar o próximo item) para somar cada um de seus elementos através da função `soma`, onde todo o array é percorrido e cada elemento é adicionado na variável local `i`.
Após essa varredura, é retornado o valor da soma dos elementos.
