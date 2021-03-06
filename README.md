Exercício Extra 1 (implementação) - Obrigatório para a célula de otimização

Implementação no Google Colab: https://colab.research.google.com/drive/1s968FRea738PlnHrwgukpwjE9G3X--vi#scrollTo=S67lXuvl78tQ

Implementar o Algoritmo do Gradiente (referência: http://www.mat.ufmg.br/~taka/Download/OTEV-Vol2.pdf, página 63) na otimização do seguinte problema:

minx¯f(x1,x2)=(x1−1)2+2x22−10≤x1,x2≤10

Onde o ótimo é x∗=[1,0]T.

Requisitos da implementação:

    Inicialmente, plotar as curvas de nível da função objetivo;
![alt text](https://github.com/thaleshsp2/GradientDescent/blob/master/fob.png?raw=true)

    Plotar o valor de f(x¯) ao longo das iterações;
![alt text](https://github.com/thaleshsp2/GradientDescent/blob/master/iterations.png?raw=true)

    Ao final, marcar o ponto x¯∗ no gráfico inicial;
![alt text](https://github.com/thaleshsp2/GradientDescent/blob/master/min.png?raw=true)

    Ter uma função que retorne o valor de f(x¯) e de ∇f(x¯) para um dado x¯;

    Número máximo de iterações: 100;

    Precisão ϵ=10−2;

    Critérios de parada:
        Número máximo de iterações
        ||∇f(x¯)||≤ϵ

    Ponto inicial: x¯0=[10,10]T

Dicas:

    ∇f(x¯k)=⎡⎣⎢∂f(x)∂x1∂f(x)∂x2⎤⎦⎥;

    d¯k=−∇f(x¯k)||∇f(x¯k)||;

    αk=d1−x1d1−2x2d2d21+2d22.




