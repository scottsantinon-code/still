/* Still — service worker. Bump CACHE when any precached file changes
   (including swapping meditation.mp3). */
const CACHE = 'still-v8';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './meditation.mp3',
  './icon-192.png',
  './icon-512.png',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE)
      .then((cache) => cache.addAll(ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

/* Safari asks for audio with Range requests and expects a 206 back —
   serve partial content from the cached full response. */
async function partialResponse(fullResponse, rangeHeader) {
  const match = /bytes=(\d+)-(\d+)?/.exec(rangeHeader);
  if (!match) return fullResponse;
  const buffer = await fullResponse.arrayBuffer();
  const start = Number(match[1]);
  const end = match[2] ? Math.min(Number(match[2]), buffer.byteLength - 1) : buffer.byteLength - 1;
  return new Response(buffer.slice(start, end + 1), {
    status: 206,
    statusText: 'Partial Content',
    headers: {
      'Content-Type': fullResponse.headers.get('Content-Type') || 'audio/mpeg',
      'Content-Range': `bytes ${start}-${end}/${buffer.byteLength}`,
      'Content-Length': String(end - start + 1),
      'Accept-Ranges': 'bytes',
    },
  });
}

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  if (new URL(req.url).origin !== location.origin) return; // Firebase / CDN go to network

  event.respondWith((async () => {
    const cached = await caches.match(req, { ignoreSearch: true, ignoreVary: true });
    const range = req.headers.get('range');
    if (cached) {
      return range ? partialResponse(cached, range) : cached;
    }
    try {
      const res = await fetch(req);
      if (res.ok && !range) {
        const cache = await caches.open(CACHE);
        cache.put(req, res.clone());
      }
      return res;
    } catch (err) {
      return cached || Response.error();
    }
  })());
});
