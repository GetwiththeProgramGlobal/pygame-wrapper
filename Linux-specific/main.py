#!/usr/bin/env bash

import pygame, project

def main():
    pygame.init()
    project.setup()

    while not project.quit(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                project.quit()

            if event.type == pygame.KEYDOWN:
                project.setLastDown(event.key)

            if event.type == pygame.KEYUP:
                project.setLastUp(event.key)
        
        project.update()
        project.drawSprites()
        pygame.display.flip()

        project.deltaTime(True)

        # Late reset of single key events
        project.setLastDown(-1)
        project.setLastUp(-1)
    pygame.quit()

if __name__ == '__main__':
    main()