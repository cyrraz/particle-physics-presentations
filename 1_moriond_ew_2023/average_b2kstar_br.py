'''
Print BR of B->Kstar(892)mumu or ee from averaging PDG over charged and neutral
Unit: 1e-6
'''

b2kstaree_charged = 1.55 
b2kstaree_charged_unc = (0.4+0.31)/2 
b2kstarmumu_charged = 0.96
b2kstarmumu_charged_unc = 0.11

b2kstaree_neutral = 1.03 
b2kstaree_neutral_unc = (0.19+0.17)/2 
b2kstarmumu_neutral = 0.94
b2kstarmumu_neutral_unc = 0.06

b2kstaree = (b2kstaree_charged+b2kstaree_neutral)/2
b2kstaree_unc = (b2kstaree_charged_unc**2+b2kstaree_neutral_unc**2)**0.5/2

b2kstarmumu = (b2kstarmumu_charged+b2kstarmumu_neutral)/2 
b2kstarmumu_unc = (b2kstarmumu_charged_unc**2+b2kstarmumu_neutral_unc**2)**0.5/2

print(f"b2kstaree: {b2kstaree}+-{b2kstaree_unc}")
print(f"b2kstarmumu: {b2kstarmumu}+-{b2kstarmumu_unc}")
