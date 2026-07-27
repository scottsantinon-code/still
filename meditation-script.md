# Still — guided shower meditation script

Written for the Still sequence: the listener has already done four guided
breaths and read a gratitude before this audio begins. They are standing in
a running shower. No intro, no music, no sign-off.

Each numbered block is synthesized as one segment. `[silence Ns]` is real
inserted silence between segments, not left to the voice. Spoken at a slow
rate (~0.85), total runtime lands around 11 minutes.

---

1. The water's running. You're here. There's nowhere else you need to be
   for the next few minutes — nothing to work out, nothing to decide.
   Just this.

   [silence 8s]

2. Let the water land where it lands. Notice the exact place it meets you —
   the crown of your head, the back of your neck, your shoulders. Notice
   the line where warm becomes cool.

   [silence 12s]

3. Take one slow breath in through your nose... and let it go, long and
   unhurried. The out-breath is where the body softens. You don't have to
   make that happen. It happens.

   [silence 12s]

4. Steam rising. Warmth settling in. Let your shoulders drop — not because
   they should. Just to see how it feels.

   [silence 15s]

5. Bring your attention to the top of your head. The heat there. The weight
   of the water — small, steady, constant. Follow it down. Forehead. Jaw.
   Let the jaw unclench.

   [silence 15s]

6. Down the back of the neck. Across the shoulders. Water finds every path
   it can — over the collarbones, down the spine, along the arms. Follow
   one path all the way to the end.

   [silence 18s]

7. Your hands. Turn them over. Feel the water pool and part. These hands
   will do a great deal today. For now, they hold nothing.

   [silence 15s]

8. Chest and belly. Notice that the breath keeps going on its own — it
   doesn't need you. Easy. Unhurried.

   [silence 15s]

9. Down the legs. Knees, shins, ankles. And at the very bottom, your feet —
   holding you up all this time, without being asked. Warm water pooling
   and draining around them.

   [silence 18s]

10. Now the sound. Let the water become everything you're listening to.
    It's not one sound — it's thousands, arriving together. Against skin.
    Against tile. Against the floor.

    [silence 18s]

11. If thoughts come — the day, the list, the conversation you're
    rehearsing — that's not a problem. That's what minds do. Notice the
    thought the way you'd notice a sound. Then come back to the water.

    [silence 20s]

12. Nothing that lands on you stays. Everything is already running off,
    already on its way down and away. You get to stand still, while it
    all keeps moving.

    [silence 25s]

13. Rest here a while. Water, warmth, breath. Nothing to do. When your
    mind wanders — and it will — the water is always here to come
    back to.

    [silence 45s]

14. There's no hurry. This part of the day belongs entirely to you.

    [silence 45s]

15. Once more, feel the whole body at once. Head to feet. Warm. Held.
    Awake.

    [silence 15s]

16. The day is out there, and it will have its own weather. You don't
    need to carry all of it at once. One thing at a time — the way water
    takes one path at a time.

    [silence 15s]

17. Take one more slow breath in... and let it go.

    [silence 10s]

18. When you're ready — not before — begin to finish up. Carry the quiet
    with you. It fits in anywhere.

---

## Production notes

- Voice: Google Cloud TTS, Chirp 3 HD, `en-AU`. Candidates: Enceladus
  (low, warm male), Sulafat (warm female).
- speakingRate 0.85, LINEAR16 at 24 kHz, segments joined with the silences
  above, encoded to `meditation.mp3`.
- After any regeneration: update `MEDITATION_MS` in `index.html` to the new
  duration and bump the cache version in `sw.js`.
