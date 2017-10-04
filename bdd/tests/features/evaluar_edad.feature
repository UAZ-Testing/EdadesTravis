Feature: Evaluación de edad
  Como usuario del programa
  deseo evaluar la edad ingresada
  con la finalidad de obtener la etapa de su vida

  Scenario: Evaluar edad 0
  Dado que ingreso la edad "0"
  cuando realizo la evaluación
  entonces obtengo el resultado "eres un recién nacido"

  Scenario: Evaluar edad -1
  Dado que ingreso la edad "-1"
  cuando realizo la evaluación
  entonces obtengo el resultado "no existes"

  Scenario: Evaluar edad 12
  Dado que ingreso la edad "12"
  cuando realizo la evaluación
  entonces obtengo el resultado "eres niño"

  Scenario: Evaluar edad 17
  Dado que ingreso la edad "17"
  cuando realizo la evaluación
  entonces obtengo el resultado "eres adolescente"

  Scenario: Evaluar edad 64
  Dado que ingreso la edad "64"
  cuando realizo la evaluación
  entonces obtengo el resultado "eres adulto"

  Scenario: Evaluar edad 119
  Dado que ingreso la edad "119"
  cuando realizo la evaluación
  entonces obtengo el resultado "eres adulto mayor"

  Scenario: Evaluar edad 121
  Dado que ingreso la edad "121"
  cuando realizo la evaluación
  entonces obtengo el resultado "eres Mumm-Ra"

  Scenario: Evaluar edad 120
  Dado que ingreso la edad "120"
  cuando realizo la evaluación
  entonces obtengo el resultado "eres Mumm-Ra"

  Scenario: Evaluar edad u
  Dado que ingreso la edad "u"
  cuando realizo la evaluación
  entonces obtengo el resultado "debes insertar un número"
