def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    first_row = "Red" if redShirtHeights[0] < blueShirtHeights[0] else "Blue"
    for i in range(len(redShirtHeights)):
        red_height = redShirtHeights[i]
        blue_height = blueShirtHeights[i]
        if first_row == "Red":
            if red_height >= blue_height:
                return False
        else:
            if blue_height >= red_height:
                return False
    return True
