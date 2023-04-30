def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    if not fastest:
        blueShirtSpeeds.sort()
    else:
        blueShirtSpeeds.sort(reverse=True)
    total_speed = 0
    for i in range(len(redShirtSpeeds)):
        red_speed = redShirtSpeeds[i]
        blue_speed = blueShirtSpeeds[i]
        total_speed += max(red_speed, blue_speed)
    return total_speed
