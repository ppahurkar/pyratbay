import matplotlib.pyplot as plt
plt.ion()

import pyratbay as pb
import pyratbay.plots as pp

# Generate a uniform and a thermochemical-equilibrium atmospheric model:
pressure, temp, vmr_tea, species_tea, radius = pb.run("/Users/parulpahurkar/Desktop/Pyratbay/run_demo/atmosphere_tea.cfg")
pressure, temp, vmr_uni, species_uni, radius = pb.run("/Users/parulpahurkar/Desktop/Pyratbay/run_demo/atmosphere_uniform.cfg")

# Plot the results:
plt.figure(12, (6,5))
plt.clf()
ax = plt.subplot(211)
ax1 = pp.abundance(
    vmr_tea, pressure, species_tea,
    colors='default', xlim=[1e-11, 10.0], legend_fs=0, ax=ax,
)
ax = plt.subplot(212)
ax2 = pp.abundance(
    vmr_uni, pressure, species_uni,
    colors='default', xlim=[1e-11, 10.0], legend_fs=8, ax=ax,
)
plt.tight_layout()
plt.savefig("volume_vs_pressure.pdf")