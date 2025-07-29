# Docker Compose
- To rebuild the Docker Compose environment, use:
  ```bash
  docker compose up --build
  ```
- Restart policies
- "no" - Never attempt to restart the container it it stops or crashes.
- "always" - Always restart the container if it stops or crashes.
- "unless-stopped" - Always restart the container unless it is explicitly stopped by the user.
- "on-failure" - Restart the container only if it exits with a non-zero exit code.

## Using docker volumes
- Volumes are stored in a part of the host filesystem which is managed by Docker (`/var/lib/docker/volumes/` on Linux).
- Volumes are not removed when the container is removed.
- To create a volume when starting a container, use the `-v` or `--mount` flag.
```bash
docker run -v volume_name:/path/in/container image_name
```

## Using multi-stage builds
- Multi-stage builds allow you to use multiple `FROM` statements in a Dockerfile.
- This is useful for separating the build environment from the runtime environment, reducing the final image size.
- Example Dockerfile:
```dockerfile
FROM node:14 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"] \# optional 
```