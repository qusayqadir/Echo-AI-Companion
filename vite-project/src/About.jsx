

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

export default function About() {

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
          <Avatar boxSize="50px" name="Logo" src="echo.png" marginRight={2}/>
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

    <Box bg = 'white' p="6" mx="auto">
      <Center>
        <Heading as="h2" size="xl" mb="4">
          About Us!
        </Heading>
      </Center>
    </Box>

    <Spacer>

    <Box
      marginTop="10px"
      p="4"
      mx="auto"
      maxW="4xl"
      bg="gray.100"
      borderRadius="md"
    >
      <Text fontSize="lg" mb="4">
        Welcome to Echo AI, your ultimate companion for dynamic and engaging
        conversations. At Echo, we've crafted a platform that blends advanced AI 
        technology with personalized interactions, allowing you to explore a variety 
        of personas tailored to meet your interests, assist with tasks, or simply 
        provide some enjoyable banter.
      </Text>
      <Text fontSize="lg" mb="4">
        Our chatbot is more than just an AI—it's designed to understand your 
        preferences, adapt to your unique style, and make every interaction feel 
        intuitive and authentic. Whether you're here to learn, seek assistance, or 
        unwind, Echo AI offers a seamless and tailored experience for every user.
      </Text>
      <Text fontSize="lg" mb="4">
        We're dedicated to innovation, accessibility, and security. From our 
        state-of-the-art AI models to our user-friendly design, Echo AI is built 
        with your needs in mind. Plus, with privacy as a top priority, your 
        conversations remain safe and secure, giving you peace of mind while you chat.
      </Text>
      <Text fontSize="lg">
        Join the Echo community today and discover a world of personalized AI 
        interactions. Let's build the future of conversational technology—together!
      </Text>
    </Box>


    </Spacer> 

    <Flex mt="55px">
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