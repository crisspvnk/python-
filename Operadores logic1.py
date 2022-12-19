'''
Los operadores logicos se caracterizan por construir expresiones logicas, estas vienen siendo
And, Or y Not (de Negación)
And: es parecida a una multiplicacion logica (true tiene que concidir con él mismo, de lo contrario 
sera false)
Or: es como una suma logica(cualquiera que concida con true sera true, si es false con false sera false)
Not: si niegas una expresión, esa expresion cambia de verdadero a falso, ejemplo: not(true)=false
'''
a = 10
b = 12
c = 13
d = 10
((a>b) or (a<c)) and ((a==c) or (a>=b))