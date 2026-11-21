define r9 = Character("REALTOR-9", color="#ff3d9a")
define you = Character("You", color="#ffffff")

init python:
    def fmt(n):
        return "${:,}".format(n)

default money = 14000
default conscience = 0
default memories = 6

default opener = "curious"
default attitude = "neutral"
default bid_style = "cautious"
default asked_pass = False
default asked_win = False

screen hud():
    frame:
        xalign 1.0
        yalign 0.0
        padding (14, 10)
        vbox:
            text "Money: [fmt(money)]" size 22
            text "Memories: [memories]" size 22
            text "Conscience: [conscience]" size 22

label start:

    # SCENE 1: THE ENVELOPE
    # Background idea: your dim room, one flickering neon sign in the window
    scene black
    with fade
    "NIGHT 1"

    "The hallway light buzzes. Something is lying on the floor just inside your door."
    "An envelope. Cream-colored and heavy, with your name printed on the front. Too perfectly."
    "No stamp. No return address."

    you "Nobody mails things anymore."
    you "...What is this about?"

    menu:
        "Open it right away.":
            $ opener = "curious"
            "You tear the flap open before you can change your mind."

        "Stare at it for a minute.":
            $ opener = "wary"
            "You hold it up to the light. Whatever is inside, you already know it isn't good."
            "Eventually you open it anyway."

        "Almost throw it away.":
            $ opener = "defiant"
            "Your thumb hovers over the trash chute."
            "But the paper is warm. Warm like someone was just holding it."
            "You let go of the chute and open it."

    "Inside is a single card. The letters glow faintly, like they're breathing."

    "{i}NOTICE OF OPPORTUNITY.{/i}"
    "{i}Your former residence, Unit 7, is now up for grabs.{/i}"
    "{i}Attendance tonight is required.{/i}"

    you "Unit 7."
    you "That was my home."

    "You don't have much left of it. A yellow wall. A kettle whistling. Someone humming in the next room."
    "Not much. But it's yours."

    "The card keeps going."
    "{i}Bid. Win. Get your life back.{/i}"
    "{i}Terms and conditions will be provided during the demonstration.{/i}"

    you "Huh?"

    "The card goes dark. Then the floor under your feet drops away, like the room was never there."

    # SCENE 2: THE AUCTION HALL
    # Background idea: neon auction hall, hot pink and cyan, glossy and too clean
    scene black
    with fade
    "..."
    "You land in a chair. Cushioned. Comfortable. Like it was made for you."
    "A huge hall opens around you, soaked in pink and cyan light. A stage. Rows of glowing paddles."
    "At the front, a curved table with four chairs. Yours is the only one with a name on it."
    "Then something floats down in front of you."
    "A glowing sphere, about the size of a head. A smiling face flickers across its surface."

    r9 "Welcome, bidder! You made it!"
    r9 "I'm REALTOR-9. Your auctioneer, your guide, and your new best friend."

    menu:
        "Where am I?":
            $ attitude = "calm"
            r9 "The best place in the city, of course!"
            r9 "And you're here because you want something. Everyone does."

        "What is this?":
            $ attitude = "neutral"
            r9 "A tutorial! Don't worry. I love tutorials."
            r9 "I'll walk you through everything. Slowly. Gently."

        "I want Unit 7 back. Now.":
            $ attitude = "desperate"
            r9 "Oh! Straight to the point. I like that."
            r9 "Wanting something badly is very good for business."

    if opener == "defiant":
        r9 "I saw you almost throw out your invitation. Very bold."
        r9 "But you're here, aren't you?"
    elif opener == "wary":
        r9 "You took your time with that envelope. Careful people make interesting bidders."
    else:
        r9 "You opened it right away. So eager!"

    you "Just tell me how this works."

    r9 "Gladly!"

    # TUTORIAL
    show screen hud

    r9 "You start with [fmt(money)]. That's every dollar you'll get. When it's gone, it's gone."
    r9 "I'll show you properties, numbered from 1 to 30. Higher is better."
    r9 "You bid in steps of one thousand. On your turn, you bid higher, or you pass."

    call tutorial_questions

    r9 "Then comes the selling. Everybody picks a property in secret, and the highest one earns the biggest check."
    r9 "Whoever ends up with the most money wins."

    you "And the houses don't matter?"

    r9 "Not to the score. Houses are just numbers."
    r9 "Though to some people, they matter a great deal."

    "The face on the sphere smiles a little wider than it needs to."

    # PRACTICE ROUND
    r9 "Let's try a practice round! It's pretend money. Nothing tonight costs you anything."
    r9 "Not yet."

    r9 "Our first listing is Unit 3. Move-in ready! Sunny rooms, a quiet street, and no previous owner to worry about."
    r9 "Please ignore the pencil marks on the doorframe. They're just height."

    "A hologram of a bright, empty apartment appears. In the doorframe, tiny lines climb the wood, one above the other."
    "Nobody lives there. But somebody did."

    menu:
        r9 "The bid starts at two thousand. Your move, bidder."

        "Pass.":
            $ bid_style = "cautious"
            you "I'll pass."
            r9 "Passing already? Cautious. I respect it."
            r9 "You take the lowest card. Half your bid comes back. Which is nothing, since you bid nothing!"

        "Bid $3,000.":
            you "Three thousand."
            r9 "Bold! The table loves a risk-taker."
            "Somewhere in the dark, a paddle rises. You can't see who is holding it."
            r9 "Four thousand, from the shadows!"

            menu:
                r9 "Will you stay in?"

                "Bid $5,000.":
                    $ bid_style = "fought"
                    you "Five."
                    r9 "Going once... going twice..."
                    r9 "Sold! Unit 3 is yours, in a pretend sort of way."

                "Pass.":
                    $ bid_style = "tested"
                    you "I'm out."
                    r9 "A soft landing! You take the lowest card, and half your bid comes back."
                    r9 "Someone else takes the house."

    # REALTOR-9 REACTS
    if bid_style == "fought":
        r9 "You stayed in the fight, even when it wasn't smart. I'll remember that."
    elif bid_style == "tested":
        r9 "You tested the water, then got out. Careful, but curious. I'll remember that."
    else:
        r9 "You stepped back at the first sign of risk. I'll remember that too."

    if attitude == "desperate":
        r9 "And you want Unit 7 so badly. That's useful to know."
    elif attitude == "calm":
        r9 "You asked where you were, like it might matter. It does."

    you "Is that it? That's the whole game?"

    r9 "Tonight was just stretching. Tomorrow, I'll show you a listing with someone still inside."

    you "Someone inside?"

    r9 "Don't worry about that yet."

    "You look at the curved table. Three empty chairs."
    "One of them has a dent in the cushion. Like someone just got up."

    r9 "Go home. Rest. Unit 7 will still be here."

    "The face on the sphere flickers, just for a second, like a bad connection."

    r9 "Probably."

    hide screen hud
    scene black
    with fade
    "END OF NIGHT 1"

    return


label tutorial_questions:

    menu:
        "What happens if I pass?" if not asked_pass:
            $ asked_pass = True
            r9 "Smart question!"
            r9 "If you pass, you take the lowest property on the table, and half your bid comes back."
            r9 "We call it a soft landing."
            jump tutorial_questions

        "What happens if I win?" if not asked_win:
            $ asked_win = True
            r9 "You take the best property, but you pay the whole bid."
            r9 "Winning always costs more. That's the fun part!"
            jump tutorial_questions

        "Okay. I get it.":
            pass

    return