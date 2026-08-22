const CACHE_NAME = 'main-edu-v24';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './game/game-ketik-luar-angkasa.html',
  './game/game-sensorik-anak.html',
  './game/jejak-huruf.html',
  './game/kartu-ingatan.html',
  './game/cocokkan-huruf.html',
  './game/tebak-suara-hewan.html',
  './game/berhitung-jari.html',
  './game/loncat-pipa-emas.html',
  './game/puzzle-hewan.html',
  './game/labirin-kecil.html',
  './game/sambung-titik.html',
  './game/cerdas-cermat-hewan.html',
  './game/cerdas-cermat-benda.html',
  './game/cerdas-cermat-warna-bentuk.html',
  './game/jam-berapa-sekarang.html',
  './game/piano-mini.html',
  './game/game-logika.html',
  './game/rapikan-kamar.html',
  './game/belajar-membaca.html',
  './manifest.json',
  './score.json',
  './assets/img/favicon.svg',
  './assets/img/favicon.png',
  './assets/img/icon-192.png',
  './assets/img/icon-512.png',
  './assets/img/apple-touch-icon.png',
  './assets/img/game-thumbnail/app-space.webp',
  './assets/img/game-thumbnail/app-garden.webp',
  './assets/img/game-thumbnail/app-trace.webp',
  './assets/img/game-thumbnail/app-memory.webp',
  './assets/img/game-thumbnail/app-match.webp',
  './assets/img/game-thumbnail/app-sound.webp',
  './assets/img/game-thumbnail/app-count.webp',
  './assets/img/game-thumbnail/app-jump.webp',
  './assets/img/game-thumbnail/app-puzzle.webp',
  './assets/img/game-thumbnail/app-maze.webp',
  './assets/img/game-thumbnail/app-dots.webp',
  './assets/img/game-thumbnail/app-quiz.webp',
  './assets/img/game-thumbnail/app-object-quiz.webp',
  './assets/img/game-thumbnail/app-color-shape-quiz.webp',
  './assets/img/game-thumbnail/app-clock-quiz.webp',
  './assets/img/game-thumbnail/app-piano.webp',
  './assets/img/game-thumbnail/app-logika.webp',
  './assets/img/game-thumbnail/app-rapikan-kamar.webp',
  './assets/img/game-thumbnail/app-read.webp',
  './assets/img/game-thumbnail/preview-read.webp',
  './assets/img/thumbnail.png',
  './assets/img/thumbnail.webp'
];

// Install Event
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[SW] Caching app shell v20...');
      return cache.addAll(ASSETS_TO_CACHE).catch((err) => {
        console.warn('[SW] Cache addAll failed, caching individually:', err);
        return Promise.all(
          ASSETS_TO_CACHE.map((url) =>
            cache.add(url).catch((e) => console.warn('[SW] Failed to cache:', url, e))
          )
        );
      });
    }).then(() => self.skipWaiting())
  );
});

// Activate Event - Purge old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cache) => {
          if (cache !== CACHE_NAME) {
            console.log('[SW] Deleting old cache:', cache);
            return caches.delete(cache);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch Event - Network First for HTML, Cache First for static assets
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  const url = new URL(event.request.url);

  // Network First for HTML pages to ensure updates reflect immediately
  if (event.request.mode === 'navigate' || event.request.headers.get('accept')?.includes('text/html')) {
    event.respondWith(
      fetch(event.request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const copy = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, copy));
          }
          return networkResponse;
        })
        .catch(() => caches.match(event.request).then((res) => res || caches.match('./index.html')))
    );
    return;
  }

  // Stale-While-Revalidate for other static assets
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      const fetchPromise = fetch(event.request)
        .then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            caches.open(CACHE_NAME).then((cache) => {
              cache.put(event.request, networkResponse.clone());
            });
          }
          return networkResponse;
        })
        .catch(() => {});
      return cachedResponse || fetchPromise;
    })
  );
});
