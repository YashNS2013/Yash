import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Ramayana Quiz")

font = pygame.font.SysFont(None, 60)
bigfont = pygame.font.SysFont(None, 60)

questions = [
    {
        "q": "Who is the father of Lord Rama?",
        "options": ["Dasharatha", "Janaka", "Ravana"],
        "answer": 0
    },
    {
        "q": "Who was abducted by Ravana?",
        "options": ["Lakshmana", "Sita", "Kaikeyi"],
        "answer": 1
    },
    {
        "q": "Who helped Rama build the bridge to Lanka?",
        "options": ["Hanuman", "Sugriva", "Vibhishana"],
        "answer": 0
    },
    {
        "q": "Who was Rama's loyal brother?",
        "options": ["Bharata", "Lakshmana", "Shatrughna"],
        "answer": 1
    },
    {
        "q": "What was the name of Rama's kingdom?",
        "options": ["Ayodhya", "Mithila", "Kishkindha"],
        "answer": 0
    }
]

score = 0
current = 0
selected = -1
feedback = ""

def draw_question(qdata, selected, feedback):
    screen.fill((245, 222, 179))
    instructions = font.render("Click an option or press 1/2/3 to select.", True, (0, 0, 128))
    screen.blit(instructions, (50, 10))
    question = font.render(qdata["q"], True, (139, 69, 19))
    screen.blit(question, (50, 60))
    for i, opt in enumerate(qdata["options"]):
        color = (0, 128, 0) if i == selected else (0, 0, 128)
        opt_text = font.render(f"{i+1}. {opt}", True, color)
        screen.blit(opt_text, (50, 150 + i*60))
    if feedback:
        fb_text = font.render(feedback, True, (200, 0, 0))
        screen.blit(fb_text, (50, 400))
    pygame.display.flip()

running = True
wait_next = False
while running:
    if current < len(questions):
        draw_question(questions[current], selected, feedback)
    else:
        screen.fill((245, 222, 179))
        result = bigfont.render(f"Quiz Over! Score: {score}/{len(questions)}", True, (0,128,0))
        screen.blit(result, (150, 250))
        pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif current < len(questions):
            if event.type == pygame.KEYDOWN and not wait_next:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                    selected = event.key - pygame.K_1
                    if selected == questions[current]["answer"]:
                        feedback = "Correct!"
                        score += 1
                    else:
                        feedback = "Incorrect!"
                    wait_next = True
                    pygame.time.set_timer(pygame.USEREVENT, 1200)
            elif event.type == pygame.MOUSEBUTTONDOWN and not wait_next:
                mx, my = pygame.mouse.get_pos()
                for i in range(3):
                    if 50 <= mx <= 400 and 150 + i*60 <= my <= 190 + i*60:
                        selected = i
                        if selected == questions[current]["answer"]:
                            feedback = "Correct!"
                            score += 1
                        else:
                            feedback = "Incorrect!"
                        wait_next = True
                        pygame.time.set_timer(pygame.USEREVENT, 1200)
            elif event.type == pygame.USEREVENT and wait_next:
                current += 1
                selected = -1
                feedback = ""
                wait_next = False
                pygame.time.set_timer(pygame.USEREVENT, 0)

pygame.quit()
sys.exit()


