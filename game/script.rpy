
# Player chooses his/her own name.
define MC = Character("[player_name]", color="#e88a73")
define reg = Character("Registration Lady", color = "#f3c452")
define s = Character("Scarlet",color = "#f3c1f1")
define r = Character("Ria", color = "#9a5c24")
define h = Character("Host", color = "#2b69cd")
define v = Character("Vienna",color = "#5155a1")

define fade = Fade(0.5, 0.0, 0.5)



# The game starts here.

label start:

    $ MC = renpy.input("Choose a name for the player")
    $ MC = MC.strip()

    if MC == "":
        $ MC = "MC"

    scene bg bedroomnight

    play sound "<from 0.0 to 4>alarm-sound.wav"

    # we can add one play music all throught the novel.

    # ACT 1
    "Today is the day of {b} Cherry Apple Academy Annual Tounament {/b}.
    To some students it’s nothing more than a fun adventure,with a chance for a
    big prize. But to me, it’s the chance for a wish that could change my life."

    scene bg entrance
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
    pause



    show scarlet neutral at left with moveinleft
    show mc angry at center with moveinbottom

    show ria neutral at right with moveinright

    "You turn to see Scarlet sneering at you. Of course, the spiteful human
    that she is can’t stand to see someone without powers like you win the
    competition."

    "And since it’s your last year at Cherry Apple Academy for
    Magical Studies, this is the last chance to win the tournament prize we
    both dearly want: the wish-granting dragon's orb."

    init:
        transform flip:
            xzoom -1.0

    show scarlet smirk at flip

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

    show host neutral at center:
        xpos 0.5
    show scarlet neutral at flip:
        yalign 0.5
        linear 0.6 ypos 0.65
    show ria neutral at right


    h "EVERYONE, ARE YOU READY FOR THE GREATEST TOURNAMENT CHERRY APPLE ACADEMY
    HAS EVER HOSTED?"

    "Yells of assent from the large crowd of participants rise in response."

    h "THEN PREPARE YOURSELF! THE TOURNAMENT WILL START IN 3…"

    "Scarlet sneers at you once more before pushing her way to the front of the
    crowd of tournament participants."

    hide scarlet with moveoutleft

    h "2..."

    r "Let’s win this!"

    pause

    hide ria with moveoutright

    h "1..."

    "You imagine yourself lifting up the dragon orb at the end of the
    tournament, summoning the wish-granting dragon, and finally earning
    powers after 19 years. The tournament gates rumble open."

    h "START! REMEMBER- THE FIRST TO GET THROUGH THE TWO ARENAS AND FIND THE
    DRAGON ORB WINS THE PRIZES! MAY THE STRONGEST STUDENT PREVAIL!"


    # End of Act 1.

    # Act 2

    scene forest background

    " As soon as the gates open, the crowd of participants rush forward with
    a roar. By the time you pass through the gates into the forest, the other
    tournament participants have already forged a path going left."

    "A few brave groups break from the crowd and plunge
    towards the right side of the forest arena. You and Ria stop to evaluate
    the best path through the forest."

    show ria neutral at left with moveinleft

    r "Looks like everyone’s going to the left. We should probably stick
    to the crowd for now."

    menu:
        "Take Ria’s advice and go left towards the crowded area - it might be safer.":
            jump left_path

        "Avoid the other participants as much as possible and go right.":
            jump right_path

    # This ends the game.

    return

label left_path:

    show mc neutral at right

    MC "Good idea. Let’s go to the left."

    hide ria neutral with moveoutleft

    "You run left along the path left by other participants, Ria close behind.
    Flashes of light indicate the fighting has already started between
    students hoping to take each other out."

    "Before long, you burst into a clearing in the forest full of students
    fighting each other. You hesitate - getting into a fight with the other
    students would be unnecessary and time consuming."

    "Turning around and finding a different path through the forest would be
    worse. You turn to ask Ria her opinion, but to your surprise she is smiling."


    show ria grinning at left with moveinleft

    r "Don’t worry, MC. I’ll get us through this."

    "You suddenly remember Ria’s power: shielding. Useless for the more
    academic subjects at Cherry Apple Academy, but really helpful when it comes
    to the physical challenges, even though it drains Ria’s energy quickly."

    MC "Thanks, Ria. I’ll leave it to you, then."

    "Ria cracks her knuckles and spreads her hands out in front of her face."
    "Her hands glow unnaturally for a brief second, and then a blue cloud extends
    from her hands, wraps around you both, and becomes a transparent,
    blue-tinted magical shield."

    MC "Nice job, Ria! We can just run right through the clearing like this."

    "You make our way through the clearing, Ria clearing a path for you using
    the shield. A few students try to break through, but quickly give up and turn
    to fight someone else."

    "In no time, you make it through the clearing and
    continue into the forest. Ria releases her shield, looking a little tired"

    show ria tired at left

    MC "Are you ok?"

    show ria happy at left

    r "Yeah, I’m fine. Let’s keep going. I think we’re almost at the end of the forest."

    hide ria happy with moveoutleft

    scene forest trees background with dissolve

    "You walk cautiously through the trees, pushing branches out of the way and
    listening carefully for other students."

    "The forest echoes with the yells
    and crashes from students fighting and occasional growls from what sounds
    like giant forest monsters, which you’ve never seen except in the Dangerous
    Magical Creatures textbook."

    "The trees begin to thin out, and eventually you spot the end of the forest
    ahead. Suddenly Ria whips her head around, and you follow her gaze to see a
    group of forest monsters swarming through the trees and ,
    heading towards you."

    show mc neutral at center:
        xalign 0.5
        linear 0.6 xpos 0.29


    show monster grp at right with dissolve:
        yalign 0.5
        linear 0.6 ypos 0.58


    pause 1.0

    MC "We have to run for it! The second arena is right ahead!"

    "Zigzagging between trees, you both sprint for the end of the forest,
    the hiss and growl of the monsters getting closer with every step."

    show mc neutral at center:
        xalign 0.5
        linear 0.6 xpos 0.85

    show monster purple at left:
        yalign 0.5
        linear 0.6 ypos 0.65

    "You glance back and feel an unpleasant jolt of adrenaline seeing a purple
    forest monster only 10 feet behind, close enough to see its forked tongue
    and the mushrooms on its back."

    "Turning around just in time to swerve around
    a tree and jump over a small creek, you barrel out of the forest, the dirt
    ground abruptly becoming pavement."

    hide monster purple with moveoutbottom
    pause

    hide monstor grp with moveoutbottom
    pause

    show ria angry at left with moveinleft

    "Stumbling to a stop, you turn and see Ria crash out of the forest.
    The monsters stop, then turn and disappear back into the trees.
    Ria grins, and you both laugh triumphantly."

    show mc smirk at center

    show ria grinning at left

    MC "First arena down, only one left to go!"

    "Ria looks towards the second arena suddenly, and her grin fades into shock."

    "That’s the second arena?"

    jump second_arena

    return

label right_path:

    show mc neutral at center with moveinbottom

    MC "There’s too many people going to the left, I think it’s better if we
    go to the right. That way we won’t have to fight other students as much."

    r "Ok. Let’s go."

    "You lead the way, following the less crowded pathway to the right.
    Already yells of students and the growls of some sort of animal echoes
    through the forest, and occasional flashes of light from the left from
    students fighting using their powers. Ria and you walk for a while without
    seeing any other students or animals."

    "You lead the way, following the less crowded pathway to the right.
    Already yells of students and the growls of some sort of animal echoes
    through the forest, and occasional flashes of light from the left from
    students fighting using their powers."

    "Ria and you walk for a while without seeing any other students or animals.
    Suddenly Ria stops and throws out her arm to stop you. You follow her gaze
    to see a group of 3 giant forest monsters foraging for food around about
    30 feet along the path."

    show monster grp at right with moveinright:
        yalign 0.5
        linear 0.6 ypos 0.5

    "You recognize them from your Dangerous Magical Creatures textbook
    by their forked tongue and the mushrooms growing on the back. You remember
    that forest monsters can be extremely aggressive and dangerous when they
    spot a possible threat."

    MC "What should we do? We have to get past the monsters to make it to
    the next arena."

    r "Hmm… we could run past as quickly as possible. But I think it’s better
    to try sneaking past them and try to avoid their attention.
    That way, we won’t have to fight."

    menu:
        "Run past the monsters and risk attack.":
            jump first_track

        "Try to sneak around and lose time.":
            jump second_track

    return


label first_track:

    MC "I don’t want to lose a lot of time here though. Let’s run past and
    if they give chase, we’ll defend ourselves."

    "Ria nods, and starts to create a shield for herself. You pull an
    extendable staff off of your weapons belt. With a flick, it extends to the
    length of your arm."

    MC "On the count of three"
    MC "one..."
    MC "two..."
    MC "three..."


    hide ria angry at left

    "You sprint forward, seeing out of the corner of your eye Ria doing the
    same. The forest monsters hiss, hearing your approach, and begin swarming
    towards you. A large green one crawls towards you and you bring your staff
    down on its head, then sprint away as it recovers."

    hide monstergrp with moveoutbottom
    pause

    show monster blue at right with moveinright
    pause

    "Another blue monster attempts to fight, but you duck away.
    It swings its heavy tail and knocks you off my feet. You manage to
    roll away and jump to your feet, stumbling away."

    "Suddenly, the dirt ground beneath you becomes pavement, and you look
    around, disoriented. You realize that you have exited the forest, and now
    stand in what must be the second arena. The blue monster prowls close,
    hissing, and then turns away and disappears into the trees."

    hide monster blue with moveoutbottom

    show ria tired at left with moveinleft

    "Ria suddenly bursts out of the forest, running at full speed.
    She looks slightly worse for wear; her shield has already disappeared,
    and her uniform sleeve has a long tear in it."

    show mc grinning at center

    MC "We made it! We’re in the second arena!"

    jump second_arena

    return

label second_track:

    MC "You’re right. Let’s go around the monsters and try to stay quiet.
    They’ll probably head towards the other groups that are fighting."

    "Ria nods. Motioning to keep quiet, she moves forward, careful to keep to
    the shadows underneath the trees and keep her footsteps quiet. You follow
    her closely, keeping an eye on the forest monsters."

    "Suddenly, loud bangs and flashes of colored light explode in the sky over
    the left side of the forest, indicating the start of a fight between
    students. The giant forest monsters look up at the noise, and you freeze
    in place. The monsters begin to move towards the left, attracted by the
    noise and light."

    "Ria takes the initiative to move forward, cautiously at first, and then
    faster once we realize the monsters have moved far away."

    hide monster grp

    "I look up and realize the trees are beginning to thin out."

    show ria happy at left

    "We run forward and finally exit the forest. I turn around, disoriented by
    the sudden lack of trees surrounding me. Ria gasps, and I turn to face the
    second arena."

    jump second_arena

    return

label second_arena:

    scene field dragons

    show ria surprised at left
    show mc surprised at right

    "The end of the forest opens onto a wide, flat Gladiator-like arena the
    size of a Quidditch field, with a gigantic dragon at the very end, its tail
    curled around the dragon orb."

    r "woah..."

    MC "A dragon is the obstacle this year? I really can’t believe it…"

    show ria sad at left


    r "Is this even legal? How is anyone supposed to get past the dragon?"

    " You hesitate and scan the arena. A few tournament goers have already
    begun fighting amongst themselves in the arena, but none seem to have made
    it as far as attempting to fight the dragon."

    menu:
        "I don’t know… we just have to find a way.":
            show ria neutral at left
            pause
            r "You’re right. I think I have an idea. As long as we get to the
            dragon first, I can probably lure the dragon away and use my shield
            long enough for you to get the orb."



        "We can and we will. Let’s think of a plan first.":
            show ria neutral at left
            pause
            r "You’re right. I think I have an idea. As long as we get to the
            dragon first, I can probably lure the dragon away and use my shield
            long enough for you to get the orb."

    MC "Good plan! Let’s go then."

    "You lead the way into the second arena. As most of the students fight
    amongst themselves at the center of the arena, you lead Ria to the side of
    the arena and avoid most of the fighting."

    "A group of seniors tries to
    attack you, but you fend them off fairly easily with your staff and Ria
    uses her shield to defend herself."

    "As you approach the dragon at the end of the arena, you notice a student
    has already made it about ¾ of the way to the end."

    "The dragon clambers
    to its feet, flying towards the student, and lands in front, rearing up
    threateningly."

    "The student stands unafraid, and suddenly you notice her pink hair and
    pointy ears. It’s Scarlet."

    hide ria neutral with moveoutbottom

    show scarlet angry at left with easeinleft

    hide mc surprised with moveoutright

    show dragon angry at right with easeinright

    "You freeze in indecision. On one hand, you don’t want to fight either the
    dragon or Scarlet, and you don’t want to throw away your plan with Ria."

    "But Scarlet seems to be dodging death with every second, and no matter how
    much you dislike her, you don’t want her dead."

    "Watching her fight the dragon, you are suddenly remember when Scarlet
    used to be your closest friend."

    scene bg flashback with fade

    show mc child at left with moveinbottom
    show scarlet child at right with moveinbottom

    s "MC! Let’s play ‘Defeat the Dragon’ together today!"

    MC "OK!"

    s "Let’s stay friends forever. You promise, right?"

    MC "Of course!"

    scene field dragons with fade

    show scarlet angry at left with easeinleft
    show dragon angry at right with easeinright
    show mc angry at center with easeinbottom

    "Suddenly, you find yourself running full speed towards Scarlet.
    You vaguely hear Ria yell something after you but you can’t make it out
    over the pounding of your own heart."

    MC "Scarlet!"

    "Scarlet turns, and you yell again, but the dragon whips its tail at her
    and she falls back. You run up to the dragon and it roars, a gust of
    burning hot air stinging your face."

    "The dragon swings its claws at you, but you dodge out of the way,
    dragging Scarlet out of the range of the dragon."

    s "What are you doing?"

    MC "Helping you!"

    "The dragon roars again, and you wince as a burst of fire almost singes
    your hair."

    "The dragon prepares to swing its tail at you, but Scarlet raises
    her hands, glowing unnaturally bright for a brief moment, before a slew of
    ice crystals shoots out at the dragon."

    "One ice crystal manages to lodge in the dragon’s eye, and it roars in fury,
    pawing at its own face. It lumbers to the side painfully, while Ria runs up
    to you and Scarlet."

    hide dragon angry with moveoutright
    show ria angry at right with easeinright

    r "Are you ok?"

    s "I was fine! Why did you come help me? I got hit because of you!"

    MC "You did not look fine! You were going to get burnt or crushed
    without me!"

    r "Hey, let’s not fight-"

    "Scarlet pushes you away, leaving handprints of ice on your uniform."

    show scarlet grinning at left

    show mc angry:
        xalign 0.5
        linear 0.6 xpos 0.58

    s "Let’s settle this once and for all. You versus me."

    MC "Fine."

    "Scarlet raises her hands, ice crystals starting to form, but you
    anticipate her attack and rush forward with your staff,
    forcing her to block your attack."

    "You know that you stand no chance unless in close combat, so even as
    Scarlet jumps away, you pursue her, forcing her to back up towards a huge
    dragon den."

    "Scarlet manages to slash your arm with an ice dagger, while
    you manage to hit her shoulder with your staff.Ria rushes forward and
    tries to get in between Scarlet and you."

    r "Stop"

    "Suddenly, Scarlet pushes Ria hard, hard enough that Ria falls backwards
    towards the dragon, which has turned back towards you all."

    hide ria angry with easeoutright
    show mc sad
    MC "RIA"
    show mc angry at center

    "Ria stumbles to her feet immediately, but collapses, a long scratch on her arm."

    show ria hurt at right with moveinbottom

    "The dragon roars. You turn on Scarlet, only to find her already running away."

    hide scarlet grinning at left

    r "MC, leave me, I’ll be fine. Go catch up to Scarlet. You have to get the orb first."

    menu:
        "Catch up to Scarlet and leave Ria behind":
            MC "I’m sorry. I’ll win for us, I promise."
            jump catch_up_to_scarlet

        "Help Ria, and let Scarlet get ahead":
            MC "MC: Scarlet can wait. You need help right now."
            jump Help_Ria





    return

label catch_up_to_scarlet:

    "You run after Scarlet, ignoring your guilt and pain as you leave
    Ria with the dragon."


    return



label Help_Ria:

    "The dragon roars and thunders towards you. You take out a throwing knife
    and aim, then throw it straight for the dragon’s eye. It turns its head at
    the last moment, and the knife grazes the scales of its head."

    "Enraged, the dragon roars, fire blazing out of its mouth. You drop to the
    group, avoiding the flames, and then jump back up and throw another knife,
    which lodges in the dragon’s eye."

    "It roars in pain and turns away."

    r " MC! Go on. I can handle it from here. Go get the dragon’s egg."

    "You hesitate. It would be poor repayment for Ria’s injury to let Scarlet
    win the tournament prize."

    return
