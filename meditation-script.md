# Still — guided shower meditation script

Written for the Still sequence: the listener has already done four guided
breaths and read a gratitude before this audio begins. They are standing in
a running shower. No intro, no music, no sign-off.

Style notes: inspired by Smiling Mind's approach — an opening and closing
check-in, invitational phrasing ("see if you can", "you might notice"),
explicit permission ("that's okay too", "there's no right way to do this"),
curiosity framing, and "whenever you're ready" transitions. The closing
check-in deliberately leads into the app's mood question.

Each numbered block is synthesized as one segment. `[silence Ns]` is real
inserted silence between segments, not left to the voice.
Voice: `en-AU-Chirp3-HD-Enceladus`, speakingRate 0.85.

---

1. The water's running. You're here. For the next little while there's
   nowhere else you need to be — nothing to work out, nothing to decide.
   Just this.

   [silence 8s]

2. Before anything else, take a moment to check in. How are you arriving?
   Maybe the mind's already busy. Maybe you're tired, or rushed, or
   somewhere in between. However you're arriving is fine. There's no
   right way to do this.

   [silence 12s]

3. Let the water land where it lands. Notice the exact place it meets you —
   the crown of your head, the back of your neck, your shoulders. See if
   you can find the line where warm becomes cool.

   [silence 12s]

4. Take one slow breath in through your nose... and let it go, long and
   unhurried. The out-breath is where the body softens. You don't have to
   make that happen. It happens by itself.

   [silence 12s]

5. Steam rising. Warmth settling in. Let your shoulders drop — not because
   they should. Just to see how it feels.

   [silence 15s]

6. Now, with a bit of curiosity, bring your attention to the top of your
   head. The heat there. The weight of the water — small, steady,
   constant. Follow it down. Forehead. Jaw. Let the jaw unclench.

   [silence 15s]

7. Down the back of the neck. Across the shoulders. Water finds every path
   it can — over the collarbones, down the spine, along the arms. Follow
   one path all the way to the end.

   [silence 18s]

8. Your hands. Turn them over. Feel the water pool and part. You might
   notice warmth, or tingling, or the drum of single drops — or not much
   at all. That's okay too. These hands will do a great deal today. For
   now, they hold nothing.

   [silence 15s]

9. Chest and belly. Notice the breath still going on its own — it doesn't
   need you. Easy. Unhurried.

   [silence 15s]

10. Down the legs. Knees, shins, ankles. And at the very bottom, your
    feet — holding you up all this time, without being asked. Warm water
    pooling and draining around them.

    [silence 18s]

11. Now the sound. Let the water become everything you're listening to.
    It's not one sound — it's thousands, arriving together. Against skin.
    Against tile. Against the floor. As if you're hearing it for the
    first time.

    [silence 18s]

12. If thoughts come — the day, the list, the conversation you're
    rehearsing — that's not a problem. That's just what minds do. See if
    you can notice the thought the way you'd notice a sound. Then come
    back to the water.

    [silence 20s]

13. Nothing that lands on you stays. Everything is already running off,
    already on its way down and away. You get to stand still, while it
    all keeps moving.

    [silence 25s]

14. Rest here a while. Water, warmth, breath. Nothing to do, nowhere to
    be. When the mind wanders — and it will — the water is always here
    to come back to.

    [silence 45s]

15. There's no hurry. This part of the day belongs entirely to you.

    [silence 45s]

16. Whenever you're ready, feel the whole body again, all at once. Head
    to feet. Warm. Held. Awake.

    [silence 15s]

17. Before you finish, check in once more. Notice how you're feeling
    now — whatever that is. No need to hold onto it, or make it stay.
    Just notice.

    [silence 15s]

18. The day is out there, and it will have its own weather. You don't
    need to carry all of it at once. One thing at a time — the way water
    takes one path at a time.

    [silence 15s]

19. One more slow breath in... and let it go.

    [silence 10s]

20. Whenever you're ready — not before — begin to finish up. You can take
    this quiet with you. It fits in anywhere.

---

## Production

`build-audio.py` synthesizes each segment via Google Cloud TTS
(Chirp 3 HD, billed to project `nanager-f8c08`), joins them with the
silences above, and encodes `meditation.mp3` with lame. After any
regeneration: update `MEDITATION_MS` in `index.html` to the printed
duration and bump the cache version in `sw.js`.
