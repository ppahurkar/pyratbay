import matplotlib.pyplot as plt
plt.ion()

import pyratbay as pb
import pyratbay.constants as pc

# Kepler-11c mass and radius:
pressure, temp, q, species, radius = pb.run("/Users/parulpahurkar/Desktop/Pyratbay/run_demo/atmosphere_hydro_m.cfg")
pressure, temp, q, species, radius_g = pb.run("/Users/parulpahurkar/Desktop/Pyratbay/run_demo/atmosphere_hydro_g.cfg")

# Plot the results:
plt.figure(12, (6,5))
plt.clf()
ax = plt.subplot(111)
ax.semilogy(radius_g/pc.rearth, pressure/pc.bar, lw=2, c='navy', label='constant g')
ax.semilogy(radius/pc.rearth, pressure/pc.bar, lw=2, c='orange', label='g = g(p)')
ax.set_ylim(1e2, 1e-6)
ax.set_xlabel(r'Radius $(R_{\oplus})$', fontsize=12)
ax.set_ylabel('Pressure (bar)', fontsize=12)
ax.tick_params(labelsize=11)
ax.legend(loc='upper left', fontsize=12)
plt.tight_layout()
plt.savefig("radius_vs_pressure.pdf")
