FROM nginx:stable

# remove the configuration file of container
RUN rm /etc/nginx/conf.d/default.conf

# copy the configuration file to the container
COPY nginx.conf /etc/nginx/conf.d
