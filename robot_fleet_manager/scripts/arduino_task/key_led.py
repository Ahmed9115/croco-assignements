import pygame
import rospy
from robot_fleet_manager.msg import custom

pygame.init()
screen = pygame.display.set_mode((600 , 400))
run = True
running = False


if __name__ == '__main__' :

    rospy.init_node("talker")
    pub = rospy.Publisher("keyboard" , custom , queue_size = 10)
    msg = custom()



while run :
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                running = False


        if running == True :
            msg.key = "q"

        else :
            msg.key = "w"


        pub.publish(msg)


pygame.quit()
              