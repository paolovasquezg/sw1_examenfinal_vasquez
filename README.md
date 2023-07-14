# sw1_examenfinal_vasquez

## Evaluación: Examen Final Ingeniería Software I
## Alumno: Paolo Vásquez Grahammer

### Pregunta 03

Se requiere realizar un cambio en el software para que soporte un valor máximo de 200 soles a
transferir por día.

**1. Qué cambiaría en el código (Clases / Métodos) - No implementación.**

Sencillamente agregaría nuevos atributos en la clase Cuenta, que sería ***valor_transf_dia*** y otro **dia_actual**, que me permitirían validar lo que nos pide el enunciado. La primera variable iria acumulando los valores transferidos en el día, y la segunda tendría el dia actual, por si es un nuevo día, se validaría que ya se pueden comenzar nuevamente a realizar transferencias, sin pasarse del límite indicado. Estos valores serían utilizados más que nada en las función de pago, validando si es que el usuario puede efectivamente realizar transacciones dado la restricciones. Algo importante a agregar es que la variable ***dia_actual***, se actualiza cuando se valida mediante ***datetime.now()*** que son diferentes. Eso sería todo.

**2. Nuevos casos de prueba a adicionar.**

Básicamente agregaríamos casos de prueba en los que haríamos transacciones seguidas, viendo si sigue realizando las transacciones a pesar de haber superado el límite diarío. Posiblemente de manera más simple, también transferir directamente un monto enorme, viendo si se cumple la restricción. De esta forma lo validaría.

**3. Cuánto riesgo hay de “romper” lo que ya funciona?**

Básicamente el riesgo vendría si verdaderamente la actualización de ***dia_actual*** se hace manera correcta. Podría existir error y este no se actualiza al empezar un nuevo día, entonces aunque ello ha pasado, el usuario sigue siendo incapaz de realizar transacciones. Ello sería el principal, y posiblemente el único existente, pero digamos que no es precisamente muy alto, ya que la actualización se puede hacer y validar de forma relativamente sencilla. Ello si se tiene en cuenta como hacerlo.


## Anexos

### Testing ~ Pregunta 02

