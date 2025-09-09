import numpy as np
import matplotlib.pyplot as plt
import niceplots

################## Problem 1 ##################

w = 0.0289 #kg/mol
gamma = 1.4 
t1 = 293 #K
p1 = 101000 #Pa
R_0 = 8.314 #J/mol-K
R = R_0 / w

#the trick is pv^k = constant, where k depends for different processes
c_v = 1/(gamma-1) * R
c_p = gamma * c_v

##################################
#Part a
##################################
t2_isochoric = 1465 #K
# t2_choric_graph = np.linspace(t1, t2_isochoric, 100)
#change in specific internal energy:
de_isochoric = c_v * (t2_isochoric-t1)
print(f"de_isochoric = {de_isochoric} J/kg")
#change in specific entropy:
ds_isochoric = c_v * np.log(t2_isochoric/t1)
print(f"ds_isochoric = {ds_isochoric} J/kg-K")
#change in specific work:
dw_isochoric = 0 #because of constant volume, dw = p dv = 0
#change in specific heat transfer:
dq_isochoric = de_isochoric + dw_isochoric
print(f"dq_isochoric = {dq_isochoric} J/kg")
#final pressure:
p2_isochoric = p1 * (t2_isochoric/t1)
print(f"p2_isochoric = {p2_isochoric/1000} kPa")

##################################
#part b
##################################
t2_isobaric = 1465
#change in specific internal energy:
de_isobaric = c_v * (t2_isobaric - t1)
print(f"de_isobaric = {de_isobaric} J/kg")
#change in specific entropy:
ds_isobaric = c_p * np.log(t2_isobaric/t1)
print(f"ds_isobaric = {ds_isobaric} J/kg-K")
#change in specific work:
v1_isobaric = R * t1 / p1
v2_isobaric = R * t2_isobaric / p1
dw_isobaric = p1 * (v2_isobaric - v1_isobaric)
print(f"dw_isobaric = {dw_isobaric} J/kg")
#change in specific heat transfer:
dq_isobaric = de_isobaric + dw_isobaric
print(f"dq_isobaric = {dq_isobaric} J/kg")
#final pressure:
p2_isobaric = p1
print(f"p2_isobaric = {p2_isobaric/1000} kPa")

##################################
#part c 
##################################
t2_isothermal = t1
#final pressure: 
p2_isothermal = p1 * (5)
print(f"p2_isothermal = {p2_isothermal/1000} kPa")
#change in specific internal energy:
de_isothermal = c_v * (t2_isothermal - t1)
print(f"de_isothermal = {de_isothermal} J/kg")
# change in specific entropy:
ds_isothermal = R * np.log(1/5)
print(f"ds_isothermal = {ds_isothermal} J/kg-K")
#change in specific work: #TODO: for the pdf, go to hw 2 solutions ae 225 and explain like that
v1 = R * t1 / p1
dw_isothermal= p1 * v1 * np.log(1/5)
print(f"dw_isothermal = {dw_isothermal} J/kg")
#change in specific heat transfer:
dq_isothermal = de_isothermal + dw_isothermal
print(f"dq_isothermal = {dq_isothermal} J/kg")

##################################
#part d
##################################
#irreversible isothermal:
P_s = 30 #J/kg*K #entropy generation
#change in specific internal energy:
de_irreversible_isothermal = c_v * (t2_isothermal - t1)
print(f"de_irreversible_isothermal = {de_irreversible_isothermal} J/kg")
#change in specific entropy:
ds_irreversible_isothermal = R * np.log(1/5) + P_s
print(f"ds_irreversible_isothermal = {ds_irreversible_isothermal} J/kg-K")
#change in specific work:
dw_irreversible_isothermal = R * t1 * np.log(1/5)
print(f"dw_irreversible_isothermal = {dw_irreversible_isothermal} J/kg")
#change in specific heat transfer:
dq_irreversible_isothermal = de_irreversible_isothermal + dw_irreversible_isothermal
print(f"dq_irreversible_isothermal = {dq_irreversible_isothermal} J/kg")
#final pressure:
p2_irreversible_isothermal = p1 * 5
print(f"p2_irreversible_isothermal = {p2_irreversible_isothermal/1000} kPa")
##################################
#part e (isentropic)
##################################
#isentropic:
#final pressure:
p2_isentropic = p1 * (1/5)**(-gamma)
print(f"p2_isentropic = {p2_isentropic/1000} kPa")
#final temperature:
t2_isentropic = t1 * (p2_isentropic/p1)**((gamma-1)/gamma)
print(f"t2_isentropic = {t2_isentropic} K")
#change in specific internal energy:
de_isentropic = c_v * (t2_isentropic - t1)
print(f"de_isentropic = {de_isentropic} J/kg")
#change in specific entropy:
ds_isentropic = 0
print(f"ds_isentropic = {ds_isentropic} J/kg-K")
#change in specific work: 
v2_isentropic = R * t2_isentropic / p2_isentropic
dw_isentropic = -p1 * v1 * 1/(gamma-1) * ((v2_isentropic/v1)**(1-gamma) - 1)
print(f"dw_isentropic = {dw_isentropic} J/kg")
#change in specific heat transfer:
dq_isentropic = de_isentropic + dw_isentropic
print(f"dq_isentropic = {dq_isentropic} J/kg")


#####################################################################################################
#Plotting 
plt.style.use(niceplots.get_style())
colors = niceplots.get_colors()

#T-s diagram:
figts, axts = plt.subplots(figsize=(8, 5))
(isochoric,) = axts.plot(np.array([0, ds_isochoric/R]), np.array([t1/t1, t2_isochoric/t1]), 'o', label="Isochoric")
(isobaric, ) = axts.plot(np.array([0, ds_isobaric/R]), np.array([t1/t1, t2_isobaric/t1]), 'o', label="Isobaric")
(isothermal, ) = axts.plot(np.array([0, ds_isothermal/R]), np.array([t1/t1, t2_isothermal/t1]), 'o', label="Isothermal")
(irreversible_isothermal, ) = axts.plot(np.array([0, ds_irreversible_isothermal/R]), np.array([t1/t1, t2_isothermal/t1]), 'o', label="Irreversible Isothermal")
(isentropic, ) = axts.plot(np.array([0, ds_isentropic/R]), np.array([t1/t1, t2_isentropic/t1]), 'o', label="Isentropic")
(initial, ) = axts.plot(0, t1/t1, 'ko', label="Initial State")
axts.set_xlabel(r"$\frac{s-s_1}{R}$")
axts.set_ylabel(r"$\frac{T}{T_1}$", rotation='horizontal', ha='right')
# niceplots.label_line_ends(axts)
niceplots.adjust_spines(axts, outward=True)
axts.legend()
axts.set_xlim(-2, 6)
axts.set_ylim(0, 6)
niceplots.save_figs(figts, "T-s_plot", "pdf", bbox_inches='tight')

#p-v diagram
figpv, axpv = plt.subplots(figsize=(8, 5))
(isochoric_pv,) = axpv.plot(np.array([v1, v1])/ v1, np.array([p1, p2_isochoric]) / p1, '-o', label="Isochoric")
(isobaric_pv, ) = axpv.plot(np.array([v1, v2_isobaric])/ v1, np.array([p1, p2_isobaric]) / p1, '-o', label="Isobaric")
(isothermal_pv, ) = axpv.plot(np.array([v1, v1*1/5])/ v1, np.array([p1, p2_isothermal]) / p1, 'o', label="Isothermal")
(irreversible_isothermal_pv, ) = axpv.plot(np.array([v1, v1*1/5])/ v1, np.array([p1, p2_irreversible_isothermal]) / p1, 'o', label="Irreversible Isothermal")
(isentropic_pv, ) = axpv.plot(np.array([v1, v2_isentropic])/ v1, np.array([p1, p2_isentropic]) / p1, 'o', label="Isentropic")
(initial_pv, ) = axpv.plot(1, 1, 'ko', label="Initial State")
axpv.set_xlabel(r"$\frac{v}{v_1}$")
axpv.set_ylabel(r"$\frac{p}{p_1}$", rotation='horizontal', ha='right')
# niceplots.label_line_ends(axpv)
niceplots.adjust_spines(axpv, outward=True)
axpv.legend()
axpv.set_xlim(-2, 6)
axpv.set_ylim(0, 11)
niceplots.save_figs(figpv, "p-v_plot", "pdf", bbox_inches='tight')
################## Problem 2 ##################

