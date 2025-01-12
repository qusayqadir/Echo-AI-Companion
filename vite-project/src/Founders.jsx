import React from "react";
import {
  Image,
  Box,
  Text,
  Spacer,
  Flex,
  Button,
  Center,
  Heading,
  Avatar,
  Link,
} from "@chakra-ui/react";

import { useAuth0 } from "@auth0/auth0-react";

export default function Founders() {

        const { loginWithRedirect, logout, isAuthenticated, isLoading, user, loginWithPopup } = useAuth0();
    
        console.log("isAuthenticated:", isAuthenticated);
        console.log("isLoading:", isLoading);
        console.log("User:", user);
return (
    <>
    <Flex color="gray">
      <Box />
      <Box p="6">
        <Spacer />
        <Heading>
          <Avatar boxSize="50px" name="Logo" src="echo.png" />
          Echo | AI Companion 
        </Heading>
      </Box>
      
      <Spacer />

      <Box p="10">

          <Link href = "/" marginLeft={4} marginRight={4}>
            Home
          </Link>

          <Link href = "/About" marginLeft={4} marginRight={4}>
            About
          </Link>

          <Link href = "/FAQ" marginLeft={4} marginRight={4}>
            FAQ
          </Link>

          <Link href = "/Founders" marginLeft={4} marginRight={4}>
            Founders
          </Link>

        <Button
          onClick={() => {
            if (!isAuthenticated) {
              loginWithPopup();
            } else {
              logout({ returnTo: window.location.origin });
            }
          }}
          colorScheme="gray"
        >
          {!isAuthenticated ? 'Sign In' : 'Log Out'}
        </Button>

      </Box>
    </Flex>

    <Flex>
        <Box marginBottom='-33px' bg='gray.200' w={'100%'}>
          <Center>
            <Text marginTop='1' marginRight={5}>
              Privacy Policy and Terms of Service
              </Text>
            </Center>
          </Box>
        </Flex>

    </>
  );

}