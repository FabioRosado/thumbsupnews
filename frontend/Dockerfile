# RUN npm run build
FROM node:12

# Create app directory
WORKDIR /usr/src/app

# Installing dependencies
COPY package*.json ./
RUN npm install

# Copying source files
COPY . .

# Building app
# TODO: Re-enable when stable
# RUN npm run build
EXPOSE 3000
