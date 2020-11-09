teaches_subject(t1,maths).
teaches_subject(t2,dsa).
teaches_subject(t3,dld).
teaches_subject(t4,dsgt).
teaches_subject(t5,ppl).

has_subject(math_dept,maths).
has_subject(comp_dept,dsa).
has_subject(comp_dept,dld).
has_subject(comp_dept,dsgt).
has_subject(comp_dept,ppl).

has_student(comp_dept,s1).
has_student(comp_dept,s2).

has_teacher(D,T):-has_subject(D,S),teaches_subject(T,S).
studies(ST,SUB):-has_subject(D,SUB),has_student(D,ST).
is_teacher(T,S):-has_student(D,S),has_teacher(D,T).