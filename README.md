## <h3 align="center"> Determinação da Curva de Equilíbrio Força-Deslocamento Usando o Método Arc-Length </h3>

**_Disciplina:_** Tópicos em Engenharia de Estruturas VII - Introdução à Análise Não Linear de Estruturas.

### **_Introdução_**

<p align="justify"> O estudo de estruturas submetidas a grandes deslocamentos requer métodos numéricos robustos capazes de rastrear corretamente o caminho de equilíbrio, mesmo quando há perda de rigidez ou mudanças de comportamento, como o pós-pico em estruturas instáveis. O método do comprimento de arco (Arc-Length) é amplamente utilizado na engenharia estrutural para esse fim, pois permite a obtenção da curva completa força-deslocamento, inclusive após o ponto de instabilidade (Crisfield, 1991).

Esta atividade tem como objetivo aplicar tal método para encontrar a relação entre o carregamento distribuído  e o deslocamento axial na extremidade de uma barra, mantendo parâmetros constantes como **_E0 = 100,000_**, **_S = 1_**, **_L = 100_**, **_n = 200_**, **_P = 1_**  e tolerância de **0,001**.</p>

### **_Metodologia e Formulação_**
#### **2.1 _Modelo do Problema_**

<p align="justify"> Considera-se uma barra submetida a um carregamento distribuído , com rigidez dependente dos deslocamentos. O sistema é resolvido numericamente com base em uma formulação não linear da rigidez, utilizando o método do comprimento de arco (Reddy, 2019).</p>
 
#### **2.2 _Método do Comprimento de Arco_**

<p align="justify"> O método Arc-Length impõe uma restrição adicional ao sistema:

onde:

- : incremento de deslocamento

- : incremento do fator de carga

- : incremento de arco (escala do passo)

- : parâmetro de escalonamento

Esse método permite rastrear a curva equilíbrio mesmo após pontos de instabilidade ou mudança de trajetória, superando as limitações de métodos incrementais convencionais (Bathe, 1996).</p>

#### **2.3 _Parâmetros Utilizados_**

- Módulo de elasticidade: 

- Área da seção: 

- Comprimento da barra: 

- Parâmetro de penalidade: 

- Carga pontual: 

- Tolerância de convergência: 

- Passo de arco: 

- Número máximo de passos: 200
