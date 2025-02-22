# Code Playground





## Project Setup
This Section ensure the installation instructions etc are recorded well for future refence and undesrtanding of code structure.
### Installation Information
Run the following command to install dependencies:

```sh
node -v # If your Node.js version is lower than 18.17.0, update it. 
```

![Ensure Select React ](screenshots/select-react-when-install.png) 

Ensure React + TypeScript+SWC Selected.
![Ensure Select React ](screenshots/selected-reatc&typescript+swc.png) 
This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Here is how Code Structue Looks After Dockerization.
![Ensure Select React ](screenshots/FOLDER-STRUCTURE.png) 
This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.


Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

--------
## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type aware lint rules:

- Configure the top-level `parserOptions` property like this:

```js
export default tseslint.config({
  languageOptions: {
    // other options...
    parserOptions: {
      project: ['./tsconfig.node.json', './tsconfig.app.json'],
      tsconfigRootDir: import.meta.dirname,
    },
  },
})
```

- Replace `tseslint.configs.recommended` to `tseslint.configs.recommendedTypeChecked` or `tseslint.configs.strictTypeChecked`
- Optionally add `...tseslint.configs.stylisticTypeChecked`
- Install [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react) and update the config:

```js
// eslint.config.js
import react from 'eslint-plugin-react'

export default tseslint.config({
  // Set the react version
  settings: { react: { version: '18.3' } },
  plugins: {
    // Add the react plugin
    react,
  },
  rules: {
    // other rules...
    // Enable its recommended rules
    ...react.configs.recommended.rules,
    ...react.configs['jsx-runtime'].rules,
  },
})
```
### Dockerized
docker-compose up --build


