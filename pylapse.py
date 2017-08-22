import pygame
import pygame.camera
import time

RES = (1280, 720) # image resolution
WINDOWSIZE = (854, 480) # preview resolution
FILEPREFIX = 'capture' # file prefix
TIMEDELAY = 60 # seconds of delay
PREVIEWDELAY = .3 # preview delay

def stream():
    # init
    pygame.init()
    pygame.camera.init() 
    # config window to preview size
    display = pygame.display.set_mode(WINDOWSIZE, 0)
    # config camera to image resolution
    camera = pygame.camera.Camera(pygame.camera.list_cameras()[0], RES)
    camera.start()
    # config screen
    screen = pygame.surface.Surface(WINDOWSIZE, 0, display)
    # start time for recording
    starttime = int(time.time())
    # file counter
    counter = 0

    looping = True
    while looping:
        # check for exit event
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                looping = False
        # current time in recording for filename
        currenttime = time.localtime()
        # current time in unix time
        newtime = int(time.time())
        # get an image from webcame
        capture = camera.get_image()
        # scale the image to screen
        screen = pygame.transform.scale(capture, WINDOWSIZE)
        display.blit(screen, (0,0))
        pygame.display.flip()
        # if set duration has passed
        if newtime - starttime > TIMEDELAY:
            # save the image with timestamp
            pygame.image.save(capture, FILEPREFIX + '_' + str(counter) + '_' + str(currenttime.tm_mon) + '_' + str(currenttime.tm_mday) + '_' + str(currenttime.tm_hour) + '_' + str(currenttime.tm_min) + '_' + str(currenttime.tm_sec)) + '.tga'
            # update time
            starttime = newtime
            # increase file count
            counter = counter + 1
        elif looping:
            # slow down loop
            time.sleep(PREVIEWDELAY)


if __name__ == '__main__':
    stream()
