# Chapter 19
# Practice Project 1
# Extending and Fixing the Chapter Project Programs.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size
os.makedirs('WithLogo', exist_ok=True)

# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.gif') or filename.lower().endswith('.bmp')) or filename == LOGO_FILENAME:
        continue    # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

# Check if image needs to be resized.
    if width >= logoWidth * 2 and height >= logoHeight * 2:

# Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

# Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    else:
        continue

# Add the logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

# Save changes.
    im.save(os.path.join('withLogo', filename))

print('Done')