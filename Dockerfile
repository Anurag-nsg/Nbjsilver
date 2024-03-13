FROM vercel/vercel:latest
RUN apt-get update && apt-get install -y libgstreamer-plugins-base1.0-0
