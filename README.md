# optimal_multi_airfoil_choice
Script select the best combination possible, based on requirements, for the main wing and the flap.
Designed to work in "automotive field" with low Re.
The (inviscid) library is already build with some of the most common profiles used at this Re, however it's possibile to add your in a very simple and intuitive manner.



# !!IMPORTANT!!
This is just the pre/post processor of a wider program which is able, ones the profiles are selected, to run a panel method and determine by itself what is the best configuration possible.
Essentially Python read/edit the control file used by Matlab® to perform the panel method, which handle the Vallarezo criteria for the multi-profiles wing, and read/plot the results.
Since Matlab® code is still private you should develop yours, use the control.txt contained here just as guidelines or wait until everything will be (ever?) published.
