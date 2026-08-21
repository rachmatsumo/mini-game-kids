const CACHE_NAME = 'main-edu-v12';
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
  './manifest.json',
  './assets/img/favicon.svg',
  './assets/img/favicon-portal.png',
  './assets/img/favicon-space.svg',
  './assets/img/favicon-space.png',
  './assets/img/favicon-garden.svg',
  './assets/img/favicon-garden.png',
  './assets/img/favicon-trace.svg',
  './assets/img/favicon-trace.png',
  './assets/img/favicon-memory.svg',
  './assets/img/favicon-memory.png',
  './assets/img/favicon-match.svg',
  './assets/img/favicon-match.png',
  './assets/img/favicon-sound.svg',
  './assets/img/favicon-sound.png',
  './assets/img/icon-192.png',
  './assets/img/icon-512.png',
  './assets/img/apple-touch-icon.png',
  './assets/img/game-thumbnail/preview-space.png',
  './assets/img/game-thumbnail/preview-garden.png',
  './assets/img/game-thumbnail/preview-trace.png',
  './assets/img/game-thumbnail/preview-memory.png',
  './assets/img/game-thumbnail/preview-match.png',
  './assets/img/game-thumbnail/preview-sound.png',
  './assets/img/game-thumbnail/app-count.png',
  './assets/img/game-thumbnail/app-jump.png',
  './assets/img/game-thumbnail/app-puzzle.png',
  './assets/img/game-thumbnail/app-maze.png',
  './assets/img/game-thumbnail/preview-count.png',
  './assets/img/game-thumbnail/preview-jump.png',
  './assets/img/game-thumbnail/preview-puzzle.png',
  './assets/img/game-thumbnail/preview-maze.png',
  './assets/img/thumbnail.png',
  'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@600;700;800&family=Outfit:wght@600;700;800&display=swap'
];

// Install Event
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[SW] Caching app shell & assets from assets/img...');
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

// Activate Event
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

// Fetch Event - Stale While Revalidate
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        fetch(event.request)
          .then((networkResponse) => {
            if (networkResponse && networkResponse.status === 200) {
              caches.open(CACHE_NAME).then((cache) => {
                cache.put(event.request, networkResponse.clone());
              });
            }
          })
          .catch(() => {});
        return cachedResponse;
      }

      return fetch(event.request)
        .then((networkResponse) => {
          if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
            return networkResponse;
          }
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, responseToCache);
          });
          return networkResponse;
        })
        .catch(() => {
          if (event.request.headers.get('accept') && event.request.headers.get('accept').includes('text/html')) {
            return caches.match('./index.html');
          }
        });
    })
  );
});
