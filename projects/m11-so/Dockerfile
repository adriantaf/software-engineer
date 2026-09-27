FROM node:20-bookworm-slim
WORKDIR /app
RUN groupadd -r app && useradd -r -g app app
COPY --chown=app:app app/package.json ./
RUN npm install --omit=dev
COPY --chown=app:app app/ ./
USER app
EXPOSE 3099
CMD ["node", "graceful-server.js"]
