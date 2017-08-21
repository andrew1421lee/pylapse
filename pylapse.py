import pygame
import pygame.camera
import time

RES = (1280, 720)
WINDOWSIZE = (854, 480)
FILEPREFIX = 'capture'

def stream():
    pygame.init()
    pygame.camera.init()
    display = pygame.display.set_mode(WINDOWSIZE, 0)
    camera = pygame.camera.Camera(pygame.camera.list_cameras()[0], RES)
    camera.start()
    screen = pygame.surface.Surface(WINDOWSIZE, 0, display)
    starttime = int(time.time())
    counter = 0

    while True:
        currenttime = time.localtime()
        newtime = int(time.time())
        capture = camera.get_image()
        screen = pygame.transform.scale(capture, WINDOWSIZE)
        display.blit(screen, (0,0))
        pygame.display.flip()
        if newtime - starttime > 60:
            pygame.image.save(capture, FILEPREFIX + '_' + str(counter) + '_' + str(currenttime.tm_mon) + '_' + str(currenttime.tm_mday) + '_' + str(currenttime.tm_hour) + '_' + str(currenttime.tm_min) + '_' + str(currenttime.tm_sec))
            starttime = newtime
            counter = counter + 1


if __name__ == '__main__':
    stream()
