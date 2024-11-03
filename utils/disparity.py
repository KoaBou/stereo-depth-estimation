import cv2
import numpy as np

def disparity_map(imgL, imgR, params):
    # Setting parameters for StereoSGBM algorithm
    

    stereo = cv2.StereoSGBM_create(minDisparity = params['minDisparity'],
        numDisparities = params['numDisparities'],
        blockSize = params['blockSize'],
        disp12MaxDiff = params['disp12MaxDiff'],
        uniquenessRatio = params['uniquenessRatio'],
        speckleWindowSize = params['speckleWindowSize'],
        speckleRange = params['speckleRange']
    )
    # Calculating disparith using the StereoSGBM algorithm
    disp = stereo.compute(imgL, imgR).astype(np.float32)
    disp = cv2.normalize(disp,0,255,cv2.NORM_MINMAX)
    
    return disp


if __name__ == '__main__':
    imgL = cv2.imread('/home/ngin/FPT/FA24/CPV391/labs/final_project/data/MiddleBury/Art-2views/Art/view1.png', 0)
    imgR = cv2.imread('/home/ngin/FPT/FA24/CPV391/labs/final_project/data/MiddleBury/Art-2views/Art/view5.png', 0)
    
    params = {
        'minDisparity': 0,
        'numDisparities': 16,
        'blockSize': 15,
        'disp12MaxDiff': 1,
        'uniquenessRatio': 1,
        'speckleWindowSize': 100,
        'speckleRange': 32
    }
    
    disparity = disparity_map(imgL, imgR, params)
    # Resize images to the same height

    cv2.imshow('Disparity', disparity)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


