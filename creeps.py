# Main Game Loop

while True:
    # Limit FPS to 50

    time_passed = clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()

    # Redraw the background
    screen.fill(BG_COLOR)

    # Update and redraw all the creeps
    for creep in creeps:
        creep.update(time_passed)
        creep.blitme()

    pygame.display.flip()