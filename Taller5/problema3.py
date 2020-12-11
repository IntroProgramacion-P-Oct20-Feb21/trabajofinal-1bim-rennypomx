marca  =  input ( "Ingrese la marca del vehiculo \ n " )
origen  =  int ( input ( "Seleccione el numero del origen de su auto \ n "
                   f "1.Alemania \ n 2.Japon \ n 3.Italia \ n 4.USA \ n 5.Otro Pais \ n " ))
costo  =  float ( input ( "Ingrese el costo del vehiculo \ n " ))
si  origen  ==  1 :
    porcentaje  =  20
    impuesto  = ( porcentaje  *  costo ) /  100
    precioVenta  =  costo  +  impuesto
    print ( f "El impuesto por pagar es: { impuesto : .2f } y el precio de"
          f "venta es: { precioVenta : .2f } " )
si  origen  ==  2 :
    porcentaje  =  30
    impuesto  =  porcentaje  *  costo  /  100
    precioVenta  =  costo  +  impuesto
    print ( f "El impuesto por pagar es: { impuesto : .2f } y el precio de"
          f "venta es: { precioVenta : .2f } " )
si  origen  ==  3 :
    porcentaje  =  15
    impuesto  = ( porcentaje  *  costo ) /  100
    precioVenta  =  costo  +  impuesto
    print ( f "El impuesto por pagar es: { impuesto : .2f } y el precio de"
          f "venta es: { precioVenta : .2f } " )
si  origen  ==  4 :
    porcentaje  =  8
    impuesto  = ( porcentaje  *  costo ) /  100
    precioVenta  =  costo  +  impuesto
    print ( f "El impuesto por pagar es: { impuesto : .2f } y el precio de"
          f "venta es: { precioVenta : .2f } " )
si  origen  ==  5 :
    impuesto  =  0
    precioVenta  =  costo  +  impuesto
    print ( f "El impuesto por pagar es: { impuesto : .2f } y el precio de"
          f "venta es: { precioVenta : .2f } " )
