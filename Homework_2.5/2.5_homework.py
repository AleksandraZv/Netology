import os
import subprocess


def lets_convert():
    cur_dir = os.path.dirname(__file__)
    path = os.path.join(cur_dir, 'Source/')
    try:
        os.makedirs('Result/')
    except OSError:
        pass
    folder = os.listdir(path)

    for pic in folder:
        # convert = (convert, os.path.join(cur_dir, 'Source', pic), '-resize', '200',
        #            os.path.join(cur_dir, 'Result', pic)]
        convert = r'C:\Program Files\ImageMagick-7.0.5-Q16\magick.exe {} -resize 200 {}'.format(os.path.join('Source', pic), os.path.join('Result', pic))
        print(convert)
        subprocess.run(convert)

lets_convert()
