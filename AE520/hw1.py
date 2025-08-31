import numpy as np
import matplotlib.pyplot as plt
import niceplots

################## Problem 1 ##################

w = 28.9 #g/mol
gamma = 1.4 
t1 = 293 #K
p1 = 101000 #Pa
R=.287

c_v = 1/(gamma-1) * R
c_p = gamma * c_v
print(c_p)
print(f"c_v = {c_v} J/g-K")
#Part a
t2_isochoric = 1465 #K
t2_choric_graph = np.linspace(t1, t2_isochoric, 100)

delta_s_isochoric = c_v * np.log(t2_choric_graph/t1)

#part b 
t2_isobaric = 1465
t2_isobaric_graph = np.linspace(t1, t2_isobaric, 100)

delta_s_isobaric = c_p * np.log(t2_isobaric_graph/t1)

#part c 
t2_isothermal_plot = np.ones(50) * t1
delta_s_isothermal = R * np.log(1/5)
delta_s_thermal_plot = np.linspace(0, delta_s_isothermal, 50)



plt.style.use(niceplots.get_style())
colors = niceplots.get_colors()
fig, ax = plt.subplots()
(isochoric,) = ax.plot(delta_s_isochoric/R, t2_choric_graph/t1, label="Isochoric")
(isobaric, ) = ax.plot(delta_s_isobaric/R, t2_isobaric_graph/t1, label="Isobaric")
(isothermal, ) = ax.plot(delta_s_thermal_plot/R, t2_isothermal_plot/t1, label="Isothermal")
ax.set_xlabel(r"$\frac{s-s_1}{R}$")
ax.set_ylabel(r"$\frac{T}{T_1}$")
niceplots.label_line_ends(ax)
niceplots.adjust_spines(ax)

niceplots.save_figs(fig, "T-s_plot", "pdf", bbox_inches='tight')