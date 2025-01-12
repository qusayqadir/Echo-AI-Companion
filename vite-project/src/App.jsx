// App.jsx
import React from "react";
import { Avatar, Box, Flex, Text, Spacer, Heading, Link, Button, Grid,GridItem, Stack, Center, Image } from "@chakra-ui/react";
import { Routes, Route, Link as RouterLink, useNavigate } from "react-router-dom";

import { useAuth0 } from "@auth0/auth0-react";
import { px } from "framer-motion";

function App() {
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
          <Avatar boxSize="50px" name="Logo" src="echoprofile.png" marginRight={2}/>
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
      <Box />
        <Spacer />
      <Box p="2" marginTop={50}></Box>

        <Spacer />
    </Flex>

    <Grid
        h="440px"
        templateRows="repeat(2, 1fr)"
        templateColumns="repeat(2, 1fr)"
        gap={4}
      >
        <GridItem rowSpan={1} colSpan={1} bg="white" marginTop={10}>
          <Heading>
            <Center>Mental Health Tool</Center>
          </Heading>
        </GridItem>

        <GridItem
          rowSpan={2}
          colSpan={1}
          bgGradient='linear(to-r, gray.800, gray.200)'
          borderRadius={15}
          marginRight={"10"}
        >
          <Heading>
            <Center>
              <Image
                borderRadius={5}
                marginTop="2"
                boxSize="400"
                src="echo.png"
              />
            </Center>
          </Heading>
        </GridItem>

        <GridItem rowSpan={1} colSpan={1} bg="white" marginLeft={"10"}>
          <Box marginTop={-20}>
            <Center>
              <Text fontSize="lg" mb="4">
                Welcome to Echo, the chatbot experience that brings personalized 
                conversations to life. Our AI-powered chatbot mimics the unique texting 
                styles and tones of specific individuals, creating a seamless and engaging 
                communication experience. Whether you're reminiscing about old chats or exploring 
                how someone might respond, Echo combines advanced natural language processing with a 
                touch of creativity to make every conversation feel authentic. 
                With a sleek, user-friendly design and innovative features, Echo is perfect for entertainment, 
                connection, and curiosity. Step into a world of tailored conversations and discover how Echo 
                reflects the voices you know best.
              </Text>
            </Center>
          <Center>
          {!isAuthenticated ? (
            <Button onClick={loginWithPopup} variant={"outline"} bg="gray.200">
              Enter Profiles
            </Button>
          ) : (
            <Button as={RouterLink} to="/Profiles" marginLeft={4} marginRight={4} variant={"outline"} bg={'gray.200'}>
              Enter Profiles
            </Button>
          )}
          </Center>
        </Box>
      </GridItem>
    </Grid>

    <Flex>
      <Spacer />
      <Box p="2" marginTop={55}></Box>
      <Spacer />
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

export default App;
