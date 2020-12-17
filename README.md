# GradientDescent

## Exercício Extra 1 (implementação) - Obrigatório para a célula de otimização

Implementar o Algoritmo do Gradiente (referência: http://www.mat.ufmg.br/~taka/Download/OTEV-Vol2.pdf, página 63) na otimização do seguinte problema:

$$\min_\bar{x} f(x_1,x_2) = (x_1-1)^2 + 2x_2^2\\
-10 \leq x_1, x_2 \leq 10$$

Onde o ótimo é $x^* = [1, 0]^T$.

Requisitos da implementação:

- Inicialmente, plotar as curvas de nível da função objetivo;

- Plotar o valor de $f(\bar{x})$ ao longo das iterações;

- Ao final, marcar o ponto $\bar{x}^*$ no gráfico inicial;

- Ter uma função que retorne o valor de $f(\bar{x})$ e de $\nabla f(\bar{x})$ para um dado $\bar{x}$;

- Número máximo de iterações: 100;

- Precisão $\epsilon = 10^{-2}$;

- Critérios de parada:
  - Número máximo de iterações
  - $ ||\nabla f(\bar{x})|| \leq \epsilon$
  
- Ponto inicial: $\bar{x}_0 = [10, 10]^T$

Dicas:

- $ \nabla f(\bar{x}_k) = \begin{bmatrix} 
\frac{\partial f(x)}{\partial x_1} \\
\frac{\partial f(x)}{\partial x_2} \\
\end{bmatrix}$;

- $\bar{d}_k = -\frac{\nabla f(\bar{x}_k)}{||\nabla f(\bar{x}_k)||}$;

- $\alpha_k = \frac{d_1 - x_1d_1 - 2x_2d_2}{d_1^2+2d_2^2}$.
![alt text](https://github.com/thaleshsp2/GradientDescent/blob/master/fob.png?raw=true)



