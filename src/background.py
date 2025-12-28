import pygame 
import cv2

class Backgrounds(pygame.sprite.Sprite):
    def __init__(self, size, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.smoothscale(pygame.image.load(img), size)

class vidbg():
    def __init__(self, filename):
        self.capture = cv2.VideoCapture(filename) 
        while self.capture.isOpened():
            ret, frame  = self.capture.read()
            if ret == True:
                cv2.imshow("frame", frame)
                if cv2.waitKey(30) == ord("q"):
                    break
            else:
                break
