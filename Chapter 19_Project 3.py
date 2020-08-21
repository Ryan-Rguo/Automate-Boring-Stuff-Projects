# Chapter 19
# Practice Project 3

# Custom Seating Cards with resolution 288 x 360 pixels which equals to 5' x 7' frame.

from PIL import Image, ImageDraw, ImageFont
import os

def invitations():

    os.makedirs('invitations', exist_ok = True)
    txt = open('guests.txt','r')
    guests = txt.readlines()

    for i in range(len(guests)):
        im = Image.new('RGBA',(288,360),'white')
        draw = ImageDraw.Draw(im)

        logoIm = Image.open('flower.png')                   # Paste flower decoration picture at the corner.
        im.paste(logoIm,(0,260),logoIm)

        draw.rectangle((0,0,287,359), outline = 'black')    # Drawing the black rectangle along the edge.

        fontsFolder = 'c:\Windows\Fonts'                    # Allocate the fonts used in the invitation.
        titleFont = ImageFont.truetype(os.path.join(fontsFolder,'BRUSHSCI.ttf'),17)
        nameFont = ImageFont.truetype(os.path.join(fontsFolder,'ROCK.TTF'),30)
        dateFont = ImageFont.truetype(os.path.join(fontsFolder,'BELL.TTF'),30)

        guestName = guests[i].rstrip('\n')
        nameWidth, nameHeight = draw.textsize(guestName, nameFont)
        draw.text((17,50),'It would be a pleasure to have the company of', fill = 'black', font = titleFont)        # Add text with specified font accordingly.
        draw.text(((288 - nameWidth) / 2, 100), guestName, fill = 'black', font = nameFont)       # The coordinate is calculated to make sure guest name stays at the centre of the row.
        draw.text((30, 165), 'at 11010 Memory Lane on the Evening of', fill = 'black', font = titleFont)
        draw.text((90, 215), 'April 1st', fill = 'black', font = dateFont)
        draw.text((112,280), "at 7 o'clock", fill = 'black', font = titleFont)

        im.save(os.path.join('invitations', 'invitation_%s.png' % str(i + 1)))      # Save each invitation to the folder with number at the end of filename.

    print('Done')

invitations()