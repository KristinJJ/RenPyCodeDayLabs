
# Player chooses his/her own name.
define MC = Character("[player_name]", color="#c8ffc8")
define reg = Character("Registration Lady", color = "#c4ffc4")
define fade = Fade(0.5, 0.0, 0.5)
define r = Character("Ria", color = "#c1ffc1")


# The game starts here.

label start:

    $ MC = renpy.input("choose a name for the player")
    $ MC = MC.strip()

    scene bg room
    show picture

    play sound "<from 0.0 to 4>alarm-sound.wav"

    # we can add one play music all throught the novel.

    # ACT 1
    "Today is the day of (tournament name). To some students it’s nothing more
    than a fun adventure,with a chance for a big prize. But to me, it’s the
    chance for a wish that could change my life."

    scene bg whitehouse
    with fade

    show reg normal at left
    pause
    show MC normal at right
    pause

    reg "Entry to the competition is $100."

    show MC upset at right

    MC "What? I don’t have that kind of money! I thought entry was $50."

    reg "We raised the prices this year. Some of the obstacles were quite
    expensive this year, you know. Especially the dr- well, nevermind.
    The point is, entry is $100."

    MC "Great..."

    "I look around desperately, and as if on queue, I turn and see my best
    friend, Ria, running towards me."

    show ria happy at center with moveinbottom

    r "MC! You’re entering, right? Let’s enter together!"

    show MC suprised at right

    MC "Ria, you’re entering too? But it’s really dangerous!"

    r "Yeah, but it would be really good if I could get the cash prize.
    I don’t care about the dragon orb, but I wanna be able to move out of my
    parent’s house. Anyway, have you already paid the fee?"

    menu:
        "No, I thought it was $50… can you lend me some money?":
            "Sure, if you promise to team up with me!"

        "Not yet… I don’t know what to do.":
            "I can lend you some, and if you win you have to give me the cash prize!"

    MC "Thank you! I’ll pay you back for sure!"

    "I turn to see Scarlet sneering at me."

    hide reg normal
    show scarlet grinning at left with moveinleft

    "Of course, the spiteful human that
    she is can’t stand to see someone without powers like me win the
    competition. And since this is our last year at (Magic Academy Name),
    it’s our last chance to win the prize we both dearly want: the dragon's orb."







    # This ends the game.

    return
