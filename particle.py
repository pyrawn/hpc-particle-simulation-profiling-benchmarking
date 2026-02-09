import matplotlib.pyplot as plt
from matplotlib import animation

class Particle:
    def __init__(self, x,y,v): # Constructor for Particle
        self.x = x
        self.y = y
        self.v = v  

class ParticleSimulator: 
    def __init__(self, particles): # Constructor for Simulation Class
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.00001
        nsteps = int(dt/timestep)
        for i in range(nsteps):
            for p in self.particles:
                
                # Calculate the distance from the origin
                r = (p.x**2 + p.y**2)**0.5
                sin_theta = p.y/r
                cos_theta = p.x/r

                # Calculate displacement in x and y directions
                dx = -timestep * p.v * sin_theta
                dy = timestep * p.v * cos_theta
                p.x += dx
                p.y += dy

def visualize(simulator):
    X=[p.x for p in simulator.particles]
    Y=[p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')
    
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    def __init__():
        line.set_data([], [])
        return line,
    
    def animate(i):
        simulator.evolve(0.01)
        X=[p.x for p in simulator.particles]
        Y=[p.y for p in simulator.particles]
        line.set_data(X, Y)
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func=__init__, frames=200, interval=20, blit=True)
    plt.show()

def test_visualize():
    particles = [Particle(0.3,0.5,5),Particle(0.0,0.5,-5), Particle(-0.1,0.4,15)]
    simulator = ParticleSimulator(particles)
    visualize(simulator)

if __name__ == "__main__":
    test_visualize()