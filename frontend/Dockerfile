#
#FROM node:lts-alpine
#WORKDIR /app
#COPY package.json ./
#RUN  npm install
#EXPOSE 8080
#CMD ["npm", "run", "serve"]
#
#
## docker-composer up # to start the compilation process
## to install npm package run
## docker-compose exec web npm i bootstrap

# base image
FROM node:lts-alpine as build

# set working directory
WORKDIR /app

# install and cache app dependencies
COPY package.json /app/package.json
RUN npm install

# add app
COPY . /app

# generate build
RUN npm run build

############
### prod ###
############

# base image
FROM nginx:alpine

# copy artifact build from the 'build environment'
COPY --from=build /app/dist /usr/share/nginx/html

# expose port 80
EXPOSE 80

# run nginx
CMD ["nginx", "-g", "daemon off;"]

# docker build -t vue-prod -f Dockerfile .
# docker run -itd -p 8080:80 vue-prod