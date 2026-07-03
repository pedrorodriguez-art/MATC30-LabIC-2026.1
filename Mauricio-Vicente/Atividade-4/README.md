# Atividade 4 - Organizando Contêineres de Bolas

## Descrição

Esta solução verifica se é possível organizar bolas de diferentes tipos em contêineres específicos usando apenas operações de troca (swap) um-para-um. Para que a organização seja bem-sucedida, ao final do processo, cada contêiner deve conter apenas bolas de um único tipo, e todas as bolas de um mesmo tipo devem estar agrupadas em um único contêiner.

## Parâmetros

| Parâmetro   | Tipo       | Descrição                                                                                   |
|-------------|------------|---------------------------------------------------------------------------------------------|
| `q`         | int        | Número de consultas ou casos de teste.                                                      |
| `n`         | int        | Número de contêineres e de tipos de bolas (tamanho da matriz n x n).                        |
| `container` | int[][]    | Matriz bidimensional onde `container[i][j]` é a quantidade de bolas do tipo `j` no contêiner `i`. |

## Retorno

O retorno será uma `string` retornando `"Possible"` se for possível organizar os contêineres de acordo com os requisitos, ou `"Impossible"` caso as capacidades e quantidades não sejam compatíveis.

## Restrições

- `1 <= q <= 10`
- `1 <= n <= 100`
- `0 <= containers[i][j] <= 10^9`

## Lógica

A solução baseia-se em um princípio lógico e matemático crucial: uma operação de troca (swap) de uma bola por outra **não altera a capacidade total** (o número de bolas) dentro de nenhum dos contêineres. 

Dessa forma, para que seja possível alocar todas as bolas de um determinado tipo dentro de um único contêiner, a **quantidade total de bolas daquele tipo** no jogo todo deve ser perfeitamente igual à **capacidade de armazenamento** de algum dos contêineres. 

O código resolve isso através dos seguintes passos utilizando a estrutura de Lista Encadeada (`List` e `No`):
1. O algoritmo percorre a matriz e calcula a capacidade total de cada contêiner (somando os valores de cada linha) e guarda esses valores na lista `capacidades`.
2. Em seguida, calcula a quantidade total existente de cada tipo de bola (somando os valores de cada coluna) e guarda na lista `totais_tipo`.
3. Através das funções customizadas `extrair_lista_ordenada` e `comparar_com`, as listas encadeadas são convertidas, ordenadas e comparadas de forma direta. Se os valores baterem exatamente, significa que temos contêineres do tamanho perfeito para cada tipo de bola, retornando a resposta de sucesso.
