"""Post processor"""
#%% Import section

import numpy as np

import config;      AoA = config.AoA;       path = config.path

import matplotlib.pyplot as mp

import os



#%% Search & Load result file & remove temporary file "header_results.txt"

results = config.load_file_results( path )

os.remove( path + '/Hess-Smith/nprofili/header_results.txt')



#%% Global aerodynamic properies from matrix "results"

alpha = results[ :, 0 ]                                             # Get the alpha's vector

Cl = results[ :, 1 ] + results[ :, 2 ]                              # Build Cl from the sum of the column 1 & 2

Cd = results[ :, 3 ] + results[ :, 4 ]                              # Build Cd from the sum of the column 3 & 4

Cm = results[ :, 5 ] + results[ :, 6 ]                              # Build Cm from the sum of the column 5 & 6

E = Cl / Cd



#%% Max Cl configuration

Cl_max = max( Cl )

index_cl_max = Cl.argmax()

prop_cl_max = results[ index_cl_max, : ]



#%% DRS configuration

Cd_min = min( Cd )

index_DRS = Cd.argmin()

prop_DRS = results[ index_DRS, : ]



#%% Summary

alpha_f_cl_max = results[ index_cl_max, 0]                                  # alpha of Cl_max config

Cl_max = results[ index_cl_max, 1] + results[ index_cl_max, 2]              # Cl_max

Cd_cl_max = results[ index_cl_max, 3] + results[ index_cl_max, 4]           # Cd in Cl_max config

Cm_cl_max = results[ index_cl_max, 5] + results[ index_cl_max, 6]           # Cm in Cl_max config

print('\n\nThe MAXIMUM LIFT configuration reach Cl={} at flap angle {}°, main wing angle {}°.\nIn this '
      'configuration the Cd is {} and Cm is {}'.format( Cl_max, alpha_f_cl_max, AoA, Cd_cl_max, Cm_cl_max ))



alpha_f_DRS = results[ index_DRS, 0]                                  # alpha of Cl_max config

Cl_DRS = results[ index_DRS, 1] + results[ index_DRS, 2]              # Cl_max

Cd_DRS = results[ index_DRS, 3] + results[ index_DRS, 4]              # Cd in Cl_max config

Cm_DRS = results[ index_DRS, 5] + results[ index_DRS, 5]              # Cm in Cl_max config

print('\n\nThe DRS configuration to MINIMIZE DRAG have Cd={} at flap angle {}°, main wing angle {}°.\nIn this '
      'configuration the Cl is {} and Cm is {}'.format( Cd_DRS, alpha_f_DRS, AoA, Cl_DRS, Cm_DRS ))



#%% Derivatives

d_Cl = []

d_Cd = []

d_Cm = []

d_alpha_plot = np.linspace( alpha[0], alpha[-1], num = len(alpha)-1)



for i in range( len( Cl ) -1):

	if i == 0:

		d_Cl.append( config.forward_first_order_derivate( Cl[ :i+2]  , (alpha[i+1] - alpha[i]) ))

	elif i == len( Cl ):

		d_Cl.append( config.backward_first_order_derivate( Cl[i-1: ]  , (alpha[i] - alpha[i-1]) ))

	else:

		d_Cl.append( config.central_first_order_derivate( Cl[i-1:i+2]  , (alpha[i] - alpha[i-1]) ))

d_Cl = np.array( d_Cl )



for i in range( len( Cd ) -1):

	if i == 0:

		d_Cd.append( config.forward_first_order_derivate( Cd[ :i+2]  , (alpha[i+1] - alpha[i]) ))

	elif i == len( Cd ):

		d_Cd.append( config.backward_first_order_derivate( Cd[i-1: ]  , (alpha[i] - alpha[i-1]) ))

	else:

		d_Cd.append( config.central_first_order_derivate( Cd[i-1:i+2]  , (alpha[i] - alpha[i-1]) ))

d_Cd = np.array( d_Cd )



for i in range( len( Cm ) -1):

	if i == 0:

		d_Cm.append( config.forward_first_order_derivate( Cm[ :i+2]  , (alpha[i+1] - alpha[i]) ))

	elif i == len( Cd ):

		d_Cm.append( config.backward_first_order_derivate( Cm[i-1: ]  , (alpha[i] - alpha[i-1]) ))

	else:

		d_Cm.append( config.central_first_order_derivate( Cm[i-1:i+2]  , (alpha[i] - alpha[i-1]) ))

d_Cm = np.array( d_Cm )



#%% Plots

cl_alpha= mp.plot( alpha, Cl )

mp.xlabel('Alpha_flap')

mp.ylabel('Lift Coefficient [ Cl ]')

mp.title('CL vs Alpha_flap')

mp.setp( cl_alpha, color = 'r', linewidth = 1.5, marker = '.' )

mp.show()


d_cl = mp.scatter( d_alpha_plot, d_Cl, color = 'b', marker = '.', linewidths = 2.5 )

mp.xlabel('Alpha_flap')

mp.ylabel('Derivative of Lift Coefficient [ d_Cl ]')

mp.title('d_CL/d_alpha')

mp.show()






cd_alpha = mp.plot( alpha, Cd )

mp.xlabel('Alpha_flap')

mp.ylabel('Drag Coefficient [ Cd ]')

mp.title('Cd vs Alpha_flap')

mp.setp( cd_alpha, color = 'r', linewidth = 1.5, marker = '.' )

mp.show()



d_cd = mp.scatter( d_alpha_plot, d_Cd, color = 'b', marker = '.', linewidths = 2.5  )

mp.xlabel('Alpha_flap')

mp.ylabel('Derivative of Drag Coefficient [ d_Cd ]')

mp.title('d_CD/d_alpha')

mp.show()






cm_alpha = mp.plot( alpha, Cl )

mp.xlabel('Alpha_flap')

mp.ylabel('Moment Coefficient [ Cm ]')

mp.title('Cm vs Alpha_flap')

mp.setp( cm_alpha, color = 'r', linewidth = 1.5, marker = '.' )

mp.show()



d_cm = mp.scatter( d_alpha_plot, d_Cm, color = 'b', marker = '.', linewidths = 2.5  )

mp.xlabel('Alpha_flap')

mp.ylabel('Derivative of Momentum Coefficient [ d_Cm ]')

mp.title('d_CM/d_alpha')

mp.show()






e = mp.plot( Cd, Cl)

mp.xlabel('Cd')

mp.ylabel('Cl')

mp.title('Efficiency')

mp.setp( e, color = 'r', linewidth = 1.5, marker = '.' )

mp.show()


