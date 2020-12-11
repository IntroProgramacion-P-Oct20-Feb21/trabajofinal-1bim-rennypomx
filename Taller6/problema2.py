cadenaFinal  =  ""
contador  =  1
denominador  =  19
mientras  contador  <=  6 :
    si ( contador  %  2 ) ==  0 :
        denominador  =  denominador  +  10
        cadenaFinal  =  "% s% d /% d"  % ( cadenaFinal , contador , denominador )
    otra cosa :
        denominador  =  denominador  -  9
        cadenaFinal  =  "% s% d /% d"  % ( cadenaFinal , contador , denominador )
    contador  =  contador  +  1
print ( f " { cadenaFinal } " )