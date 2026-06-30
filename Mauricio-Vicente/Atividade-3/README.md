# Atividade 3 - Próxima ordem lexicográfica

## Descrição

Essa função irá percorrer uma lista encadeada de palavras e retornar, para cada uma delas, a menor string lexicograficamente maior possível. Caso não seja possível formar uma palavra maior, ela retornará que não há resposta.

## Parâmetros

| Parâmetro | Tipo | Descrição       |
|-----------|------|-----------------|
| `T`       | int  | Número de casos de teste (Tamanho da lista) |
| `w`       | string | Palavras que serão adicionadas à Lista |

## Retorno

O retorno será uma `string` retornando a nova palavra reorganizada ou `"no answer"` caso a palavra já esteja na sua maior combinação possível.

## Restrições

- `1 <= T <= 100000`
- `1 <= tamanho de w <= 100`
- `w` conterá apenas letras no intervalo ascii [a..z].

## Lógica

A solução é dada através da criação de duas classes, uma para ser a Lista (`List`) e a outra para ser cada elemento (`No`).
Através disso é possível usar essa lista de mão única (Só podemos acessar o próximo item) para avaliar cada um de seus elementos através da função `lexicografica`, onde todo o array encadeado é percorrido.
Em cada nó, a string é convertida em uma lista de caracteres e lida de trás para frente para encontrar o ponto exato de troca. Após alterar a posição das letras e inverter o restante da palavra para garantir a menor ordem possível, é retornado o valor final no terminal.
