# implexCaixeiro

Instruções de Compilação e Execução
Este documento fornece instruções para compilar e executar o código fornecido para resolver o Problema do Caixeiro Viajante (TSP).

1.	Requisitos:
•	Python 3.x instalado no sistema.

2.	Compilação:
•	Não é necessário compilar o código, pois o Python é uma linguagem interpretada. O código será executado diretamente.

3.	Execução:
•	Abra um terminal ou prompt de comando.
•	Navegue até o diretório onde o código fonte está localizado.
•	Execute o seguinte comando para executar o programa:
python main.py 

4.	Configuração dos Parâmetros:
•	No arquivo "main.py", você pode ajustar os seguintes parâmetros de acordo com sua preferência:
•	Leitura das entradas: O código foi implementado para analisar todos os itens que possuem a extensão “.txt” ou seja não é necessário informar quais serão os arquivos de contendo os dados das cidades. Basta colocar os arquivos “.txt” na mesma pasta que o arquivo “main.py”
•	temperatura_inicial: Temperatura inicial para o algoritmo Simulated Annealing. Defina o valor desejado.
•	taxa_resfriamento: Taxa de resfriamento para o algoritmo Simulated Annealing. Defina o valor desejado.

5.	Saída:
•	Após a execução do programa, serão exibidos os melhores percursos encontrados pelos algoritmos Hill Climbing Iterativo e Simulated Annealing.
•	Além disso, o comprimento da rota para a solução do Hill Climbing Iterativo e Simulated Annealing será calculado e exibido.

6.	Observações:
•	Certifique-se de que o arquivo de entrada está no formato adequado. Verifique se as coordenadas das cidades estão corretamente formatadas no arquivo.
7.	Melhorias e Personalização:
•	O código fornecido pode ser melhorado e personalizado para atender a requisitos específicos.
•	Você pode implementar algoritmos adicionais, ajustar parâmetros, modificar a forma de cálculo da distância entre as cidades, entre outros.

8.	Limitações:
•	O código fornecido é uma implementação básica e pode não atingir o ótimo global para todas as instâncias do TSP.
•	Para obter melhores resultados, é recomendado explorar algoritmos mais avançados e realizar otimizações específicas para o problema.

9.	Referências:
•	As informações e conhecimentos abordados neste código foram baseados em conceitos gerais sobre o Problema do Caixeiro Viajante e algoritmos de busca heurística.
