def total_mechanical_energy(mass: float, height: float, speed: float):
    kin = speed**2*mass/2
    pot = mass*height*9.8
    return kin+pot