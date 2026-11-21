
import matplotlib.pyplot as plt
import numpy as np

import glob2
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import MultipleLocator


from pymatgen.io.vasp import Vasprun
from pymatgen.core import Element
from pymatgen.electronic_structure.core import Spin, Orbital, OrbitalType
import glob2


import matplotlib.pyplot as plt
import numpy as np


def makeplot(runpath="/Users/zhengyuliu/Library/CloudStorage/OneDrive-ImperialCollegeLondon/phd/IrO2/structures/defect/defect_2",outputname="slab.pdf"):


            file=runpath+"/vasprun.xml"
            print(file)
            vaspr = Vasprun(filename=file, parse_projected_eigen=True)
            bandstructure=vaspr.get_band_structure()
            data_list=[]
            energy_list=[]
            #projections=bandstructure.projections
            for spin in bandstructure.projections:
                print("spin",spin)
                nbands,nkpoints,norbital,nion=bandstructure.projections[spin].shape
                print("number of bands",nbands,"number of kpoints",nkpoints,"number of orbitals",norbital,"number of ions",nion)
                #print(bandstructure.bands.shape,bandstructure.bands)
                for kpt in range(nkpoints):
                    for band in range(nbands):
                        #print("band energy:",bandstructure.bands[spin][band,kpt])

                        occupation_array=np.sum(bandstructure.projections[spin][band,kpt,:,:],axis=0)
                        ipr=np.sum(occupation_array**2)/(np.sum(occupation_array)**2)
                        data_list.append(ipr)
                        energy_list.append(bandstructure.bands[spin][band,kpt])
                        #print(ipr)




                        #total_occupy=np.sum(bandstructure.projections[spin][band,kpt,:,:])
                        #print(total_occupy)
                        #print((np.sum(bandstructure.projections[spin][band,kpt,:,:],axis=0)))

                        #for ion in range(nion):
                            #print("occupation on each orbital:",bandstructure.projections[spin][band,kpt,:,ion])
                            #print("total occupation:",np.sum(bandstructure.projections[spin][band,kpt,:,ion]))

            print(data_list,energy_list)
            #struc= vaspr.st
            dos = vaspr.tdos
            #site_dos= dos.get_site_dos()
            spinup = dos.densities[Spin.up]
            #spindn = dos.densities[Spin.down]

            valence_band_top=bandstructure.get_vbm()["energy"]

            element_dos = vaspr.complete_dos.get_element_dos()
            energy_list_np=np.array(energy_list)
            #energy_list_np-=valence_band_top
            f, ax = plt.subplots(2,1,gridspec_kw={'height_ratios': [1, 3]},figsize=(6,3))
            ax=ax.ravel()
            #struc= vaspr.st


            #####Band Gap in eV #######
            gap = vaspr.get_band_structure().get_band_gap()["energy"]
            gap="{:.1f}".format(gap)
            gap=str(gap)
            print ("Band Gap = ", gap)    

            vbmup= dos.get_cbm_vbm(spin=Spin.up)[-1]
            #vbmdown=dos.get_cbm_vbm(spin=Spin.down)[-1]

            vb = vbmup
            #if abs(vbmup) < abs(vbmdown):
            #    vb = vbmdown

            print ("Valence band ", vb, " eV")

            sigma = 0 #smearing width                


            energy = dos.energies# - valence_band_top#- sigma
            print(dos.efermi,vaspr.efermi)

            print(dos.efermi)
            #print (ax)
            item=1
            linewidth=0.1
            ax[item].plot(energy, spinup, color="black", label='Total',linewidth=linewidth)
            ax[item].fill_between(energy, 0, spinup, color ="grey")
            #ax.plot(energy, -spindn, color="black")
            #ax.fill_between(energy, 0, -spindn, color ="grey")


            species =[Element['P'], Element['S'], Element['Na'],Element['Li'],Element['O'],Element['La'],Element['Zr'],Element['Cl'],Element['Y']]


            colors = sns.color_palette("Set2")
            colors = sns.color_palette("Set2")
            for i, j in enumerate(species):
                if j in vaspr.final_structure.composition:
                #for i in vaspr.final_structure.types_of_specie:
                    ax[item].plot(energy, element_dos[j].densities[Spin.up], label=str(j), color=colors[i],linewidth=linewidth)
                #ax.plot(energy, -element_dos[j].densities[Spin.down], color=colors[i])
                #ax.plot(energy, element_dos[i])


            ax[item].legend(loc="center",bbox_to_anchor=(0.32,0.5))
            ax[item].set_xlim(-10,10)
            ax[item].set_ylim(0,250)
            ax[item].set_ylabel("Density of States")
            ax[item].set_xlabel("Energy [eV]")
            ax[item].xaxis.set_major_locator(plt.MultipleLocator(1))
            #ax[item].xaxis.set_minor_locator(plt.MultipleLocator(0.2))

            rightytick=ax[item].twinx()
            rightytick.set_yticks(ax[item].get_yticks())
            rightytick.set_ylim(ax[item].get_ylim())

            upxtick=ax[item].twiny()
            upxtick.set_xticks(ax[item].get_xticks())
            upxtick.set_xlim(ax[item].get_xlim())
            #ax.set_xlim(xlim)
            #ax.set_ylim(ylim)



            title="bulk"




            #energy_list+=vaspr.efermi


            #rightaxx.set_xlim(-10,10)




            item=0





            #rightaxx.set_title(title)
            ax[item].set_xticks(ax[1].get_xticks())
            ax[item].set_xlim(ax[1].get_xlim())
            #rightaxx.set_ylim(0.001,10)
            ax[item].set_ylabel("IPR")

            ax[item].bar(energy_list_np,data_list,width=0.01)
            ax[item].set_yscale("log")
            ax[item].plot((-10,10),(1/288,1/288),c="red")

            for idx_ in range(len(energy_list_np)):
                if energy_list_np[idx_]<-10 or energy_list_np[idx_]>10:
                    continue
                #rightaxx.text(energy_list_np[idx_],data_list[idx_],idx_,)
                pass

            rightytick=ax[item].twinx()
            rightytick.set_yticks(ax[item].get_yticks())
            rightytick.set_ylim(ax[item].get_ylim())
            rightytick.set_yscale("log")

            upxtick=ax[item].twiny()
            upxtick.set_xticks(ax[item].get_xticks())
            upxtick.set_xlim(ax[item].get_xlim())
            #df=pd.DataFrame(result,columns=["bandgap","valence_band","title"])
            #df.to_csv(vasprunpattern.split("/")[6]+"all.csv")
            plt.tight_layout()
            plt.savefig(outputname,dpi=1200)


makeplot(runpath="/Users/zhengyuliu/Library/CloudStorage/OneDrive-ImperialCollegeLondon/phd/IrO2/structures/defect/defect_2", outputname="S2.pdf")
#makeplot(runpath="/home/dx/scratch/Na_grain_boundary/grain_boundary/llzo/230310_HSE/k1_encut520Li56La24Zr16O96_0_HSE",outputname="S1.pdf")
#makeplot(runpath="/home/dx/scratch/Na_grain_boundary/grain_boundary/llzo/230331_llzo_HSE_GB_locpot_on/001_Zr_terminated_001opt_code93/Li168La72Zr48O288_0",outputname="S3.pdf")