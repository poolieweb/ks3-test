// 6-digit-PIN keyed JSON state store for the ks3-test revision app.
// Free Cloudflare Worker + KV. The PIN is the only auth — threat model is "one kid".
//
// API:
//   OPTIONS /state/:pin            CORS preflight
//   GET     /state/:pin            -> 200 with stored JSON, or 404
//   PUT     /state/:pin   <json>   -> 200 OK (overwrites)

const ORIGINS = [
  "https://poolieweb.github.io",
  "http://localhost:8000",
  "http://localhost:8765",
];

function corsHeaders(req) {
  const origin = req.headers.get("Origin") || "";
  const allow = ORIGINS.includes(origin) ? origin : ORIGINS[0];
  return {
    "Access-Control-Allow-Origin": allow,
    "Access-Control-Allow-Methods": "GET, PUT, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "86400",
    "Vary": "Origin",
  };
}

export default {
  async fetch(req, env) {
    const cors = corsHeaders(req);
    if (req.method === "OPTIONS") return new Response(null, { headers: cors });

    const url = new URL(req.url);
    const m = url.pathname.match(/^\/state\/(\d{6})$/);
    if (!m) return new Response("Not found", { status: 404, headers: cors });
    const pin = m[1];

    if (req.method === "GET") {
      const raw = await env.STATE.get(pin);
      if (!raw) {
        return new Response("null", {
          status: 404,
          headers: { ...cors, "Content-Type": "application/json" },
        });
      }
      return new Response(raw, {
        headers: { ...cors, "Content-Type": "application/json" },
      });
    }

    if (req.method === "PUT") {
      const body = await req.text();
      if (body.length > 1_048_576) {
        return new Response("Too large", { status: 413, headers: cors });
      }
      try { JSON.parse(body); }
      catch { return new Response("Bad JSON", { status: 400, headers: cors }); }
      await env.STATE.put(pin, body);
      return new Response("OK", { headers: cors });
    }

    return new Response("Method not allowed", { status: 405, headers: cors });
  },
};
