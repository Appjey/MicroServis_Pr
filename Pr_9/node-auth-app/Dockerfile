# syntax=docker/dockerfile:1

FROM node:12.18.1
ENV NODE_ENV=production
RUN git clone https://github.com/AamirNawaz/krakend_with_backend_srv.git /auth
WORKDIR /auth/node-auth-app
RUN npm install
EXPOSE 4500
CMD npm run dev