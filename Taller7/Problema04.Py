numerador  =  1
contadorDenominador  =  3
cadena  =  ""
operacion  =  0
cadena  =  f " { cadena } { numerador } "
operacion  =  operacion  +  numerador
i  =  1
para  i  en el  rango ( i , 8 ):
	si (( i  %  2 ) ==  0 ):
		cadena  =  f " { cadena } + { numerador } / { contadorDenominador } "
		operacion  =  operacion  +  numerador  /  contadorDenominador
	otra cosa :
		cadena  =  f " { cadena } - { numerador } / { contadorDenominador } "
		operacion  =  operacion  -  numerador  /  contadorDenominador
	contadorDenominador  =  contadorDenominador  +  2
cadena  =  f " { cadena } = { operacion : .3f } "
print ( f " { cadena } \ n " )
