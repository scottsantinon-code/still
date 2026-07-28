# Still — guided shower meditation script

Written for the Still sequence: the listener has already done four guided
breaths and read a gratitude before this audio begins. They are standing in
a running shower. No intro, no music, no sign-off. Target ~6 minutes.

Style notes: inspired by Smiling Mind's approach — an opening and closing
check-in, invitational phrasing ("see if you can", "you might notice"),
explicit permission ("however you're arriving is fine", "there's no right
way to do this"), curiosity framing, and "whenever you're ready"
transitions. The closing check-in deliberately leads into the app's mood
question.

Each numbered block is synthesized as one segment. `[silence Ns]` is real
inserted silence between segments, not left to the voice.
Voice: `en-AU-Chirp3-HD-Enceladus`, speakingRate 0.85.

---

1. The water's running. You're here. For the next few minutes there's
   nowhere else you need to be. Just this.

   [silence 6s]

2. Take a moment to check in. How are you arriving? Busy mind, tired,
   rushed — somewhere in between. However you're arriving is fine.
   There's no right way to do this.

   [silence 10s]

3. Let the water land where it lands. Notice the exact place it meets
   you — the crown of your head, the neck, the shoulders. See if you can
   find the line where warm becomes cool.

   [silence 10s]

4. Take one slow breath in through your nose... and let it go, long and
   unhurried. The out-breath is where the body softens. It happens by
   itself.

   [silence 10s]

5. With a bit of curiosity, follow the water down. Forehead. Jaw — let it
   unclench. Across the shoulders, down the spine, along the arms.

   [silence 12s]

6. Your hands. Turn them over. Feel the water pool and part. These hands
   will do a great deal today. For now, they hold nothing.

   [silence 12s]

7. Down through the chest and belly — the breath still going on its own,
   easy, unhurried — all the way to your feet. Holding you up all this
   time, without being asked. Warm water pooling and draining around
   them.

   [silence 14s]

8. Now the sound. Let the water become everything you're listening to.
   Not one sound — thousands, arriving together. Against skin. Against
   tile. Against the floor.

   [silence 15s]

9. If thoughts come — the day, the list, the conversation you're
   rehearsing — that's not a problem. That's just what minds do. Notice
   the thought the way you'd notice a sound. Then come back to the water.

   [silence 15s]

10. Nothing that lands on you stays. Everything is already running off,
    already on its way down and away. You get to stand still, while it
    all keeps moving.

    [silence 18s]

11. Rest here a while. Water, warmth, breath. Nothing to do, nowhere to
    be. The water is always here to come back to.

    [silence 30s]

12. Whenever you're ready, feel the whole body again, all at once. Head
    to feet. Warm. Held. Awake. And check in once more — how are you
    feeling now? Just notice.

    [silence 12s]

13. The day out there will have its own weather. You don't need to carry
    it all at once. One thing at a time — the way water takes one path
    at a time.

    [silence 8s]

14. One more slow breath in... and let it go. Whenever you're ready,
    begin to finish up. You can take this quiet with you. It fits in
    anywhere.

---

## Production

`build-audio.py` synthesizes each segment via Google Cloud TTS
(Chirp 3 HD, billed to project `nanager-f8c08`), joins them with the
silences above, and encodes `meditation.mp3` with lame. After any
regeneration: update `MEDITATION_MS` in `index.html` to the printed
duration and bump the cache version in `sw.js`. (The app also reads the
real duration from the audio itself at runtime; `MEDITATION_MS` is the
fallback if the file fails to load.)
