# -*- coding: utf-8 -*-

import mi_modulo
import Cliente

print(mi_modulo.crea_listado(['a','b','c'],3))
C1=Cliente.Cliente('ISABEL','Vitoria','9898989','@@')
print(C1.nombre + '-' + C1.direccion + '-' +C1.telefono + '-' +C1.email)
C1=Cliente.Cliente('ISABELlllll','Vitoriaaaaaaa','98989899999999999','@@.............')
print(C1.nombre + '-' + C1.direccion + '-' +C1.telefono + '-' +C1.email)