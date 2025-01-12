import * as React from 'react'
import { ChakraProvider } from '@chakra-ui/react'
import * as ReactDOM from 'react-dom/client'
import { RouterProvider, createBrowserRouter } from "react-router-dom";

import theme from "./theme"; 

import App from './App'
import About from './About'
import Profiles from './Profiles'
import Founders from './Founders'
import FAQ from './faq';
import Chatbot from './assets/Chatbot';

import { Auth0Provider } from '@auth0/auth0-react';

const rootElement = document.getElementById('root')

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/About",
    element: <About />,
  },
  {
    path: "/Founders",
    element: <Founders />,
  },
  {
    path: "/FAQ",
    element: <FAQ />,
  },
  {
    path: "/Profiles",
    element: <Profiles />,
  },
  {
    path: "/Chatbot",
    element: <Chatbot />
  }

]);

ReactDOM.createRoot(rootElement).render(
  <React.StrictMode>
    <ChakraProvider>
    <Auth0Provider 
        domain={import.meta.env.VITE_AUTH0_DOMAIN} 
        clientId={import.meta.env.VITE_AUTH0_CLIENT_ID} 
        onRedirectCallback
        authorizationParams={{ redirect_uri: window.location.origin }}
        cacheLocation="localstorage"
        useRefreshTokens={true} 
        >
        <RouterProvider router={router} />
      </Auth0Provider>
    </ChakraProvider>
  </React.StrictMode>,
)




