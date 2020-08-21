# Chapter 19
# Practice Project 2

# Identifying Photo Folders on the Hard Drive.
# Hard Drive (E:\) used for the instance.
# A valid photo folder should contain at least 20 photos which is also beyond the amount of non-photo files.
# Only both coordinates of an image file are over 500 pixels can be considered as a photo.

from PIL import Image
import os, pprint, PIL

def photoFolderLocator():
    photoFolder = []
    for foldername, subfolders, filenames in os.walk('E:\\'):
        numPhotoFiles = 0
        numNonPhoto = 0
        for filename in filenames:              # Distinguish image files from non-image files.
            if not filename.lower().endswith('.jpg') or filename.lower().endswith('.png') or filename.lower().endswith('.gif') or filename.lower().endswith('.bmp'):
                numNonPhoto += 1
                continue
            else:
                try:        # Skip the cracked image file.
                    im = Image.open(os.path.join(foldername,filename))
                    width, height = im.size
                except PIL.UnidentifiedImageError:
                    print('CRACKED FILE IS SKIPPED: %s.' % (os.path.join(foldername,filename)))
                    continue
                if width > 500 or height > 500:   # Distinguish photos from other image files.
                    numPhotoFiles +=1
                else:
                    numNonPhoto += 1

        if numPhotoFiles >= numNonPhoto and numPhotoFiles > 20:    # Check photo amount, and percentage in that folder.
            photoFolder.append(foldername)

    pprint.pprint(photoFolder)
    print('Done')

photoFolderLocator()