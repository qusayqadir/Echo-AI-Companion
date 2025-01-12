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

import { keyframes } from "@emotion/react";

import { useAuth0 } from "@auth0/auth0-react";

export default function Founders() {

        const { loginWithRedirect, logout, isAuthenticated, isLoading, user, loginWithPopup } = useAuth0();
    
        console.log("isAuthenticated:", isAuthenticated);
        console.log("isLoading:", isLoading);
        console.log("User:", user);

        const gradientAnimation = keyframes`
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
      `;
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

    <Box
      bg="white"
      p="6"
      mx="auto"
      bgGradient="linear(to-r, red, orange, yellow, green, blue, indigo, violet)"
      bgSize="200% 200%" // Makes the gradient span a larger area for animation
      animation={`${gradientAnimation} 8s ease infinite`} // Apply the animation
    >
      <Center>
        <Heading as="h2" size="xl" mb="4" color="white">
          THE Founders.
        </Heading>
      </Center>
    </Box>

    <Flex
      direction="row"
      justifyContent="center"
      align="center"
      p={8}
      bg="gray.50"
      wrap="wrap" // Ensures responsiveness for smaller screens
    >
      {/* First Box */}
      <Box
        bg="white"
        borderRadius="lg"
        boxShadow="lg"
        p={4}
        m={4}
        maxW="300px"
        textAlign="center"
      >
        <Image
          src="me1.png"
          borderRadius="md"
          mb={4}
        />
        <Heading as="h3" size="md" mb={2}>
          Qusay Qadir
        </Heading>
        <Text>Software Engineering II</Text>
      </Box>

      {/* Second Box */}
      <Box
        bg="white"
        borderRadius="lg"
        boxShadow="lg"
        p={4}
        m={4}
        maxW="300px"
        textAlign="center"
      >
        <Image
          src="me2.jpg"
          alt="Placeholder 2"
          borderRadius="md"
          mb={4}
        />
        <Heading as="h3" size="md" mb={2}>
        Jack Vu
        </Heading>
        <Text>Computer Engineering III</Text>
      </Box>

      {/* Third Box */}
      <Box
        bg="white"
        borderRadius="lg"
        boxShadow="lg"
        p={4}
        m={4}
        maxW="300px"
        textAlign="center"
      >
        <Image
          src="me3.png"
          alt="Placeholder 3"
          borderRadius="md"
          mb={4}
        />
        <Heading as="h3" size="md" mb={2}>
          Ryan Brubachar
        </Heading>
        <Text>Computer Engineering III</Text>
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