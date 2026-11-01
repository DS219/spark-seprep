FROM node:22-alpine
WORKDIR /app

RUN npm install -g tsx

COPY randomNumber.ts .

CMD ["tsx", "randomNumber.ts"]

