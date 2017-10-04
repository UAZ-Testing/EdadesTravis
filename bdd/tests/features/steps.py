# -*- coding: utf-8 -*-

from lettuce import step
from lettuce import world
from edad import Edad
from cStringIO import StringIO

import sys

reload(sys)
sys.setdefaultencoding('utf8')


@step(u'Dado que ingreso la edad "([^"]*)"')
def dado_que_ingreso_la_edad_group1(step, edad):
    world.evaluador = Edad()
    try:
        world.edad = float(edad)
    except ValueError:
        world.edad = edad


@step(u'cuando realizo la evaluación')
def cuando_realizo_la_evaluacion(step):
    stdout_orig = sys.stdout
    sys.stdout = StringIO()
    world.evaluador.evaluar_edad(world.edad)
    world.output = sys.stdout.getvalue().replace('\n', '')
    sys.stdout.close()
    sys.stdout = stdout_orig


@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    assert esperado == world.output, 'El resultado esperado es "' + \
                                     esperado + '" y el obtenido es "' + \
                                     world.output + '"'
