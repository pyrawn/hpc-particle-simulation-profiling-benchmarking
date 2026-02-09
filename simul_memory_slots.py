from random import uniform
from memory_profiler import profile


class Particle:
    __slots__ = ('x', 'y', 'ang_vel')

    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel


class ParticleSimulator:
    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt / timestep)
        for i in range(nsteps):
            for p in self.particles:
                norm = (p.x**2 + p.y**2)**0.5
                v_x = -p.y / norm
                v_y = p.x / norm

                d_x = timestep * p.ang_vel * v_x
                d_y = timestep * p.ang_vel * v_y

                p.x += d_x
                p.y += d_y


@profile
def benchmark_memory():
    particles = [Particle(uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0),
                          uniform(-1.0, 1.0))
                 for i in range(100000)]

    simulator = ParticleSimulator(particles)
    simulator.evolve(0.001)


if __name__ == '__main__':
    benchmark_memory()
