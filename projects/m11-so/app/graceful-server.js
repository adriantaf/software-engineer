import http from "node:http";

const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-Type": "text/plain" });
  res.end("ok\n");
});

const port = Number(process.env.PORT || 3099);
server.listen(port, "127.0.0.1", () => console.log("listen", port));

function shutdown(signal) {
  console.log("got", signal, "closing…");
  server.close(() => {
    console.log("closed");
    process.exit(0);
  });
  setTimeout(() => {
    console.error("force exit");
    process.exit(1);
  }, 10_000).unref();
}

process.on("SIGTERM", () => shutdown("SIGTERM"));
process.on("SIGINT", () => shutdown("SIGINT"));
