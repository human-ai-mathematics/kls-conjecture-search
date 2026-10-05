// The restricted preview on Cloudflare Pages: every request needs the shared password,
// read from the project's secret PREVIEW_PASSWORD (set by .github/workflows/preview.yml).
// Any user name is accepted. Without the secret the site serves nothing: it fails closed.

const REALM = 'Basic realm="KLS preview", charset="UTF-8"';

async function digest(text) {
  const bytes = new TextEncoder().encode(text);
  return new Uint8Array(await crypto.subtle.digest('SHA-256', bytes));
}

// Compare digests, so the time taken does not depend on where the strings differ.
async function same(a, b) {
  const [x, y] = await Promise.all([digest(a), digest(b)]);
  let diff = 0;
  for (let i = 0; i < x.length; i++) diff |= x[i] ^ y[i];
  return diff === 0;
}

function suppliedPassword(request) {
  const [scheme, encoded] = (request.headers.get('Authorization') || '').split(' ');
  if (scheme !== 'Basic' || !encoded) return null;
  let decoded;
  try {
    decoded = new TextDecoder().decode(Uint8Array.from(atob(encoded), (c) => c.charCodeAt(0)));
  } catch {
    return null;
  }
  const colon = decoded.indexOf(':');
  return colon < 0 ? null : decoded.slice(colon + 1);
}

export async function onRequest({ request, env, next }) {
  if (!env.PREVIEW_PASSWORD) {
    return new Response('This preview is not configured.', { status: 503 });
  }
  const supplied = suppliedPassword(request);
  if (supplied === null || !(await same(supplied, env.PREVIEW_PASSWORD))) {
    return new Response('This preview is restricted.', {
      status: 401,
      headers: { 'WWW-Authenticate': REALM, 'X-Robots-Tag': 'noindex, nofollow' },
    });
  }
  const served = await next();
  const response = new Response(served.body, served);
  response.headers.set('X-Robots-Tag', 'noindex, nofollow');
  return response;
}
