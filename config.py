"""Config File"""

table_w = []

table_f = []

solution_w = []

solution_f = []

file_name_f = []

file_name_w = []

path = []



#%% Functions

def index_tuple_check( index , AoA, path, name, a ):           # Function to extract the index in case of AoA is not
															   # listed in the specific profile under investigation

	global val                                                 # Define as global to get the value on the main!!

	import numpy as np

	if AoA in a:                                               # if AoA is listed val is exactly the index
															   # corresponding to AoA in vector a

		val = index

		return val

	else :                                                     # In case of no value get a lower one

		print('Data set not available for {} at {}, lowering value of the angle of attack to {}'.format(
			str(name[(path.count('') + 11):]), AoA, AoA - 0.5))

		AoA -= 0.5                                             # Reduce AoA

		index_tuple = np.where(a == AoA)                       # Get the index of the AoA in vector a

		index = index_tuple[0]

		index_tuple_check( index, AoA, path, name, a )         # RECURSIVE FUNCTION: Guarantee that, if AoA is still
															   # not listed in a, the program do another iteration.
															   # Iterations will stop when "index_tuple" will return
															   # a value different from "None"

		return val



def central_first_order_derivate( f, h ):

	df = ( -f[0] + f[2]) / ( 2*h )

	return df



def forward_first_order_derivate( f, h ):

	df = ( -f[0] + f[ 1 ]) / h

	return df



def backward_first_order_derivate( f, h ):

	df = ( -f[0] + f[1]) / h

	return df



def load_file_results( path ):

	import numpy as np

	results_txt = str( path + '/Hess-Smith/nprofili/results.txt')  # Select automatically the correct file

	try:

		results = np.loadtxt(results_txt, skiprows=2)  # Matrix of the imported data

		return results

	except OSError:

		print( 'File "results.txt" NOT FOUND')

		path = input('\nSpecify the path in which the Matlab® output "results.txt" is located: ')

		if path == 'exit':

			print(col.colored('Exit selected\nAbort operation...', on_color='on_red'))

			return

		else:

			load_file_results( path )

