parent(david,sam).
parent(bella,sam).
parent(david,julie).
parent(bella,julie).

female(bella).
female(julie).

male(david).
male(sam).

father(X,Y):-parent(X,Y),male(X).
mother(X,Y):-parent(X,Y),female(X).
sister(X,Y):-parent(Z,X),parent(Z,Y),feamle(X).
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X).