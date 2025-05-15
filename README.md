## <h3 align="center"> Determinação da Curva de Equilíbrio Força-Deslocamento Usando o Método Arc-Length </h3>

**_Disciplina:_** Tópicos em Engenharia de Estruturas VII - Introdução à Análise Não Linear de Estruturas.

### **1. _Introdução_**

<p align="justify"> O estudo de estruturas submetidas a grandes deslocamentos requer métodos numéricos robustos capazes de rastrear corretamente o caminho de equilíbrio, mesmo quando há perda de rigidez ou mudanças de comportamento, como o pós-pico em estruturas instáveis. O método do comprimento de arco (Arc-Length) é amplamente utilizado na engenharia estrutural para esse fim, pois permite a obtenção da curva completa força-deslocamento, inclusive após o ponto de instabilidade (Crisfield, 1991).

Esta atividade tem como objetivo aplicar tal método para encontrar a relação entre o carregamento distribuído  e o deslocamento axial na extremidade de uma barra, mantendo parâmetros constantes como **_E0 = 100,000_**, **_S = 1_**, **_L = 100_**, **_n = 200_**, **_P = 1_**  e tolerância de **0,001**.</p>

### **2. _Metodologia e Formulação_**
#### **2.1 _Modelo do Problema_**

<p align="justify"> Considera-se uma barra submetida a um carregamento distribuído , com rigidez dependente dos deslocamentos. O sistema é resolvido numericamente com base em uma formulação não linear da rigidez, utilizando o método do comprimento de arco (Reddy, 2019).</p>
 
#### **2.2 _Método do Comprimento de Arco_**

<p align="justify"> O método Arc-Length impõe uma restrição adicional ao sistema:

**(Δu)<sup>T</sup>. (Δu) + α<sup>2</sup>Δλ<sup>2</sup> = Δs<sup>2</sup>**

onde:

- **Δu**: incremento de deslocamento

- **Δλ**: incremento do fator de carga

- **Δs**: incremento de arco (escala do passo)

- **α**: parâmetro de escalonamento

Esse método permite rastrear a curva equilíbrio mesmo após pontos de instabilidade ou mudança de trajetória, superando as limitações de métodos incrementais convencionais (Bathe, 1996).</p>

#### **2.3 _Parâmetros Utilizados_**

- Módulo de elasticidade: **_E0 = 100,000_**

- Área da seção: **_S = 1_**

- Comprimento da barra: **_L = 100_**

- Parâmetro de penalidade: **_n = 200_**

- Carga pontual: **_P = 1_**

- Tolerância de convergência: **_tol = 0.001_**

- Passo de arco: **Δs = 0.05**

- Número máximo de passos: 200

### **3 _Implementação Computacional_**
##### **3.1 _Trechos Principais do Código_**

```ruby
def calcular_matriz_rigidez(u1, u2, u3, E0, S, L, n):
    factor = (2 * E0 * S) / L
    term = n * 2 / L
    return factor * np.array([
        [1, 0, 0],
        [0, 2 - term * (u3 - u1), -1 + term * (u3 - u2)],
        [0, -1 + term * (u3 - u2), 1 - term * (u3 - u2)]
    ])
```

##### **3.2 _Algoritmo de Arc-Length_**

<p align="justify"> A cada passo, o sistema resolve:

**K(u) . Δu = λ . F**

E aplica a restrição de arco. Isso foi implementado em uma rotina de Newton-Raphson adaptada (Crisfield, 1991).</p>

