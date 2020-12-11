cadenaReporte  =  ""
cadenaEdades  =  ""
bandera  =  Verdadero
sumaEdades  =  0
sumaEstaturas  =  0
contadorIteraciones  =  0
cadenaReporte  =  f " { cadenaReporte } Listado de Jugadores \ n "
mientras ( bandera ):
	nombreJugador  =  input ( "Ingrese el nombre del Jugador:" )
	posicionCampo  =  input ( "Ingrese la posición en el campo:" )
	edad  =  int ( input ( "Ingrese la edad del Jugador:" ))
	estatura  =  float ( input ( "Ingrese la estatura del jugador:" ))
	sumaEdades  =  sumaEdades  +  edad
	sumaEstaturas  =  sumaEstaturas  +  estatura
	contadorIteraciones  =  contadorIteraciones  +  1
	cadenaReporte  =  f " { cadenaReporte } { contadorIteraciones } .) { nombreJugador } " \
	f "- { posicionCampo } -, edad { edad } , estatura { estatura : .2f } \ n "
	cadenaEdades  =  f " { cadenaEdades } { edad } \ n "
	salir  =  input ( "Desea ingresar mas información; digite si \ n " \
		"Desea presentar el reporte; digite: no:" )
	salir  =  salir . inferior ()
	si ( salir  ! =  "si" ):
		bandera  =  Falso
si ( salir  ==  "no" ):
	promedioEdad  =  sumaEdades  /  contadorIteraciones
	promedioEstatura  =  sumaEstaturas / contadorIteraciones
	cadenaReporte  =  f " { cadenaReporte } Listado de edades \ n { cadenaEdades } " \
	f "Promedio de edades: { promedioEdad : .2f } \ n Promedio de estaturas:" \
	f " { promedioEstatura : .2f } \ n "
print ( f " { cadenaReporte } \ n " )