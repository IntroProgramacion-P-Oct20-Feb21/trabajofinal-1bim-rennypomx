contador  =  1
cadenaFinal  =  ""
mientras  contador  <=  4 :
    nombreEstudiante  =  input ( "Ingrese su nombre \ n >" )
    promedioCiclo  =  float ( input ( "Ingrese su promedio del ciclo \ n >" ))
    si  promedioCiclo  > =  7 :
        notaFinal  =  "Aprobado"
        cadenaFinal  =  "% s% s \ t % .2f \ t % s \ n "  % \
                      ( cadenaFinal , nombreEstudiante , promedioCiclo , notaFinal )
    otra cosa :
        notaFinal  =  "Reprobado"
        cadenaFinal  =  "% s% s \ t % .2f \ t % s \ n "  % \
                      ( cadenaFinal , nombreEstudiante , promedioCiclo , notaFinal )
    contador  =  contador  +  1
imprimir ( cadenaFinal )