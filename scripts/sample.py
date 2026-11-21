import os
from pymatgen.io.vasp import Vasprun
from pymatgen.core.structure import Structure
import numpy as np
import pandas as pd
from joblib import Parallel,delayed
import multiprocessing
from tqdm import tqdm
import glob2
import json
from pymatgen.analysis.surface_analysis import WorkFunctionAnalyzer
 
bondlength=2.3# for work function analyzer
 
def process_vasprun(vasprun_path="",
nonstochiometric_chemical_potential={},
nonstochiometric_atomic_volume={},
stochiometric_formula=' Li7 La3 Zr2 O12 ',
only_stochiometric=False,):
    try:
                        vasprun=Vasprun(vasprun_path)
                        final_structure = vasprun.final_structure
                       
                        if max(final_structure.lattice.abc) < 25:
                            return [None,ValueError("abc<25"), vasprun_path ]
                       
                        composition = final_structure.composition
                        composition_human_readable=""
                        excessive_energy=vasprun.final_energy# for gamma sigma
                        formation_energy=vasprun.final_energy# for formation energy
                        reference_volume=0
                        reduced_formula,number_of_formula=final_structure.composition.get_reduced_composition_and_factor()
                       
                        if stochiometric_formula not in str(reduced_formula) and only_stochiometric:
                            raise ValueError("Nonstochiometric",reduced_formula)
                       
                        """
                       
                       
                        START OF PASTE
                       
                       
                        """                            
     
 
 
     
                        n_P = composition.get_el_amt_dict()['P']
                        n_S = composition.get_el_amt_dict()['S']
                        n_Li = composition.get_el_amt_dict()['Li']
                        n_Na = composition.get_el_amt_dict()['Na']
                        n_La = composition.get_el_amt_dict()['La']
                        n_O = composition.get_el_amt_dict()['O']
                        n_Zr = composition.get_el_amt_dict()['Zr']
                        n_Si = composition.get_el_amt_dict()['Si']
                        n_Y=composition.get_el_amt_dict()['Y']
                        n_Cl=composition.get_el_amt_dict()['Cl']
                        n_N=composition.get_el_amt_dict()['N']
                        if 5*n_P+n_Li+n_Na+n_La*3+n_Zr*4+n_Si*4+3*n_Y!=2*n_S+2*n_O+n_Cl+3*n_N and "metals" not in vasprun_path:
                            raise ValueError("unneutral charge")  
     
 
                        n_P = composition.get_el_amt_dict()['P']
                        if 'P' in nonstochiometric_chemical_potential:
                            excessive_energy-=n_P*nonstochiometric_chemical_potential['P']
                           
 
                           
         
 
                        n_S = composition.get_el_amt_dict()['S']
                        if 'S' in nonstochiometric_chemical_potential:
                            excessive_energy-=n_S*nonstochiometric_chemical_potential['S']
                           
 
                           
         
 
                        n_Li = composition.get_el_amt_dict()['Li']
                        if 'Li' in nonstochiometric_chemical_potential:
                            excessive_energy-=n_Li*nonstochiometric_chemical_potential['Li']
                           
 
                           
         
 
                        n_Na = composition.get_el_amt_dict()['Na']
                        if 'Na' in nonstochiometric_chemical_potential:
                            excessive_energy-=n_Na*nonstochiometric_chemical_potential['Na']
                           
 
                           
         
 
                        n_La = composition.get_el_amt_dict()['La']
                        if 'La' in nonstochiometric_chemical_potential:
                            excessive_energy-=n_La*nonstochiometric_chemical_potential['La']
                           
 
                           
         
 
                        n_O = composition.get_el_amt_dict()['O']
                        if 'O' in nonstochiometric_chemical_potential:
                            excessive_energy-=n_O*nonstochiometric_chemical_potential['O']
                           
 
                           
         
 
                        n_Zr = composition.get_el_amt_dict()['Zr']
                        if 'Zr' in nonstochiometric_chemical_potential:
                            excessive_energy-=n_Zr*nonstochiometric_chemical_potential['Zr']
                           
 
                           
         
 
                        n_Si = composition.get_el_amt_dict()['Si']
                        if 'Si' in nonstochiometric_chemical_potential:
                            excessive_energy-=n_Si*nonstochiometric_chemical_potential['Si']
                           
 
                           
         
 
                        n_Y = composition.get_el_amt_dict()['Y']
                        if 'Y' in nonstochiometric_chemical_potential:
                            excessive_energy-=n_Y*nonstochiometric_chemical_potential['Y']
                           
 
                           
         
 
                        n_Cl = composition.get_el_amt_dict()['Cl']
                        if 'Cl' in nonstochiometric_chemical_potential:
                            excessive_energy-=n_Cl*nonstochiometric_chemical_potential['Cl']
                           
 
                           
         
 
                        n_N = composition.get_el_amt_dict()['N']
                        if 'N' in nonstochiometric_chemical_potential:
                            excessive_energy-=n_N*nonstochiometric_chemical_potential['N']
                           
 
                           
         
 
 
                        n_P = composition.get_el_amt_dict()['P']
                        n_S = composition.get_el_amt_dict()['S']
                        n_Li = composition.get_el_amt_dict()['Li']
                        n_Na = composition.get_el_amt_dict()['Na']
                        n_La = composition.get_el_amt_dict()['La']
                        n_O = composition.get_el_amt_dict()['O']
                        n_Zr = composition.get_el_amt_dict()['Zr']
                        n_Si = composition.get_el_amt_dict()['Si']
                        n_Y=composition.get_el_amt_dict()['Y']
                        n_Cl=composition.get_el_amt_dict()['Cl']
                        n_N=composition.get_el_amt_dict()['N']
                        if 5*n_P+n_Li+n_Na+n_La*3+n_Zr*4+n_Si*4+3*n_Y!=2*n_S+2*n_O+n_Cl+3*n_N and "metals" not in vasprun_path:
                            raise ValueError("unneutral charge")  
 
                        n_Na3Zr2Si2PO12=min(n_Na/3,n_Zr/2,n_Si/2,n_P/1,n_O/12,)
 
                 
                        if n_Na3Zr2Si2PO12>0:
                            composition_human_readable+=f"(Na3Zr2Si2PO12){n_Na3Zr2Si2PO12}"
                            reference_volume+=n_Na3Zr2Si2PO12*279.61702309373106
   
                            n_Na-=n_Na3Zr2Si2PO12*3
                            n_Zr-=n_Na3Zr2Si2PO12*2
                            n_Si-=n_Na3Zr2Si2PO12*2
                            n_P-=n_Na3Zr2Si2PO12*1
                            n_O-=n_Na3Zr2Si2PO12*12
                        n_Li7La3Zr2O12=min(n_Li/7,n_La/3,n_Zr/2,n_O/12,)
 
                 
                        if n_Li7La3Zr2O12>0:
                            composition_human_readable+=f"(Li7La3Zr2O12){n_Li7La3Zr2O12}"
                            reference_volume+=n_Li7La3Zr2O12*275.28340017184144
   
                            n_Li-=n_Li7La3Zr2O12*7
                            n_La-=n_Li7La3Zr2O12*3
                            n_Zr-=n_Li7La3Zr2O12*2
                            n_O-=n_Li7La3Zr2O12*12
                        n_Li2PNO2=min(n_Li/2,n_P/1,n_N/1,n_O/2,)
 
                 
                        if n_Li2PNO2>0:
                            composition_human_readable+=f"(Li2PNO2){n_Li2PNO2}"
                            reference_volume+=n_Li2PNO2*58.723722258904516
   
                            n_Li-=n_Li2PNO2*2
                            n_P-=n_Li2PNO2*1
                            n_N-=n_Li2PNO2*1
                            n_O-=n_Li2PNO2*2
                        n_Na2ZrSi2O7=min(n_Na/2,n_Zr/1,n_Si/2,n_O/7,)
 
                 
                        if n_Na2ZrSi2O7>0:
                            composition_human_readable+=f"(Na2ZrSi2O7){n_Na2ZrSi2O7}"
                            reference_volume+=n_Na2ZrSi2O7*155.80805283194596
   
                            n_Na-=n_Na2ZrSi2O7*2
                            n_Zr-=n_Na2ZrSi2O7*1
                            n_Si-=n_Na2ZrSi2O7*2
                            n_O-=n_Na2ZrSi2O7*7
                        n_Li3YCl6=min(n_Li/3,n_Y/1,n_Cl/6,)
 
                 
                        if n_Li3YCl6>0:
                            composition_human_readable+=f"(Li3YCl6){n_Li3YCl6}"
                            reference_volume+=n_Li3YCl6*219.90698262277817
   
                            n_Li-=n_Li3YCl6*3
                            n_Y-=n_Li3YCl6*1
                            n_Cl-=n_Li3YCl6*6
                        n_Na3PS4=min(n_Na/3,n_P/1,n_S/4,)
 
                        if n_Na3PS4>0 and "cubic-Na3PS4" in vasprun_path:
                            reference_volume+=n_Na3PS4*351.96563989712763/2
                 
                            n_Na-=n_Na3PS4*3
                            n_P-=n_Na3PS4*1
                            n_S-=n_Na3PS4*4
                        n_Na3PS4=min(n_Na/3,n_P/1,n_S/4,)
 
                        if n_Na3PS4>0 and "tetra-Na3PS4" in vasprun_path:
                       
                            reference_volume+=n_Na3PS4*350.26346797599774/2
                 
                            n_Na-=n_Na3PS4*3
                            n_P-=n_Na3PS4*1
                            n_S-=n_Na3PS4*4
                        n_Li3PS4=min(n_Li/3,n_P/1,n_S/4,)
 
                 
                        if n_Li3PS4>0:
                            composition_human_readable+=f"(Li3PS4){n_Li3PS4}"
                            reference_volume+=n_Li3PS4*165.6658877878175
   
                            n_Li-=n_Li3PS4*3
                            n_P-=n_Li3PS4*1
                            n_S-=n_Li3PS4*4
                        n_Li3PO4=min(n_Li/3,n_P/1,n_O/4,)
 
                 
                        if n_Li3PO4>0:
                            composition_human_readable+=f"(Li3PO4){n_Li3PO4}"
                            reference_volume+=n_Li3PO4*80.79655700459973
   
                            n_Li-=n_Li3PO4*3
                            n_P-=n_Li3PO4*1
                            n_O-=n_Li3PO4*4
                        n_Na4P2O7=min(n_Na/4,n_P/2,n_O/7,)
 
                 
                        if n_Na4P2O7>0:
                            composition_human_readable+=f"(Na4P2O7){n_Na4P2O7}"
                            reference_volume+=n_Na4P2O7*176.362573194657
   
                            n_Na-=n_Na4P2O7*4
                            n_P-=n_Na4P2O7*2
                            n_O-=n_Na4P2O7*7
                        n_La2O3=min(n_La/2,n_O/3,)
 
                 
                        if n_La2O3>0:
                            composition_human_readable+=f"(La2O3){n_La2O3}"
                            reference_volume+=n_La2O3*92.61865832264952
   
                            n_La-=n_La2O3*2
                            n_O-=n_La2O3*3
                        n_ZrO2=min(n_Zr/1,n_O/2,)
 
                 
                        if n_ZrO2>0:
                            composition_human_readable+=f"(ZrO2){n_ZrO2}"
                            reference_volume+=n_ZrO2*36.08696539188881
   
                            n_Zr-=n_ZrO2*1
                            n_O-=n_ZrO2*2
                        n_SiO2=min(n_Si/1,n_O/2,)
 
                 
                        if n_SiO2>0:
                            composition_human_readable+=f"(SiO2){n_SiO2}"
                            reference_volume+=n_SiO2*46.948669010653504
   
                            n_Si-=n_SiO2*1
                            n_O-=n_SiO2*2
                        n_Li2O=min(n_Li/2,n_O/1,)
 
                 
                        if n_Li2O>0:
                            composition_human_readable+=f"(Li2O){n_Li2O}"
                            reference_volume+=n_Li2O*24.67136008142777
   
                            n_Li-=n_Li2O*2
                            n_O-=n_Li2O*1
                        n_Li2S=min(n_Li/2,n_S/1,)
 
                 
                        if n_Li2S>0:
                            composition_human_readable+=f"(Li2S){n_Li2S}"
                            reference_volume+=n_Li2S*46.30617346336254
   
                            n_Li-=n_Li2S*2
                            n_S-=n_Li2S*1
                        n_P2S5=min(n_P/2,n_S/5,)
 
                 
                        if n_P2S5>0:
                            composition_human_readable+=f"(P2S5){n_P2S5}"
                            reference_volume+=n_P2S5*226.12155824131386
   
                            n_P-=n_P2S5*2
                            n_S-=n_P2S5*5
                        n_P2O5=min(n_P/2,n_O/5,)
 
                 
                        if n_P2O5>0:
                            composition_human_readable+=f"(P2O5){n_P2O5}"
                            reference_volume+=n_P2O5*93.47120898854914
   
                            n_P-=n_P2O5*2
                            n_O-=n_P2O5*5
                        n_LiCl=min(n_Li/1,n_Cl/1,)
 
                 
                        if n_LiCl>0:
                            composition_human_readable+=f"(LiCl){n_LiCl}"
                            reference_volume+=n_LiCl*34.139695919625034
   
                            n_Li-=n_LiCl*1
                            n_Cl-=n_LiCl*1
                        n_YCl3=min(n_Y/1,n_Cl/3,)
 
                 
                        if n_YCl3>0:
                            composition_human_readable+=f"(YCl3){n_YCl3}"
                            reference_volume+=n_YCl3*139.58418336400598
   
                            n_Y-=n_YCl3*1
                            n_Cl-=n_YCl3*3
                        n_Na2O=min(n_Na/2,n_O/1,)
 
                 
                        if n_Na2O>0:
                            composition_human_readable+=f"(Na2O){n_Na2O}"
                            reference_volume+=n_Na2O*43.575192256814184
   
                            n_Na-=n_Na2O*2
                            n_O-=n_Na2O*1
                        n_Na2S=min(n_Na/2,n_S/1,)
 
                 
                        if n_Na2S>0:
                            composition_human_readable+=f"(Na2S){n_Na2S}"
                            reference_volume+=n_Na2S*70.34786872838717
   
                            n_Na-=n_Na2S*2
                            n_S-=n_Na2S*1
 
                        if n_P+n_Li+n_Na+n_La+n_Zr+n_Si+n_Y+n_S+n_O+n_Cl+n_N>0 and "metals" not in vasprun_path:
                            print(n_P,n_Li,n_Na,n_La,n_Zr,n_Si,n_Y,n_S,n_O,n_Cl,n_N)
                            raise ValueError("element left compount not identified")  
                           
 
         
 
                       
                        """
                       
                       
                        END OF PASTE
                       
                       
                        """    
 
                       
                        this_area=np.linalg.norm(np.cross(final_structure.lattice._matrix[0],final_structure.lattice._matrix[1]))
                       
                        print(np.cross(final_structure.lattice._matrix[0],final_structure.lattice._matrix[1])[-1],np.linalg.norm(np.cross(final_structure.lattice._matrix[0],final_structure.lattice._matrix[1])))
                       
 
                        gamma_or_sigma=excessive_energy/this_area/2
                        formation_energy=excessive_energy/len(final_structure)
                       
                        total_volume=final_structure.volume
                        volume_change=total_volume-reference_volume
                           
 
                        dir=vasprun_path.split("/")[-3]
                       
                        # add the locpot
                        #for folder in tqdm(glob2.glob("/home/dx/scratch/Na_grain_boundary/grain_boundary/*/230222_*_slab_locpot_on/stochiometric*slab/*")):
                       
 
                        if "slab" in dir:
                            miller_and_shift=dir.replace("_slab","").replace("non","").replace("stochiometric_","")
                            #slab_energy[miller_and_shift]=vasprun.final_energy
                            #gammas[miller_and_shift]=gamma_or_sigma          
                            gap = vasprun.get_band_structure().get_band_gap()["energy"]
                            minimum_z_coord_of_structure=min(final_structure.frac_coords[:,2])
                            final_structure.translate_sites(indices=np.arange(len(final_structure)),vector=[0,0,-minimum_z_coord_of_structure+0.0001],to_unit_cell=True)
                            if max(final_structure.frac_coords[:,2])>0.9:
                                final_structure.translate_sites(indices=np.arange(len(final_structure)),vector=[0,0,1-max(final_structure.frac_coords[:,2])+0.0001],to_unit_cell=True)
                            slab_thickness=max(final_structure.cart_coords[:,2])-min(final_structure.cart_coords[:,2])# because this is orthogonal_c_slab so it is ok
                            vacuum=final_structure.lattice.c-max(final_structure.cart_coords[:,2])  
                               
                            hkl=[]
                                         
                            for string in miller_and_shift:
                                try:
                                    temp_int=int(string)
                                except Exception as e:
                                    continue
                                else:
                                    hkl.append(temp_int)
                                    #print(miller_and_shift,temp_int)
                                if len(hkl)==3:
                                    break
                               
                            hkl=hkl[0]**2+ hkl[1]**2+  hkl[2]**2            
                           
                            if "nonstochiometric" in dir:
                                #stochiometric_or_nots[miller_and_shift]=False
                               
                                thisslab_isstochiometric=False
                               
                               
                            else:
                                thisslab_isstochiometric=True
                               
                            locpot_folder="/".join(vasprun_path.split("/")[:7])+"/230222_"+vasprun_path.split("/")[6]+"_slab_locpot_on/"+vasprun_path.split("/")[8]+"/"+vasprun_path.split("/")[9]
                            #print(locpot_folder)
                            if os.path.isdir(locpot_folder) and os.path.isfile(locpot_folder+"/LOCPOT"):
                                #print("selected for locpot")
                               
 
                                a=WorkFunctionAnalyzer.from_files(locpot_folder+"/CONTCAR",locpot_folder+"/LOCPOT",locpot_folder+"/OUTCAR",shift=0,blength=bondlength)
                                locpot_vasprun=Vasprun(filename=locpot_folder+"/vasprun.xml")
                                bandstructure=locpot_vasprun.get_band_structure()    
                                if not a.is_converged():
                                    min_points_frac=0.015*2
                                    tol=0.0025*2
                                    while True:
 
                                        if a.is_converged(min_points_frac=min_points_frac,tol=tol):
                                            print(f"{locpot_folder}  converged with min_points_frac{min_points_frac} and tolerance{tol}")
                                            break
                                        else:
                                            print(f"{locpot_folder}  not converged with min_points_frac{min_points_frac} and tolerance{tol}")
                                        #min_points_frac*=2
                                        tol*=2
                                   
                                   
                                   
                                    #a.get_locpot_along_slab_plot()
 
                                   
                                    #raise ValueError(f"{folder} not converged")
                                else:
                                    tol=0.0025
                                    #a.get_locpot_along_slab_plot()    
                                   
                                aligned_valence_band=bandstructure.get_vbm()['energy']-a.vacuum_locpot
                                aligned_conduction_band=bandstructure.get_cbm()['energy']-a.vacuum_locpot
                                workfunction=a.work_function
                            else:
                                aligned_valence_band="Not calculated"
                                aligned_conduction_band="Not calculated"
                                workfunction="Not calculated"      
                               
                               
                            json_data={'miller':miller_and_shift,
                                       "final_energy":vasprun.final_energy,
                                       "gamma":gamma_or_sigma,
 
                                       "work_function":workfunction,
                                       "ionization_potentail":aligned_valence_band,
                                       "electron_affinity":aligned_conduction_band,
                                       "is_stochiometric":thisslab_isstochiometric,
                                       "incar_parameters":vasprun.parameters.as_dict(),
                                       "relaxed_structures":vasprun.final_structure.as_dict(),
                                        "formula":composition_human_readable,
                                        "bandgap":gap,
                                        "slab_thickness":slab_thickness,
                                       
                                       }
                            dump_path="/home/dx/projects/project_grainboundary/JSON_metadata/"+vasprun_path.split("/")[6]+'/slab/'
                            os.system("mkdir -p "+dump_path)
                            dump_json_path=dump_path+miller_and_shift+".json"
                            print("dumping to"+dump_json_path)
                            with open(dump_json_path,"w") as f:
                                json.dump(json_data,f)
                               
                            return ("slab",miller_and_shift,vasprun.final_energy,gamma_or_sigma,gap,slab_thickness,vacuum,aligned_valence_band,aligned_conduction_band,workfunction,hkl,thisslab_isstochiometric)
                       
                       
                       
 
                        else:
                            gap = vasprun.get_band_structure().get_band_gap()["energy"]
 
                            miller_and_shift=dir
                           
                            gb_thickness=final_structure.lattice.c
                            grainboundary_symmetry=final_structure.get_space_group_info(symprec=0.01)
                            json_data={'miller':miller_and_shift,
                                       "final_energy":vasprun.final_energy,
                                       "sigma":gamma_or_sigma,
 
                                       "incar_parameters":vasprun.parameters.as_dict(),
                                       "relaxed_structures":vasprun.final_structure.as_dict(),
                                        "formula":composition_human_readable,
                                        "bandgap":gap,
 
                                       
                                       }
                            dump_path="/home/dx/projects/project_grainboundary/JSON_metadata/"+vasprun_path.split("/")[6]+'/grainboundary/'
                            os.system("mkdir -p "+dump_path)
                            dump_json_path=dump_path+miller_and_shift+".json"
                            print("dumping to"+dump_json_path)
                            with open(dump_json_path,"w") as f:
                                json.dump(json_data,f)
                            return("grain",miller_and_shift,str(composition).replace(" ",""),composition_human_readable,vasprun.final_energy,gamma_or_sigma,this_area,volume_change,formation_energy,gb_thickness,grainboundary_symmetry,gap)
    except Exception as e:
        return [None,e, vasprun_path ]
         
 
def process_material(sinter_T=1503,
name_of_material="LLZO",
reference_bandgap=4.3688,
grainboundary_vasprun_path="/home/dx/scratch/Na_grain_boundary/grain_boundary/llzo/llzo_grain_boundaries_520eV_reorganize_dir",
nonstochiometric_chemical_potential={},
nonstochiometric_atomic_volume={},
stochiometric_formula="",
only_stochiometric=True,
):
    sinter_T=sinter_T
    name_of_material=name_of_material
    reference_bandgap=reference_bandgap
    grainboundary_vasprun_path=grainboundary_vasprun_path
    gb_bandgaps={}
    slab_bandgaps={}
    compositions={}
    compositions2={}
    gammas={}
    sigmas={}
    grainboundary_energy={}
    slab_energy={}
    area={}
    Efs={}
    volumes={}
    stochiometric_or_nots={}
    possibilities={}
    slab_thicknesss={}
    vacuums={}
    gb_thicknesss={}
    gb_symmetrys={}
    slab_conduction_bands={}
    slab_valence_bands={}
    slab_work_functions={}
    hkl_squre_sums={}
 
   
   
    rawdatas=Parallel(n_jobs=35)(delayed(process_vasprun)(vasprun_path,nonstochiometric_chemical_potential,nonstochiometric_atomic_volume,stochiometric_formula, only_stochiometric) for vasprun_path in tqdm(glob2.glob(grainboundary_vasprun_path+"/**/vasprun.xml.relaxed")))
 
    for rawdata in rawdatas:
        if rawdata[0]=="slab":
            ababa,miller_and_shift_,slabenergy_,gamma_,bandgap_,slab_thickness,vacuum,valence_band_position,conduction_band_position,work_function,hkl_square_sum,stochiometric_or_not_=rawdata
            print(miller_and_shift_,hkl_square_sum)
            stochiometric_or_nots[miller_and_shift_]=stochiometric_or_not_
                       
            slab_bandgaps[miller_and_shift_]=bandgap_-reference_bandgap
            slab_energy[miller_and_shift_]=slabenergy_
            gammas[miller_and_shift_]=gamma_
            slab_thicknesss[miller_and_shift_]=slab_thickness
            vacuums[miller_and_shift_]=vacuum
            slab_valence_bands[miller_and_shift_]=valence_band_position
            slab_conduction_bands[miller_and_shift_]=conduction_band_position
            slab_work_functions[miller_and_shift_]=work_function
            hkl_squre_sums[miller_and_shift_]=hkl_square_sum
           
           
           
           
           
        elif rawdata[0]=="grain":                
            ababa, miller_and_shift_,composition_,composition2_,grainbboundary_energy_,sigma_,area_,volume_change_,formation_energy_,gb_thickness,gb_symmetry,bandgap_=rawdata
 
            gb_bandgaps[miller_and_shift_]=bandgap_-reference_bandgap
           
            grainboundary_energy[miller_and_shift_]= grainbboundary_energy_
 
            compositions[miller_and_shift_]=composition_
            sigmas[miller_and_shift_]=sigma_
            compositions2[miller_and_shift_]=composition2_                    
            area[miller_and_shift_]=area_
            volumes[miller_and_shift_]=volume_change_
            Efs[miller_and_shift_]=formation_energy_
            possibilities[miller_and_shift_]=np.exp(-formation_energy_/(0.00008617333*sinter_T))
            gb_thicknesss[miller_and_shift_]=gb_thickness
            gb_symmetrys[miller_and_shift_]=gb_symmetry
           
        elif rawdata[0]==None:
            print(str(rawdata[1])+" error occcur in "+str(rawdata[2]))
           
           
 
    pd_summary=[]                    
 
    for miller_and_shift in slab_energy:
        if miller_and_shift in grainboundary_energy:
 
           
            pd_summary.append([miller_and_shift,
                            compositions[miller_and_shift],
                            compositions2[miller_and_shift],
                            float(2*gammas[miller_and_shift]-sigmas[miller_and_shift])*16.0218,
                            area[miller_and_shift],
                            gammas[miller_and_shift]*16.0218,
                            sigmas[miller_and_shift]*16.0218,
                            Efs[miller_and_shift]*1000,
                            possibilities[miller_and_shift]/sum(possibilities.values())*100,
                            grainboundary_energy[miller_and_shift],
                            slab_energy[miller_and_shift],
                            (volumes[miller_and_shift])/area[miller_and_shift]/2,
                            slab_bandgaps[miller_and_shift],
                            gb_bandgaps[miller_and_shift],
                            slab_conduction_bands[miller_and_shift],
                            slab_valence_bands[miller_and_shift],
                            slab_work_functions[miller_and_shift],
                            hkl_squre_sums[miller_and_shift],
                            stochiometric_or_nots[miller_and_shift],
                            name_of_material])
    #print(pd_summary)
           
           
    summary=pd.DataFrame(pd_summary, columns=["miller_shift",
                                            "composition",
                                            "composition2",
                                            "Wad[Jm-2]",
                                            "area[A2]",
                                            "gammas[Jm-2]",
                                            "sigmas[Jm-2]",
                                            "Ef[meV/atom]",
                                            "P_boltzman[%]",
                                            "E_gb[eV]",
                                            "E_slab[eV]",
                                            "BFV[A]",
                                            "slab_bandgap_change[eV]",
                                            "gb_bandgap_change[eV]",
                                            "slab_conduction_band[eV]",
                                            "slab_valence_band[eV]",
                                            "slab_work_function[eV]",
                                            "hkl_square_sum",
                                            "is_stochiometric",
                                            "data"])
    print(summary)
 
    summary.to_csv("data_each_materials/"+name_of_material+"_work_of_adhesionv3.csv")
    lines=open("data_each_materials/"+name_of_material+"_work_of_adhesionv3.csv").readlines()[1:]
    #sigma_column_name="sigmas[Jm-2]"
   
    sigma_column_at_index=7
   
    if open("data_each_materials/"+name_of_material+"_work_of_adhesionv3.csv").readlines()[0].split(",")[sigma_column_at_index]!="sigmas[Jm-2]":
        raise ValueError("need realign")
   
   
    lines.sort(key=lambda x: float(x.split(",")[sigma_column_at_index]))
    done_miller=[]
    unique_lines=[open("data_each_materials/"+name_of_material+"_work_of_adhesionv3.csv").readlines()[0]]
    for line in lines:
        miller=line.split(",")[1].split("_")[0]
        data=line.split(",")[-1].replace("\n","")
        if data+miller in done_miller:
            continue
        else:
            done_miller.append(data+miller)
            unique_lines.append(line)
    print(done_miller)
    with open("data_each_materials/"+name_of_material+"_workofadhesion_uniquemillerv3.csv","w") as f:
        f.write("".join(unique_lines))
    """
    1eV/A2=1.60218*10-19J/(10-20m2)=16.0218J/M2
 
    """
 
def main():
#     process_material(name_of_material="Li6PS5Cl",
#     grainboundary_vasprun_path="/home/dx/scratch/Na_grain_boundary/grain_boundary/Li6PS5Cl/230323_657_allcalc",
# #bulk energy -54.00697249 eV
# #bulk volume: 258.00626973085355
# #bulk energy -54.00697249 eV
# #bulk volume: 258.00626973085355
# stochiometric_formula='Li6 P1 S5 Cl1',
# reference_bandgap=2.1592000000000002,
# nonstochiometric_chemical_potential= {'Li': -3.6413096737500026, 'P': -7.741451838749992, 'S': -4.1358126925, 'Cl': -3.738599146249997} ,
# only_stochiometric=False,
 
    # sinter_T=573)
    process_material(name_of_material="Li6PS5Cl_Cl",
    grainboundary_vasprun_path="/home/dx/scratch/Na_grain_boundary/grain_boundary/Li6PS5Cl/230413_S_deficient",
#bulk energy -54.33321196 eV
#bulk volume: 250.42066038541165
stochiometric_formula='Li6 P1 S5 Cl1',
reference_bandgap=2.2419,
nonstochiometric_chemical_potential= {'Li': -3.9528525300000017, 'P': -6.736162777500002, 'S': -4.090575542499998, 'Cl': -3.4270562899999986} ,
only_stochiometric=False,
    sinter_T=573)
   
    process_material(name_of_material="Li6PS5Cl_S",
    grainboundary_vasprun_path="/home/dx/scratch/Na_grain_boundary/grain_boundary/Li6PS5Cl/230413_S_rich",
#bulk energy -54.33321196 eV
#bulk volume: 250.42066038541165
stochiometric_formula='Li6 P1 S5 Cl1',
reference_bandgap=2.2419,
nonstochiometric_chemical_potential= {'Li': -3.80442940875, 'P': -7.252092633749999, 'S': -4.1358126925, 'Cl': -3.5754794112499995} ,
only_stochiometric=False,
sinter_T=573)
    process_material(sinter_T=1503,
    name_of_material="LLZO",
    reference_bandgap=4.3688,
    grainboundary_vasprun_path="/home/dx/scratch/Na_grain_boundary/grain_boundary/llzo/230303_miller1_and_frompiero",
    stochiometric_formula='Li7 La3 Zr2 O12',
    nonstochiometric_chemical_potential= {'Li': -1.9248503863671866, 'La': -5.225328623164058, 'Zr': -8.523807205, 'O': -10.496620729765628} ,
    nonstochiometric_atomic_volume= {'Li': 11.967824154513588, 'La': 45.205761502723874, 'Zr': 23.531402656633798, 'O': 0.7357117724005919} ,
    only_stochiometric=False,
    )
 
    process_material(sinter_T=573,
    name_of_material="beta-Li3PS4",
    grainboundary_vasprun_path="/home/dx/scratch/Na_grain_boundary/grain_boundary/beta-Li3PS4/221121_LiPS_grainboundary",stochiometric_formula='Li3 P1 S4',
    reference_bandgap=2.8137,
    only_stochiometric=True,
    nonstochiometric_chemical_potential= {'S': -8.795088839375} ,
    nonstochiometric_atomic_volume= {'S': 41.416471946954374} ,)
 
    process_material(name_of_material="nasicon",
    grainboundary_vasprun_path="/home/dx/scratch/Na_grain_boundary/grain_boundary/nasicon/230224_Na3_miller2_calcZr",
    nonstochiometric_atomic_volume= {'Na': 39.76034844273341, 'Zr': 23.531402656633816, 'Si': -94.62082540637519, 'P': -112.33821233943618, 'O': 34.571086300370816} ,
    #bulk energy -152.03381364 eV
    #bulk volume: 279.61702309373106
    stochiometric_formula='Na3 Zr2 Si2 P1 O12',
    reference_bandgap=4.6785,
    nonstochiometric_chemical_potential= {'Na': -4.30326182875, 'Zr': -18.9014100625, 'Si': -13.944562552500004, 'P': -14.155420363750011, 'O': -4.93972188} ,
    only_stochiometric=False,
 
    sinter_T=573)
 
    process_material(name_of_material="Li3YCl6",
 
    grainboundary_vasprun_path="/home/dx/scratch/Na_grain_boundary/grain_boundary/Li3YCl6/230207_LiYCl_grainboundary_calc",
#bulk energy -43.203818936666664 eV
#bulk volume: 223.10258274445187
    stochiometric_formula='Li3 Y1 Cl6',
    reference_bandgap=4.9453000000000005,
    nonstochiometric_chemical_potential= {'Li': -2.5000266694444466, 'Y': -6.424446025, 'Cl': -4.879882150555554} ,
    only_stochiometric=False,
 
    sinter_T=573)
 
    process_material(name_of_material="tetra-Na3PS4",
    stochiometric_formula='Na3 P1 S4',
    reference_bandgap=2.2794000000000003,
    only_stochiometric=True,
    nonstochiometric_chemical_potential= {'S': -8.23091554875} ,
    nonstochiometric_atomic_volume= {'S': 43.995704987140954} ,
    grainboundary_vasprun_path="/home/dx/scratch/Na_grain_boundary/grain_boundary/tetra-Na3PS4/221118_grainboundary/",
    sinter_T=300)
 
    process_material(name_of_material="cubic-Na3PS4",
    stochiometric_formula='Na3 P1 S4',
    reference_bandgap=2.2962,
    only_stochiometric=True,
    nonstochiometric_chemical_potential= {'S': -8.2195624875} ,
    nonstochiometric_atomic_volume= {'S': 43.78293349699972} ,
    grainboundary_vasprun_path="/home/dx/scratch/Na_grain_boundary/grain_boundary/cubic-Na3PS4/221119_grain_boundaries_stochiometric_finekpoint_520eV",
    sinter_T=300)
 
    process_material(sinter_T=673,
    name_of_material="gamma-Li3PO4",
    grainboundary_vasprun_path="/home/dx/scratch/Na_grain_boundary/grain_boundary/gamma_Li3PO4/221124_LiPO_grainboundary",
    stochiometric_formula='Li3 P1 O4',
    reference_bandgap=5.8369,
    only_stochiometric=True,
    nonstochiometric_chemical_potential= {'O': -12.5835947675} ,
    nonstochiometric_atomic_volume= {'O': 20.199139251149933} ,
    )


    process_material(name_of_material="Li2O",
    stochiometric_formula='Li2 O1',
    reference_bandgap=4.9698,
    only_stochiometric=True,
    nonstochiometric_chemical_potential= {'O': -14.3463215025} ,
    nonstochiometric_atomic_volume= {'O': 24.67136008142777} ,
    grainboundary_vasprun_path="/home/dx/scratch/Na_grain_boundary/grain_boundary/Li2O/230208_no_coordination_require",
    sinter_T=573)
 
    process_material(name_of_material="Li2S",
    stochiometric_formula='Li2 S1',
    reference_bandgap=3.3893,
    only_stochiometric=True,
    nonstochiometric_chemical_potential= {'S': -11.9962806025} ,
    nonstochiometric_atomic_volume= {'S': 46.30617346336254} ,
    grainboundary_vasprun_path="/home/dx/scratch/Na_grain_boundary/grain_boundary/Li2S/230209_nocoordination",
    sinter_T=573)
 
    process_material(name_of_material="Na2S",
    stochiometric_formula='Na2 S1',
    reference_bandgap=2.4657,
    only_stochiometric=True,
    nonstochiometric_chemical_potential= {'S': -9.9755967475} ,
    nonstochiometric_atomic_volume= {'S': 70.34786872838717} ,
    grainboundary_vasprun_path="/home/dx/scratch/Na_grain_boundary/grain_boundary/Na2S/230222_grainboudnary",
    sinter_T=573)
 
    process_material(name_of_material="LiCl",
    stochiometric_formula='Li1 Cl1',
    reference_bandgap=6.270499999999999,
    only_stochiometric=True,
    nonstochiometric_chemical_potential= {'Cl': -7.37990882} ,
    nonstochiometric_atomic_volume= {'Cl': 34.139695919625034} ,
    grainboundary_vasprun_path="/home/dx/scratch/Na_grain_boundary/grain_boundary/LiCl/230228_LiCl_grainboundary",
    sinter_T=573)


















    import pandas as pd
    import glob2


    allcsv=glob2.glob("data_each_materials/*_work_of_adhesionv3.csv")
    df_concat = pd.concat([pd.read_csv(f) for f in allcsv ], ignore_index=True)
    df_concat.to_csv("allworkofadhesionv3.csv")    
   
   
    merged_li6ps5cl=[open("allworkofadhesionv3.csv").readlines()[0]]
    for line in open("allworkofadhesionv3.csv").readlines()[1:]:
        merged_li6ps5cl.append(line.replace("Li6PS5Cl_S","Li6PS5Cl").replace("Li6PS5Cl_Cl","Li6PS5Cl"))
       
    merged_li6ps5cl="".join(merged_li6ps5cl)
    with open("allworkofadhesionv3.csv","w") as f:
        f.write(merged_li6ps5cl)
       
       
       



    df_concat=df_concat.drop(labels=["Unnamed: 0","composition","composition2","area[A2]","P_boltzman[%]","E_gb[eV]","E_slab[eV]",], axis=1)
 
    df_concat.to_csv("print_summary_allmiller.csv")







    allcsv=glob2.glob("data_each_materials/*_workofadhesion_uniquemillerv3.csv")
 
    df_concat = pd.concat([pd.read_csv(f) for f in allcsv ], ignore_index=True)
    df_concat.to_csv("allworkofadhesion_uniquemiller_nonstov3.csv")
 
    df_concat=df_concat.drop(labels=["Unnamed: 0","composition","composition2","area[A2]","P_boltzman[%]","E_gb[eV]","E_slab[eV]",], axis=1)
    print(df_concat)
    df_concat.to_csv("print_summary.csv")
 
    merged_li6ps5cl=[open("allworkofadhesion_uniquemiller_nonstov3.csv").readlines()[0]]
    for line in open("allworkofadhesion_uniquemiller_nonstov3.csv").readlines()[1:]:
        merged_li6ps5cl.append(line.replace("Li6PS5Cl_S","Li6PS5Cl").replace("Li6PS5Cl_Cl","Li6PS5Cl"))
       
    merged_li6ps5cl="".join(merged_li6ps5cl)
    with open("allworkofadhesion_uniquemiller_nonstov3.csv","w") as f:
        f.write(merged_li6ps5cl)



    merged_na3ps4=[open("allworkofadhesionv3.csv").readlines()[0]]
    for line in open("allworkofadhesionv3.csv").readlines()[1:]:
        merged_na3ps4.append(line.replace("tetra-Na3PS4","Na3PS4").replace("cubic-Na3PS4","Na3PS4"))
       
    merged_na3ps4="".join(merged_na3ps4)
    with open("allworkofadhesionv3_merge_NPS.csv","w") as f:
        f.write(merged_na3ps4)
       
 
    merged_na3ps4=[open("allworkofadhesion_uniquemiller_nonstov3.csv").readlines()[0]]
    for line in open("allworkofadhesion_uniquemiller_nonstov3.csv").readlines()[1:]:
        merged_na3ps4.append(line.replace("tetra-Na3PS4","Na3PS4").replace("cubic-Na3PS4","Na3PS4"))
       
    merged_na3ps4="".join(merged_na3ps4)
    with open("allworkofadhesion_uniquemiller_nonstov3_merge_NPS.csv","w") as f:
        f.write(merged_na3ps4)
       
       
       
    onlystochiometric=[open("allworkofadhesionv3_merge_NPS.csv").readlines()[0]]
    for line in open("allworkofadhesionv3_merge_NPS.csv").readlines()[1:]:
        if line.split(",")[-2]=="True":
            onlystochiometric.append(line)
       
    onlystochiometric="".join(onlystochiometric)
    with open("allworkofadhesionv3_onlystochiometric.csv","w") as f:
        f.write(onlystochiometric)



    onlystochiometric=[open("allworkofadhesion_uniquemiller_nonstov3_merge_NPS.csv").readlines()[0]]
    for line in open("allworkofadhesion_uniquemiller_nonstov3_merge_NPS.csv").readlines()[1:]:
        if line.split(",")[-2]=="True":
            onlystochiometric.append(line)
       
    onlystochiometric="".join(onlystochiometric)
    with open("allworkofadhesion_uniquemiller_v3_merge_NPS_onlystochiometric.csv","w") as f:
        f.write(onlystochiometric)
 
main()
 