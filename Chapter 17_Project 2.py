# Chapter 17
# Practice Project 2

# Check & download updated comic from www.xkcd.com everyday automatically.
# And more archived comics to other file accordingly.

import requests, bs4, os, shutil

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
os.makedirs('Archive', exist_ok = True)

def checkComic():
    res = requests.get('https://xkcd.com', headers = headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')

        # Check if new comic is updated or not yet.
        comicFile = os.listdir('.')
        if os.path.basename(comicUrl) in comicFile:
            print('No updating available!')
        else:

            # Move all past comics to Archive file.
            for png in comicFile:
                if png.endswith('.png') is True:
                    shutil.move(os.path.join('.',png),os.path.join('.','Archive'))
            print('Last comic has moved to Archive file, and...')
            print('Downloading new comic...')

            # Save the latest comic from website.
            res = requests.get('https:' + comicUrl)
            imageFile = open(os.path.join('.',os.path.basename(comicUrl)),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
            print('Done')

checkComic()