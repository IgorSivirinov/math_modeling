import numpy
def grav_accel(phi=0, h=0):
    """
    :param phi: Широта места наблюдения
    :param h: высота над поверхностью Земли
    :return: Ускорение свободного подения
    """
    return 9.780318*(1 + 0.005302*(numpy.sin(phi)**2-0.00006*(numpy.sin(2*phi))**2)-0.000003086)
print(grav_accel(2,3))
def losing_weigh_function(mass=50,phi_0=54,phi_end=0,h_0=0,h_end=3000):
    """
    :param mass: Масса вашего тела
    :param phi_0: Широта с
    :param phi_end: Широта после
    :param h_0: Высота с
    :param h_end: Высота после
    :print: На сколько грамов изменится масса
    """
    P_0 = grav_accel(phi_0,h_0)*mass
    P_end = grav_accel(phi_end,h_end)*mass
    delta_P = (P_0-P_end)
    if delta_P > 0:
        print("Вы похудеете на",delta_P,'г.')
    elif delta_P < 0:
        print("Вы поправитесь на", delta_P*(-1),'г.')
    else:
        print('Ты - жиробас')