
def pallette_generator(image_file):
    import numpy as np
    '''
    Returns the top five colors used in
    and image and the corresponding
    percentage in the form of list of
    five tuples:
    [(color, percent), (color, percent), ..]
    each color is in the form of a three-element'
    list color = [r, g, b].
    '''
    # Color data
    Hexlist = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

    pixels = {}

    dims = image_file.shape

    imax, jmax = dims[0:2]

    for i in range(0,imax,5):
        for j in range(0,jmax,5):
            pixel = image_file[i, j]
            x,y = divmod(pixel[0], 16)
            xp,yp = divmod(pixel[1], 16)
            xpp,ypp = divmod(pixel[2], 16)

            pixel_hex = "".join([Hexlist[i] for i in [x,y,xp,yp,xpp,ypp]])

            if pixel_hex not in pixels:
                pixels[pixel_hex] = 1
            else:
                pixels[pixel_hex] += 1

    total_count = len(pixels)

    spread = np.linspace(0,total_count//2,5)

    spread = spread.tolist()

    for i in range(len(spread)):
        spread[i] = int(spread[i])

    #sort dictionary keys
    sorted_pixels = sorted(pixels.items(), key = lambda kv: kv[1])
    return [sorted_pixels[i][0] for i in spread]