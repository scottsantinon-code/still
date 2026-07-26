# Still

A shower-mounted mindfulness PWA. One tap starts a ~9-minute sequence:
four guided breaths, a gratitude, an 8-minute meditation, a session count,
an optional mood rating. Works fully offline; syncs to Firebase when it can.

## Files

```
index.html      all UI, styles, logic
manifest.json   PWA manifest (portrait, standalone)
sw.js           service worker — precaches everything for offline
meditation.mp3  the guided meditation audio (placeholder — see below)
icon-192.png    home-screen icons
icon-512.png
```

## Deploy to GitHub Pages

1. Create a repo and push:

   ```sh
   git remote add origin git@github.com:YOUR_USERNAME/still.git
   git push -u origin main
   ```

2. On GitHub: **Settings → Pages → Source: Deploy from a branch**, branch
   `main`, folder `/ (root)`. Save.

3. The app appears at `https://YOUR_USERNAME.github.io/still/` after a minute
   or two. All paths are relative, so any repo name or subpath works.

### Put it on the tablet

Open the URL in Safari, **Share → Add to Home Screen**, then launch from the
home-screen icon. That gives you standalone full-screen with the status bar
blended in. Open it once while online so the service worker can precache
everything; after that it runs with no network.

## Swap in the real meditation audio

`meditation.mp3` is currently an 8-minute silent placeholder.

1. Replace `meditation.mp3` with your real file (keep the same filename).
2. Bump the cache version at the top of `sw.js`: `still-v1` → `still-v2`.
3. Commit and push. On the tablet, open the app once while online and give it
   a few seconds to re-download, then it's cached for offline again.

The meditation stage takes its duration from the audio file itself, so the
replacement doesn't have to be exactly 8 minutes. If the audio fails to load
for any reason, the stage falls back to a silent 8-minute timer
(`MEDITATION_MS` in `index.html`).

## Tuning

All timings and content sit at the top of the `<script>` block in
`index.html`: `INHALE_MS`, `EXHALE_MS`, `BREATH_COUNT`, `GRATITUDE_MS`,
`STATS_MS`, and the `GRATITUDES` array — add one string per gratitude, the
app picks at random and won't repeat the previous one.

## Firebase sync (optional)

The app is local-first: every session and mood is written to IndexedDB and
counted from there. Firebase is a background sync layer only — if it's
unconfigured, unreachable, or broken, nothing changes on screen.

1. [console.firebase.google.com](https://console.firebase.google.com) →
   create a project.
2. **Build → Authentication → Sign-in method** → enable **Anonymous**.
3. **Build → Firestore Database** → create a database (production mode).
4. **Project settings → General → Your apps → Web app** → register, copy the
   config object.
5. Paste the values into `FIREBASE_CONFIG` at the top of `index.html`.
   While any value still starts with `YOUR_`, Firebase is skipped entirely.

### Firestore security rules

**Firestore Database → Rules**, publish:

```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{uid}/sessions/{docId} {
      allow read, write: if request.auth != null && request.auth.uid == uid;
    }
    match /users/{uid}/moods/{docId} {
      allow read, write: if request.auth != null && request.auth.uid == uid;
    }
  }
}
```

Records are keyed on client-generated UUIDs (`users/{uid}/sessions/{uuid}`,
`users/{uid}/moods/{uuid}`), so retries overwrite rather than double-count.
The anonymous UID persists on the tablet, so all sessions land under one user.
