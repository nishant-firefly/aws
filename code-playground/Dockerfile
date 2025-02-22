# Use the latest Node.js version
FROM node:23.7.0 AS builder

# Set working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies inside the container
RUN npm install

# Copy all project files
COPY . .

# Expose the Vite port
EXPOSE 5173

# Start the Vite dev server
CMD ["npm", "run", "dev", "--", "--host"]
