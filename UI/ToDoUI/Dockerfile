FROM node:latest as node
WORKDIR /app
COPY . .
RUN npm install 
RUN npm run build --prod

FROM nginx:stable
COPY --from=builder /dist/todoui /usr/share/nginx/html