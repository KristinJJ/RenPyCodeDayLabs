
# Player chooses his/her own name.
define MC = Character("[player_name]", color="#c8ffc8")
define reg = Character("Registration Lady", color = "#c4ffc4")
define s = Character("Scarlet",color = "#E9967A")
define r = Character("Ria", color = "#c1ffc1")
define t = Character("Host", color = "008080")
define fade = Fade(0.5, 0.0, 0.5)



# The game starts here.

label start:

    $ MC = renpy.input("Choose a name for the player")
    $ MC = MC.strip()

    if MC == "":
        $ MC = "MC"



    play sound "<from 0.0 to 4>alarm-sound.wav"

    # we can add one play music all throught the novel.

    # ACT 1
    "Today is the day of {b} {i}Cherry Apple Academy Annual Tounament{/i} {/b}.
    To some students it’s nothing more than a fun adventure,with a chance for a
    big prize. But to me, it’s the chance for a wish that could change my life."

    scene bg whitehouse
    with fade

    stop sound

    play music "music.mp3"

    show reg neutral at left
    pause
    show mc neutral at right with moveinright


    reg "Entry to the competition is $100."

    show mc sad at right

    MC "What? I don’t have that kind of money! I thought entry was $50."

    reg "We raised the prices this year. Some of the obstacles were quite
    expensive this year, you know. Especially the dr- well, nevermind.
    The point is, entry is $100."

    MC "Great..."

    "You look around desperately, and as if on cue, you turn and see your best
    friend, Ria, running towards you."

    show ria happy at center with moveinbottom

    r "%(MC)s! You’re entering, right? Let’s enter together!"

    show mc surprised at right



    MC "Ria, you’re entering too? But it’s really dangerous!"

    show mc neutral at right


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

    hide reg neutral

    scene background

    show scarlet neutral at left with moveinleft
    show mc angry at center with moveinbottom
    show ria neutral at right with moveinright



    "You turn to see Scarlet sneering at you. Of course, the spiteful human
    that she is can’t stand to see someone without powers like you win the
    competition."

    "And since it’s your last year at Cherry Apple Academy for
    Magical Studies, this is the last chance to win the tournament prize we
    both dearly want: the wish-granting dragon's orb."


    show scarlet smirk at left

    s "You're entering? As if you'll have a chance with you know…"



    "She smirks deviously, and looks around as if she wants to say something
    secretive, but raises her voice just loud enough for those nearby to hear."

    s "...your lack of powers. Good luck either way, I guess.
    You'll certainly need it with me in the way."

    show mc sad at center

    "You sigh internally. It’s hard to imagine that the pink-haired demon in front of you had
    once been your best friend. Everything in my life changed once everyone
    realized you had no powers, including my friendship with Scarlet."

    "But now, you have the chance to change your life with the tournament prize,
    and she is not going to get in your way."

    MC "No, I don’t think I need good luck. Even without powers,
    I think I’m perfectly capable of defeating you, thanks."

    #menu:
        #"Save your luck for yourself. I don’t need powers to win."

        #"Even without powers, I think I’m perfectly capable of defeating you, thanks."

    hide ria neutral

    show scarlet grinning at left

    show mc sad:
        xalign 0.5
        linear 0.6 xpos 0.85
    "Scarlet scowls and opens her mouth to retort."
    pause
    "Suddenly, a loud, magnified voice echoes across the clearing."

    scene background

    show Tournament host at center

    t "EVERYONE, ARE YOU READY FOR THE GREATEST TOURNAMENT CHERRY APPLE ACADEMY
    HAS EVER HOSTED?"

    "Yells of assent from the large crowd of participants rise in response."
















    # This ends the game.

    return
