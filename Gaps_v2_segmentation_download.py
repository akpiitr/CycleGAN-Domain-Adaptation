#author: Abhishek Kumar Prajapati

from gaps_dataset import gaps

dwnld_directory = 'desired folder'
login_id = 'gapsro3Z=1Yb%7'

gaps.download(login= login_id,
				output_dir= dwnld_directory,
				version='10m', 
				patchsize='segmentation', 
				issue='ASFaLT',)

#Caution: The download may take a while and by default the progress is not displayed. To view the download progress use the code below instead.

# gaps.download(login= login_id,  
# 				output_dir= dwnld_directory,    
# 				version='10m', 
# 				patchsize='segmentation', 
# 				issue='ASFaLT',
# 				debug_outputs=True)


#Log in details
# 'gapsro3Z=1Yb%7' - Abhishek ku. Prajapati 
# Users: Veziroglu, Vedat


'''
Reference:

Stricker, R., Aganian, D., Sesselmann, M., Seichter, D., Engelhardt, M., Spielhofer, R., Hahn, M., Hautz, A., Debes, K., Gross, H.-M.
Road Surface Segmentation - Pixel-Perfect Distress and Object Detection for Road Assessment.
in:  International Conference on Automation Science and Engineering (CASE), Lyon, France, pp. 1-8, IEEE 2021

@inproceedings{stricker2021road,
  title={Road Surface Segmentation - Pixel-Perfect Distress and Object Detection for Road Assessment.},
  author={Stricker, Ronny and Aganian, Dustin and Sesselmann, Maximilian and Seichter, Daniel and Engelhardt, Marius and Spielhofer, Roland and Hahn, Matthias and Hautz, Astrid and Debes, Klaus and Gross, Horst-Michael},
  booktitle={International Conference on Automation Science and Engineering (CASE)},
  pages={1--8},
  year={2021}
}
'''
