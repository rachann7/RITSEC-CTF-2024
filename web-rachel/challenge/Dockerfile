# Use a lightweight base image
FROM nginx:alpine

# Copy index.html and robots.txt to nginx default public directory
COPY index.html /usr/share/nginx/html
COPY robots.txt /usr/share/nginx/html

# Expose port 80
EXPOSE 80