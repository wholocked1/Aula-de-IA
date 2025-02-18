progenitor(pietro1,joao).
progenitor(pietro1,clara).
progenitor(pietro1,francisco).
progenitor(pietro1,valeria).
progenitor(pietro1,ana).
progenitor(antonita,joao).
progenitor(antonita,clara).
progenitor(antonita,francisco).
progenitor(antonita,valeria).
progenitor(antonita,ana).
progenitor(ana,helena).
progenitor(ana,joana).
progenitor(joao,mario).
progenitor(helena,carlos).
progenitor(mario,carlos).
progenitor(clara,pietro2).
progenitor(clara,enzo).
progenitor(jacynto,francisca).
progenitor(jacynto,antonia).
progenitor(claudia,francisca).
progenitor(claudia,antonia).
progenitor(luzia,jacynto).
progenitor(pablo,jacynto).
relacao(pietro1,antonia).
relacao(mario,helena).
relacao(francisco, fabiana).
relacao(enzo,antonia).
relacao(pietro2,francisca).
relacao(pablo,luzia).
relacao(jacynto,claudia).
sexo(pietro1,masculino).
sexo(pietro2,masculino).
sexo(joao,masculino).
sexo(francisco,masculino).
sexo(mario,masculino).
sexo(carlos,masculino).
sexo(enzo,masculino).
sexo(jacynto,masculino).
sexo(pablo,masculino).
sexo(antonita,feminino).
sexo(clara,feminino).
sexo(valeria,feminino).
sexo(ana,feminino).
sexo(helena,feminino).
sexo(joana,feminino).
sexo(fabiana,feminino).
sexo(claudia,feminino).
sexo(luzia,feminino).
sexo(francisca,feminino).
sexo(antonia,feminino).

irma(X,Y):-progenitor(A,X),
    progenitor(A,Y),
    X\==Y,
    sexo(X,feminino).

irmao(X,Y):-progenitor(A,X),
    progenitor(A,Y),
    X\==Y,
    sexo(X,masculino).

descendente(X,Y):-progenitor(X,Y).

ascendente(X,Y):-progenitor(Y,X).

avo(X,Y):-progenitor(X,A),
    progenitor(A,Y),
    sexo(X,masculino).
avoh(X,Y):-progenitor(X,A),
    progenitor(A,Y),
    sexo(X,feminino).

tio(X,Y):-irmao(X,A),
    ascendente(Y,A). %erro

tia(X,Y):-irma(X,A),
    ascendente(Y,A). %erro

primo(X,Y):-descendente(A,X),
    irmao(A,B),
    descendente(B,Y),
    sexo(X,masculino).

primo(X,Y):-descendente(A,X),
    irma(A,B),
    descendente(B,Y),
    sexo(X,masculino). %erro

prima(X,Y):-descendente(A,X),
    irmao(A,B),
    descendente(B,Y),
    sexo(X,feminino). %erro

prima(X,Y):-descendente(A,X),
    irma(A,B),
    descendente(B,Y),
    sexo(X,feminino).
