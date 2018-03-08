import random
import tkinter
import tkinter.messagebox


player_wins_number = 0
dealer_wins_number = 0


def start():
    deal_player()
    deal_player()
    deal_dealer()
    if player_score == 21:
        player_count()
        result_text.set("BLACKJACK!!!!!!!!!!!!!!!!")
        if tkinter.messagebox.askokcancel(title="Player wins!", message="Do you want to try again?"):
            restart()
        else:
            quit()


def player_count():
    global player_wins_number
    player_wins_number += 1
    scores.set("PLAYER " + str(player_wins_number) + "-" + str(dealer_wins_number) + " DEALER")


def dealer_count():
    global dealer_wins_number
    dealer_wins_number += 1
    scores.set("PLAYER " + str(player_wins_number) + "-" + str(dealer_wins_number) + " DEALER")


def player_wins():
    result_text.set("Player wins!")
    player_count()
    if tkinter.messagebox.askokcancel(title="Player wins!", message="Do you want to try again?"):
        restart()
    else:
        quit()


def dealer_wins():
    result_text.set("Dealer wins!")
    dealer_count()
    if tkinter.messagebox.askokcancel(title="Dealer wins!", message="Do you want to try again?"):
        restart()
    else:
        quit()


def draw():
    result_text.set("DRAW!")
    if tkinter.messagebox.askokcancel(title="DRAW", message="Do you want to try again?"):
        restart()
    else:
        quit()


def results():
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("PLAYER BUSTED")
        dealer_score_label.set(dealer_score)
        dealer_count()
        if tkinter.messagebox.askokcancel(title="Dealer wins!", message="Do you want to play again?"):
            restart()
        else:
            quit()
    elif player_score <= 21:
        dealer_playing()
        dealer_score_label.set(dealer_score)
        if dealer_score > 21:
            result_text.set("DEALER BUSTED")
            player_count()
            if tkinter.messagebox.askokcancel(title="Player wins!", message="Do you want to play again?"):
                restart()
            else:
                quit()
        elif dealer_score > player_score:
            dealer_wins()
        elif player_score > dealer_score:
            player_wins()
        elif dealer_score == player_score:
            draw()


def restart():
    global dealer_score
    global dealer_card_frame
    global player_score
    global player_card_frame
    global cards
    global deck
    global player_ace
    global dealer_ace
    player_ace = False
    dealer_ace = False
    dealer_score_label.set("x")
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
    dealer_score = 0
    player_score_label.set(0)
    player_score = 0
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)
    result_text.set("")
    cards = []
    load_images(cards)
    deck = list(cards)
    random.shuffle(deck)
    start()


def load_images(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]
    for suit in suits:
        for card in range(1, 11):
            name = "cards/{}_{}.png".format(str(card), suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))
        for card in face_cards:
            name = "cards/{}_{}.png".format(str(card), suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def deal_card(frame):
    next_card = deck.pop(0)
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    return next_card


def deal_dealer():
    global dealer_score
    card_value = deal_card(dealer_card_frame)[0]
    if card_value == 1:
        card_value = 11
    dealer_score += card_value
    dealer_score_label.set("x")


def dealer_playing():
    global dealer_score
    global dealer_ace
    while True:
        if dealer_score < 11:
            card_value = deal_card(dealer_card_frame)[0]
            if card_value == 1:
                card_value = 11
            dealer_score += card_value
        if 11 <= dealer_score < 17:
            random_value = random.randint(1, 4)
            if random_value == 1:
                break
            else:
                card_value = deal_card(dealer_card_frame)[0]
                dealer_score += card_value
        if 11 <= dealer_score <= 19:
            random_value = random.randint(1, 3)
            if random_value == 1:
                card_value = deal_card(dealer_card_frame)[0]
                dealer_score += card_value
            else:
                break
        if dealer_score > 19:
            break


def deal_player():
    global player_score
    global player_ace
    card_value = deal_card(player_card_frame)[0]
    if card_value == 1 and not player_ace:
        player_ace = True
        card_value = 11
    player_score += card_value
    if player_score > 21 and player_ace and (card_value == 11 or card_value == 1):
        player_score -= 10
        player_ace = False
    player_score_label.set(player_score)
    if player_score > 21:
        results()


mainWindow = tkinter.Tk()
mainWindow.title("Blackjack")
mainWindow.geometry("640x400")
mainWindow.configure(background="green")


result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text, bg="green", fg="black")
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=30, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)


dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
dealer_score_label = tkinter.IntVar()
dealer_score = 0
tkinter.Label(card_frame, background="green", text="Dealer",  fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0, pady=50)


player_score_label = tkinter.IntVar()
player_score = 0
player_ace = False
dealer_ace = False


tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0, pady=50)
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)


button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

stop_button = tkinter.Button(button_frame, text="STAND", command=results, bg="green", fg="yellow")
stop_button.grid(row=0, column=2)

player_button = tkinter.Button(button_frame, text="HIT", command=deal_player, bg="green", fg="yellow")
player_button.grid(row=0, column=1)

exit_button = tkinter.Button(button_frame, text="EXIT", command=quit, bg="green", fg="yellow")
exit_button.grid(row=0, column=4)

tkinter.Label(mainWindow, padx=20, bg="green").grid(column=5, row=0)

scores = tkinter.StringVar()
tkinter.Label(mainWindow, textvariable=scores, bg="green", fg="white", relief="raised", padx=10).grid(row=4, column=6)

cards = []
load_images(cards)
deck = list(cards)
random.shuffle(deck)


start()

mainWindow.mainloop()
