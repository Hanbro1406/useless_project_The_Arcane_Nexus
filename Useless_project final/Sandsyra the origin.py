import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sandsyra The origin: a visual novel")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
background_intro = pygame.image.load('background_intro.jpg')
background_level_one = pygame.image.load('background_level_one.jpg')
l2 = pygame.image.load('24.jpg')
background_level_three = pygame.image.load('background_level_four.jpg')
background_level_five = pygame.image.load('background_level_five.jpg')
background_level_six = pygame.image.load('background_level_six.jpg')
background_final = pygame.image.load('background_final.jpg')
button1_image = pygame.image.load('button1.png')
button2_image = pygame.image.load('button2.png')
button3_image = pygame.image.load('button3.png')
transition_image_1 = pygame.image.load('transition_image_1.jpg')
transition_image_2 = pygame.image.load('transition_image_2.jpg')
conclusion_yes_button = pygame.image.load('conclusion_yes_button.png')
conclusion_no_button = pygame.image.load('conclusion_no_button.png')
transition_image_no_button = pygame.image.load('conclusion_no_button.png')
a = pygame.image.load('1.jpg')
b = pygame.image.load('B.jpg')
C = pygame.image.load('C.jpg')
z = pygame.image.load('9.jpg')
d = pygame.image.load('10.jpg')
e = pygame.image.load('11.jpg')
f = pygame.image.load('12.jpg')
g = pygame.image.load('13.jpg')
h = pygame.image.load('14.jpg')
j = pygame.image.load('15.jpg')
k = pygame.image.load('16.jpg')
l = pygame.image.load('17.jpg')
m = pygame.image.load('18.jpg')
n = pygame.image.load('19.jpg')
o = pygame.image.load('20.jpg')
p = pygame.image.load('21.jpg')
dr1 = pygame.image.load('22.jpg')
dr2 = pygame.image.load('23.jpg')
bbb = pygame.image.load('222.jpg')


# Load sounds and background music
t_sound = pygame.mixer.Sound('t.wav')
u_sound = pygame.mixer.Sound('u.wav')
v_sound = pygame.mixer.Sound('v.wav')
click_sound = pygame.mixer.Sound('click.wav')
transition_music = pygame.mixer.Sound('transition_sound.wav')
invalid_sound = pygame.mixer.Sound('invalid_answer.wav')
music_intro = 'music_intro.mp3'
music_level_two = 'music_level_two.mp3'
music_level_three = 'music_level_three.mp3'
terror = 'terror.mp3'
music_final = 'music_final.mp3'
win_sound = pygame.mixer.Sound('win_sound.wav')
lose_sound = pygame.mixer.Sound('lose_sound.wav')
love = 'love1.mp3'
music_file = 'love.mp3'
music_file = 'music_story.mp3'

def draw_text_in_box(text, x, y, width, height, color, bgcolor):
    # Draw the box
    pygame.draw.rect(screen, bgcolor, (x, y, width, height))
    pygame.draw.rect(screen, color, (x, y, width, height), 2)  # Optional: Border
    
    # Render the text
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)



# Font
font = pygame.font.Font(None, 36)

# Functions
def play_transition():
    pygame.mixer.Sound.play(transition_music)
    pygame.time.delay(2000)

def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)

def draw_text(text, x, y):
    # Ensure text is a string
    if not isinstance(text, str):
        text = str(text)  # Convert to string if it's not
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))


def display_transition(slides):
    for slide in slides:
        # Assuming each slide is structured as {'background': image, 'text_lines': [...]}
        background = slide['background']
        text_lines = slide['text_lines']

        # Draw the background for each slide
        screen.blit(background, (0, 0))
        
        y_offset = 100
        for line in text_lines:
            draw_text(line, 50, y_offset)
            y_offset += 50
        draw_text("Click to continue...", WIDTH // 2 - 100, HEIGHT - 100)
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(click_sound)
                    waiting = False
    return True

def fade_in(surface, duration=1500):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.fill((0, 0, 0))  # Black overlay for fade effect
    for alpha in range(255, 0, -5):  # Fade from black (alpha 255) to clear
        overlay.set_alpha(alpha)
        screen.blit(surface, (0, 0))
        screen.blit(overlay, (0, 0))
        pygame.display.flip()
        pygame.time.delay(duration // 51)

def fade_out(surface, duration=2000):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.fill((0, 0, 0))  # Black overlay for fade effect
    for alpha in range(0, 255, 5):  # Fade from clear (alpha 0) to black
        overlay.set_alpha(alpha)
        screen.blit(surface, (0, 0))
        screen.blit(overlay, (0, 0))
        pygame.display.flip()
        pygame.time.delay(duration // 51)

def display_intro(intro_scenes, music_file, display_time=4200):
    play_music(music_file)  # Start intro music
    for scene in intro_scenes:
        background = scene['background']
        text_lines = scene['text_lines']

        # Display the background and text
        screen.blit(background, (0, 0))
        y_offset = 100
        for line in text_lines:
            draw_text(line, 50, y_offset)
            y_offset += 50
        pygame.display.flip()

        # Fade in effect for the scene
        fade_in(screen.copy())

        # Wait for a specified time before moving to the next scene
        pygame.time.delay(display_time)

        # Fade out effect after the scene
        fade_out(screen.copy())

    pygame.mixer.music.stop()  # Stop intro music at the end of intro
    return True


# Setup intro scenes with images and text lines
intro_scenes1 = [
    {'background': b, 'text_lines': []},
    {'background': a, 'text_lines': []},
    {'background': C, 'text_lines': []}
]

# Call display_intro at the start of the game
display_intro(intro_scenes1, love)

def story(story_scenes, music_file, display_time=4000):
    play_music(music_file)  # Start story music
    for scene in story_scenes:
        background = scene['background']
        text_lines = scene['text_lines']

        # Fade in effect for the scene
        fade_in(background)

        # Display the background and text
        screen.blit(background, (0, 0))
        y_offset = 100
        for line in text_lines:
            draw_text(line, 50, y_offset)
            y_offset += 50
        pygame.display.flip()

        # Wait for a specified time before moving to the next scene
        pygame.time.delay(display_time)

        # Fade out effect after the scene
        fade_out(screen.copy())

    pygame.mixer.music.stop()  # Stop story music at the end of story
    return True

# Define the story scenes
story_scenes = [
    {'background': z, 'text_lines': [
        "In a high-tech laboraory filled with the hum of machines two brilliant scientists, ",
        "Jonas and Martha, shared a deep bond forged through love and a passion for discovery."
    ]},
    {'background': d, 'text_lines': [
        "One day, an unexpected explosion happened in the lab...",
        "Martha was gone forever, leaving Jonas in greif."
    ]},
    {'background': e, 'text_lines': [
        "Jonas decided to rewrite the past...",
        "So he started building a time machine"
    ]},
    {'background': f, 'text_lines': [
        "Afters years of hardwork, he finally succeeded building time machine...",
        "He was on his mission: to prevent the explosion that took Martha away from him."
    ]},
    {'background': g, 'text_lines': [
        "He reached the past",
        "With a bold nature he walked towards the doors"
    ]},
]

# Example call to the story function
story_music = 'music_story.mp3'  # Replace with your story music file
story(story_scenes, story_music)




def intro():
    play_music(music_intro)
    screen.blit(background_final, (0, 0))
    draw_text("Welcome to 'Sandsyra: The Origin'!", 50, 50)
    draw_text("You are a Time Traveler and you have come to past to save your wife", 50, 100)
    draw_text("Make your choices wisely, but remember: You have only one chance.", 50, 150)
    draw_text("So monuse, all the best!....", 50, 200)
    pygame.display.flip()
    pygame.time.delay(7000)


def i():
    play_music(music_level_two)
    screen.blit(background_intro, (0, 0))

def hi():
    play_music(terror)
    screen.blit(background_intro, (0, 0))

def level_one():
    play_transition()
    play_music(music_intro)
    
    waiting = True
    while waiting:
        screen.blit(dr2, (0, 0))
        draw_text("You are looking around and ensures no one is present", 50, 50)
        draw_text("You have three doors in front of you. One will open the way to the next level.", 50, 100)
        
        # Draw doors and labels
        draw_text("1", 150, 250)
        screen.blit(button1_image, (150, 250))  # Door 1
        draw_text("2", 500, 250)
        screen.blit(button2_image, (500, 250))  # Door 2
        draw_text("3", 850, 250)
        screen.blit(button3_image, (850, 250))  # Door 3
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                pygame.mixer.Sound.play(click_sound)
                
                # Check if Door 1 is clicked
                if 150 <= mouse_x <= 150 + button1_image.get_width() and 250 <= mouse_y <= 250 + button1_image.get_height():
                    display_transition([
                        {'background': dr2, 'text_lines': ["This door is locked. Try another door."]}
                    ])
                    
                    
                # Check if Door 2 is clicked 
                elif 500 <= mouse_x <= 500 + button2_image.get_width() and 250 <= mouse_y <= 250 + button2_image.get_height():
                    display_transition([
                        {'background': dr2, 'text_lines': ["Good choice! You found the correct door. Proceeding to the next level..."]}
                    ])
                    waiting = False 
                    return True
                
                # Check if Door 3 is clicked 
                elif 850 <= mouse_x <= 850 + button3_image.get_width() and 250 <= mouse_y <= 250 + button3_image.get_height():
                    display_transition([
                        {'background': dr2, 'text_lines': ["This door is locked. Try another door."]}
                    ])
                    

    return False



def level_two():
    play_transition()
    play_music(music_level_two)
    
    # Initialize variables for attempts
    attempts = 3
    number = str(random.randint(100, 999))  

    while attempts > 0:
        # Display the random number 
        screen.blit(l2, (0, 0))
        draw_text(f"Memorize this number: {number}", 50, 50)
        pygame.display.flip()
        pygame.time.delay(1000)  # Display number for 1 second

        # Clear the number from the screen
        screen.blit(l2, (0, 0))
        draw_text("Enter the number shown previously to continue:", 50, 50)
        pygame.display.flip()

        user_input = ''
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                elif event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(click_sound)
                    if event.key == pygame.K_RETURN:
                        if user_input == number:
                            return True  # Correct number entered
                        else:
                            pygame.mixer.Sound.play(invalid_sound)  
                            attempts -= 1
                            user_input = ''  # Clear input for retry
                            waiting = False  # End current attempt
                    elif event.key == pygame.K_BACKSPACE:
                        user_input = user_input[:-1]
                    else:
                        user_input += event.unicode

            # Update with user input
            screen.blit(l2, (0, 0))
            draw_text("Enter the number shown previously to continue:", 50, 50)
            draw_text(user_input, 50, 100)
            pygame.display.flip()

        # If attempts reach 3, generate a new number
        if attempts == 0:
            attempts = 3  # Reset attempts
            number = str(random.randint(100, 999))  
            draw_text("Generating a new number...", 50, 150)
            pygame.display.flip()
            pygame.time.delay(2000) 


def level_three():
    play_transition()
    play_music(music_level_three)
    screen.blit(dr2, (0, 0))
    draw_text("Rearrange the letters to form a word: 'ADNSYSAR'", 50, 50)
    correct_answer = "SANDSYRA"
    pygame.display.flip()

    user_input = ''
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN:
                pygame.mixer.Sound.play(click_sound)
                if event.key == pygame.K_RETURN:
                    if user_input.upper() == correct_answer:
                        return True
                    else:
                        pygame.mixer.Sound.play(invalid_sound)  # Play invalid sound
                        user_input = ''  # Clear the input for retry
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        screen.blit(dr2, (0, 0))
        draw_text("Rearrange the letters to form a word: 'ADNSYSAR' Clue: It's the name u saw at first", 50, 50)
        draw_text(user_input.upper(), 50, 100)
        pygame.display.flip()

def level_four():
    play_transition()
    play_music(music_level_three)
    screen.blit(j, (0, 0))
    draw_text("Press SPACE inorder to hide!!", 50, 50)
    pygame.display.flip()
    
    correct_timing = random.randint(1, 3)
    pygame.time.delay(correct_timing * 1000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if pygame.time.get_ticks() % correct_timing == 0:
                        return True
                    else:
                        pygame.mixer.Sound.play(invalid_sound)
                        pygame.time.delay(2000)

def level_five():
    # XOX game setup
    play_transition()
    play_music(music_level_three)
    screen.blit(k, (0, 0))
    draw_text("Play XOX against Computer inorder to get the access to server!", 50, 50)
    pygame.display.flip()

    # Board and game variables
    def reset_board():
        return [["" for _ in range(3)] for _ in range(3)]

    board = reset_board()
    player_turn = True  
    cell_size = 200
    margin_x, margin_y = (WIDTH - cell_size * 3) // 2, (HEIGHT - cell_size * 3) // 2

    # Draws the game board
    def draw_board():
        screen.blit(background_level_six, (0, 0))
        for row in range(3):
            for col in range(3):
                x = margin_x + col * cell_size
                y = margin_y + row * cell_size
                pygame.draw.rect(screen, WHITE, (x, y, cell_size, cell_size), 3)
                if board[row][col] == "X":
                    draw_text("X", x + cell_size // 2 - 10, y + cell_size // 2 - 10)
                elif board[row][col] == "O":
                    draw_text("O", x + cell_size // 2 - 10, y + cell_size // 2 - 10)
        pygame.display.flip()

    # Checks for a win or draw
    def check_win():
        for row in board:
            if row[0] == row[1] == row[2] != "":
                return row[0]
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != "":
                return board[0][col]
        if board[0][0] == board[1][1] == board[2][2] != "":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != "":
            return board[0][2]
        return None

    # AI randomly chooses an empty spot
    def ai_move():
        empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            board[row][col] = "O"

    # XOX Game Loop
    while True:
        draw_board()
        winner = check_win()
        if winner:
            pygame.mixer.Sound.play(win_sound if winner == "X" else lose_sound)
            draw_text("You Win!" if winner == "X" else "You Lose!", WIDTH // 2 - 50, HEIGHT // 2)
            pygame.display.flip()
            pygame.time.delay(3000)
            
            if winner == "O":  
                pygame.time.delay(2000)
                board = reset_board()   
                player_turn = True    
                continue               
            return winner == "X"  
        
        # Check for draw

        if all(cell != "" for row in board for cell in row):
            draw_text("It's a Draw!", WIDTH // 2 - 50, HEIGHT // 2)
            pygame.display.flip()
            pygame.time.delay(2000)  
            board = reset_board()     
            player_turn = True        
            continue                 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if player_turn and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col = (mouse_x - margin_x) // cell_size
                row = (mouse_y - margin_y) // cell_size
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == "":
                    board[row][col] = "X"
                    player_turn = False
            elif not player_turn:
                pygame.time.delay(500)
                ai_move()
                player_turn = True  



                 


def final_level():
    play_transition()
    play_music(music_final)
    screen.blit(background_final, (0, 0))
    draw_text("You have reached the final level. Choose wisely.", 50, 50)
    draw_text("Press 'A' to avoid pressing the button.", 50, 100)
    draw_text("Press 'B' to press the button.", 50, 150)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.KEYDOWN:
                pygame.mixer.Sound.play(click_sound)

                # Option 'A' - Do not press the button, end the game with one conclusion
                if event.key == pygame.K_a:
                    display_transition([
                        {'background': background_final, 'text_lines': ["You chose not to press the button. Perhaps this was the wiser choice..."]}
                    ])
                    conclusion_no_button()
                    return False

                # Option 'B' - Choose to press the button, prompt confirmation
                elif event.key == pygame.K_b:
                    draw_text("Are you sure? Press 'Y' to confirm, 'N' to go back.", 50, 200)
                    pygame.display.flip()
                    confirm = True

                    # Confirm choice loop
                    while confirm:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                pygame.mixer.Sound.play(click_sound)
                                
                                # Confirm 'Yes' - Trigger conclusion for pressing the button
                                if event.key == pygame.K_y:
                                    display_transition([
                                        {'background': transition_image_1, 'text_lines': ["You pressed the button... consequences unfold."]}
                                    ])
                                    conclusion_yes_button()
                                    return False  # End the game

                                # Confirm 'No' - Trigger alternate conclusion for not pressing after reconsideration
                                elif event.key == pygame.K_n:
                                    display_transition([
                                        {'background': transition_image_2, 'text_lines': ["You chose not to press the button after reconsidering. Perhaps this was the wiser choice..."]}
                                    ])
                                    conclusion_no_button_retry()
                                    return False  # End the game with alternate outcome

    return False

def conclusion_yes_button():
    screen.blit(n, (0, 0))
    draw_text("You pressed the button, sealing your fate. But it triggered the blast", 50, 50)
    draw_text("She is dead!!!", 50, 200)
    pygame.display.flip()
    pygame.time.delay(6000)

def conclusion_no_button():
    screen.blit(n, (0, 0))
    draw_text("You decided not to press the button. But suddenly a lizard fell onto the button", 50, 50)
    draw_text("3.2.1, Boom!! She is gone!!!", 50, 200)
    pygame.display.flip()
    pygame.time.delay(6000)

def conclusion_no_button_retry():
    screen.blit(n, (0, 0))
    draw_text("You reconsidered and stepped back. A new path may await...", 50, 50)
    draw_text("But suddenly a lizard fell onto the button", 50, 100)
    draw_text("3.2.1, Boom!! She is gone!!!", 50, 200)
    pygame.display.flip()
    pygame.time.delay(6000)




def level_six():
    play_transition()
    screen.fill(BLACK)
    draw_text("Access the computer and locate the file with the sound pattern.", 50, 50)
    pygame.display.flip()
    pygame.time.delay(3000)

    # Setup for the computer interface simulation
    folders = ["Documents", "Music", "Sandsyra"]
    sound_files = ["SoundCode.txt", "Notes.txt", "Readme.txt"]
    correct_file = "SoundCode.txt"  # Only this file contains the sound pattern
    
    # Define the sound pattern as a sequence of sounds
    sound_pattern = [t_sound, u_sound, v_sound]
    sound_buttons = [t_sound, u_sound, v_sound]
    user_pattern = []

    def display_computer_interface():
        screen.fill(BLACK)
        draw_text("Computer Desktop", WIDTH // 2 - 100, 50)
        for idx, folder in enumerate(folders):
            draw_text(folder, 100, 150 + idx * 100)
        pygame.display.flip()

    def display_folder_contents():
        screen.fill(BLACK)
        draw_text("Folder: Sandsyra", WIDTH // 2 - 100, 50)
        for idx, file in enumerate(sound_files):
            draw_text(file, 100, 150 + idx * 100)
        pygame.display.flip()

    def play_sound_pattern():
        for sound in sound_pattern:
            pygame.mixer.Sound.play(sound)
            pygame.time.delay(800)  

    # To: Display computer desktop and folders
    in_computer = True
    in_folder = False
    while in_computer:
        display_computer_interface()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if 100 <= mouse_x <= 300:  
                    if 150 <= mouse_y <= 250:
                        in_folder = True
                        break
                    elif 250 <= mouse_y <= 350:
                        in_folder = True
                        break
                    elif 350 <= mouse_y <= 450:
                        in_folder = True
                        break
        
        #To Navigate to folder and find sound file
        while in_folder:
            display_folder_contents()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if 100 <= mouse_x <= 400:
                        if 150 <= mouse_y <= 250:
                            if sound_files[0] == correct_file:
                                play_sound_pattern()  
                                pygame.time.delay(2000)
                                in_computer = False  
                                in_folder = False
                                break
                            else:
                                draw_text("Nothing here.", WIDTH // 2 - 50, HEIGHT // 2)
                                pygame.display.flip()
                                pygame.time.delay(1000)

    #Must do the same sound pattern
    screen.fill(BLACK)
    draw_text("Repeat the sound pattern by pressing the buttons in order!", 50, 50)
    pygame.display.flip()
    
    button_positions = [(200, 400), (500, 400), (800, 400)]  
    for idx, pos in enumerate(button_positions):
        pygame.draw.rect(screen, WHITE, (*pos, 100, 100))
        draw_text(str(idx + 1), pos[0] + 30, pos[1] + 30)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for idx, pos in enumerate(button_positions):
                    if pos[0] <= mouse_x <= pos[0] + 100 and pos[1] <= mouse_y <= pos[1] + 100:
                        pygame.mixer.Sound.play(sound_buttons[idx])  
                        user_pattern.append(sound_buttons[idx])  

                        if len(user_pattern) == len(sound_pattern):
                            if user_pattern == sound_pattern:
                                # Display "Correct!!!" at the top
                                draw_text("Correct!!!", WIDTH // 2 - 100, 70)  
                                pygame.display.flip()
                                pygame.time.delay(3000)
                                return True
                            else:
                                # "Incorrect pattern! Try again!
                                draw_text("Incorrect pattern! Try again.", WIDTH // 2 - 100, 90)
                                pygame.display.flip()
                                pygame.time.delay(2000)
                                user_pattern = []




def play_game():
    intro()
    display_transition([
        {'background': g, 'text_lines': [
            "After narrowly escaping, you see three doors in front of you.",
        ]}
    ])

    if level_one():
        display_transition([
            {'background': dr1, 'text_lines': ["after passing through the doors."]},
            {'background': dr1, 'text_lines': ["He heads towards a computer passcode hacking device."]},
        ])


        if level_two():
            display_transition([
            {'background': h, 'text_lines': ["he is then asked to spell a word"]},
            ])

            if level_three():
                hi()
                display_transition([
                {'background': dr2, 'text_lines': ["He solved it and proceeded to hall"]},
                {'background': j, 'text_lines': ["on the way he met a big robot."]},
                ])

                if level_four():
                    i()
                    display_transition([
                    {'background': bbb, 'text_lines': ["After narrowly escaping, he goes towards the server room."]},
                    {'background': k, 'text_lines': ["He is tired!!"]},
                    ])

                    if level_five():
                        display_transition([
                        {'background': l, 'text_lines': ["now he goes towards the main computer inorder to gain access"]},
                        {'background': l, 'text_lines': ["He is breathing heavily"]},
                        ])
                        if level_six():
                            display_transition([
                            {'background': g, 'text_lines': ["He rushed towards the button"]},   
                            {'background': m, 'text_lines': ["After all these efforts"]},
                            {'background': m, 'text_lines': ["He has finally reached near the button."]},
                            ])
                              
                            if final_level():
                                    pass
    display_transition([
                            {'background': o, 'text_lines': ["After narrowly escaping, you find yourself in an unfamiliar place."]},
                            {'background': o, 'text_lines': ["Strange symbols surround you, hinting at a deeper mystery ahead."]},
                            {'background': background_final, 'text_lines': ["A path lies ahead, leading to unknown challenges."]},
                            {'background': background_final, 'text_lines': ["Stay focused and proceed with caution, as danger awaits."]}
                            ])
    conclusion()

def conclusion():
    screen.blit(p, (0, 0))
    draw_text("You are the one who made this to happen. You are useless!!! Nee enth paranjalum karyam illa.", 50, 50)
    draw_text(" You are the reason for her death", 50, 100)
    draw_text("This is a practical case for Predestination Paradox", 50, 150)
    draw_text("Thank you for playing!", 50, 200)
    pygame.display.flip()
    pygame.time.delay(6000)

# Start the game
play_game()
pygame.quit()