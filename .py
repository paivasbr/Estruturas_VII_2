import numpy as np
import matplotlib.pyplot as plt

def calcular_matriz_rigidez(u1, u2, u3, E0, S, L, n):
    factor = (2 * E0 * S) / L
    term = n * 2 / L
    return factor * np.array([
        [1, 0, 0],
        [0, 2 - term * (u3 - u1), -1 + term * (u3 - u2)],
        [0, -1 + term * (u3 - u2), 1 - term * (u3 - u2)]
    ])

def resolver_arc_length(u_inicial, q_inicial, delta_s, max_iter, tol, E0, S, L, n, P):
    """
    Método arc-length: traça a curva de equilíbrio completa q x u
    """
    # Inicializações
    u = u_inicial.copy()
    q = q_inicial
    historia_q = []
    historia_u3 = []

    for passo in range(300):  # número arbitrário de passos
        # Iteração de Newton-Raphson com restrição de arco
        for it in range(max_iter):
            K = calcular_matriz_rigidez(*u, E0, S, L, n)

            # Derivada da força externa em relação a q
            dF_dq = np.array([0, L/2, L/4])

            # Resíduo do equilíbrio: R(u,q) = K(u) * u - F(q)
            Fq = np.array([0, q * L/2, q * L/4 + P])
            R = K @ u - Fq

            # Matriz aumentada e sistema linear (K modificada + equação de arco)
            dRdq = -dF_dq
            Ju = K
            Jq = dRdq.reshape((3, 1))

            # Monta o sistema aumentado:
            A = np.block([
                [Ju, Jq],
                [2 * u.reshape(1, -1), 2 * q]  # derivada da equação do arco
            ])

            b = np.concatenate([-R, [delta_s**2 - (np.linalg.norm(u)**2 + q**2)]])

            # Resolve o sistema
            try:
                solucao = np.linalg.solve(A, b)
            except np.linalg.LinAlgError:
                print("Sistema singular - encerrando")
                return historia_q, historia_u3

            delta_u = solucao[:3]
            delta_q = solucao[3]

            # Atualiza as variáveis
            u += delta_u
            q += delta_q

            # Critérios de convergência
            if np.linalg.norm(R) < tol and np.linalg.norm(delta_u) < tol:
                break

        # Armazena resultados
        historia_q.append(q)
        historia_u3.append(u[2])

        # Verificação de instabilidade numérica (opcional)
        if np.abs(q) > 100 or np.abs(u[2]) > 10:
            print("Solução divergente - encerrando")
            break

    return historia_q, historia_u3

def main():
    # Parâmetros fixos
    E0 = 100000
    S = 1.0
    L = 100
    n = 200
    P = 1.0
    tol = 1e-3
    max_iter = 50
    delta_s = 0.1  # comprimento do passo (ajuste fino aqui)

    # Condições iniciais
    u_inicial = np.zeros(3)
    q_inicial = 0.01  # pequeno valor para iniciar

    # Executa o arc-length
    lista_q, lista_u3 = resolver_arc_length(u_inicial, q_inicial, delta_s, max_iter, tol, E0, S, L, n, P)

    # Plot da curva de equilíbrio completa
    plt.figure(figsize=(8, 6))
    plt.plot(lista_u3, lista_q, marker='o', linestyle='-')
    plt.xlabel('Deslocamento na extremidade inferior u₃ (m)', fontsize=12)
    plt.ylabel('Carga distribuída q (N/m)', fontsize=12)
    plt.title('Curva de Equilíbrio Completa: Método Arc-Length', fontsize=14)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
